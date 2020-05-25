"""This is a pretty good example of attaining an array
of alphabetical substrings from an arbitrary string"""

import unicodedata


def strspl(s):
    """This function divides a string in a list of alphabetical substrings."""

    l = []  # An array for our future list of substrings
    if len(s) == 0:
        l = []

    # Check each object(index,character) whether it is alpha or not
    else:
        for j,c in enumerate(s):
        # If there's an alphabetical character
        # it can be the first char in the string
        # or the previous character isn't alpha
        # Write it as a beginning of a substring
            if c.isalpha() and (j == 0 or not s[j-1].isalpha()):
                index = j

        # We should know that we haven't reached
        # the last char in the string
            if (j + 1) <= (len(s) - 1) and c.isalpha() and not s[j + 1].isalpha():
                # Define where the end of alpha substring
                # and we add it to our list
                if c.isalpha() and not s[j+1].isalpha():
                    l.append(s[index:j+1])
        # Otherwise, we've reached the last char in the string
        # and should add it to our list
        if c.isalpha():
            l.append(s[index:])
    return l


class MyTokenizer(object):
    """
    Create this class which contains some methods
     for tokenization of the string

     """
    def tokenize(self,s):
        """
        This method divides our string
        in a list of alpha substrings (tokens)

        """
        l = []
        if len(s) == 0:
            return []
        # Check each object(index,character) whether it is alpha or not
        else:
            for j,c in enumerate(s):
                # If there's an alphabetical character
                # it can be the first char in the string
                # or the previous character isn't alpha
                # Write it as a beginning of a substring
                if c.isalpha() and (j == 0 or not s[j-1].isalpha()):
                    index = j

                # We should know that we haven't reached
                # the last char in the string
                if (j+1) <= (len(s)-1):

                    # Define where the end of alpha substring
                    # and we add it to our list
                    if c.isalpha() and not s[j+1].isalpha():
                        l.append(s[index:j+1])

            # Otherwise, we've reached the last char in the string
            # and should add it to our list
            if c.isalpha():
                l.append(s[index:])
            return l

    @staticmethod
    def make_category(c):

        """
        This method helps us to classify chars in the strings
        depending on their type
        """

        if c.isspace():
            category = 'SPACE'
        elif c.isalpha():
            category = 'ALPHA'
        elif c.isdigit():
            category = 'DIGIT'
        elif unicodedata.category(c)[0] == 'P':
            category = 'PUNCT'
        else:
            category = 'UNKNOWN'
        return category

    def tokenize_cat(self, s):

        """
        This method tokenizes the string in order to add a token,
        its type, index of first and last char of substring in the whole string.
        Moreover, it creates an instance of class Token with attributes
        :param s: a string
        :return: a list of instances of class Token with attributes (substring, its type, firstj, lastj)

        """

        tokens = []
        if len(s) == 0:
            return []
        else:
            for j,c in enumerate(s):
                # Determine type of char
                category = self.make_category(c)

                # We should find the beginning of an substring of one of the category
                # It can be the first char in the string
                # or the char of one type(category),
                # but the previous one belongs to another type.
                # So we save category in order not to call the function when it isn't necessary

                if j == 0:
                    index = j
                    prevcat = category
                # We should know that we haven't reached
                # the last char in the string
                elif (j+1) < len(s):
                    # Now we need to find the end of the substring of one category
                    # and add it to our list. To do so we compare categories of
                    # the current and the next chars. So, if they are different, we've
                    # reached the last char of the category and add the substring to the list
                    if category != prevcat:
                        token = s[index:j]
                        k = Token(token, prevcat, index, j)
                        tokens.append(k)
                        index = j
                        prevcat = category
            # Again we check the last char in the string
            # It is a char of another category
            # and the method adds the last substring to our list
            token = s[index:]
            j = j + 1
            k = Token(token, category, index, j)
            tokens.append(k)

        return tokens

    def gen_tokenize_cat(self, s):

        """
        This method acts like an iterator. It generates instances of class Token
        with attributes
        @param s: a string
        @yield: instances of class Token with attributes (substring, its type, firstj, lastj)
        """
        if len(s) == 0:
            return

        for j,c in enumerate(s):
            # Determine type of char
            category = self.make_category(c)

            # We should find the beginning of an substring of one of the category
            # It can be the first char in the string
            # or the char of one type(category),
            # but the previous one belongs to another type.
            # So we save category in order not to call the function when it isn't necessary
            if j == 0:
                index = j
                prevcat = category
            # We should know that we haven't reached
            # the last char in the string
            elif (j+1) < len(s):
                # Now we need to find the end of the substring of one category
                # and add it to our list. To do so we compare categories of
                # the current and the next chars. So, if they are different, we've
                # reached the last char of the category and add the substring to the list
                if category != prevcat:
                    token = s[index:j]
                    k = Token(token, prevcat, index, j)
                    yield k
                    index = j
                    prevcat = category
        # Again we check the last char in the string
        # It is a char of another category
        # and 'yield' returns a result as a generator element.
        # Then the function starts from the previous yield
        token = s[index:]
        j = j + 1
        k = Token(token, category, index, j)
        yield k

    def gen_alpha_digit_tokens(self,s):
        """ This method generates only those instance of class Token
        which belong to the categories 'ALPHA' or 'DIGIT'
        @param s: a string
        @yield: instances of class Token with attributes (substring, its type, firstj, lastj)
        """
        for token in self.gen_tokenize_cat(s):
            if token.category == 'ALPHA' or token.category == 'DIGIT':
                yield token

class Token(object):

    """
    This class is for tokens which have the substring, type (category) and its first
    and last indexes in the whole string as attributes of the class
    """

    def __init__(self, k, type, start, end):
        """ Let's install the attributes of the class"""
        self.token = k
        self.category = type
        self.firstj = start
        self.lastj = end

    def __repr__(self):
        """ This method returns a printable representation of the object """
        # but we need to convert int to str
        return '(' + self.token + ':' + self.category + ', [' + str(self.firstj) + ', ' + str(self.lastj) + '])'

    def __eq__(self, other):
        """ Compares two instances of class Token.
        If their attributes are equal,
        then they are equal too"""


        # Check whether we have an instance of class Token
        if isinstance(other, Token):

            # Check whether all the attributes of these two instances are equal
            return (self.token == other.token and
                    self.category == other.category and
                    self.firstj == other.firstj and
                    self.lastj == other.lastj)
        # If the other element is not an instance of class Token, we can't compare them.
        # NotImplemented is a special value which should be returned by the binary special methods
        # to indicate that the operation is not implemented with respect to the other type
        return NotImplemented

def main():
    k = MyTokenizer()
    s = input()
    result = strspl(s)
    print("Функция strspl: ", result)
    print("Функция tokenize внутри класса: ", k.tokenize(s))
    print("Типы токенов via tokenize_cat: ", k.tokenize_cat(s))
    a = list(k.gen_tokenize_cat(s))
    print("Генератор типов токенов: ", a)
    b = list(k.gen_alpha_digit_tokens(s))
    print("Генератор типа alpha и digit: ", b)


if __name__ == '__main__':
    main()
