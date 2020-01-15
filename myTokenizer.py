"""This is a pretty good example of attaining an array
of alphabetical substrings from an arbitrary string"""

import unicodedata

class MyTokenizer(object):
    """This class tokenizes a string based on the method 'tokenize'"""
    def get_tokens_by_categories(self, s):
        cat = {'SPACE': [],
                'ALPHA': [],
                'DIGIT': [],
               'UNKNOWN': []}
        for c in s:
                if c.isspace():
                    cat['SPACE'].append(c)
                if c.isalpha():
                    cat['ALPHA'].append(c)
                if c.isdigit():
                    cat['DIGIT'].append(c)
                else:
                    cat['UNKNOWN'].append(c)
                return cat
    def tokenize_all_substrings(self, s):
        if len(s) == 0:
            l = []
        words = []
        index = 0
        cat = self.get_tokens_by_categories(s[0])
        for j, c in enumerate(s):
            current_cat = self.get_tokens_by_categories(s)
            if current_cat != self.get_tokens_by_categories(s[j-1]) and j>0:
                token = s[index:j]
                k = Token(token, index, cat)
                words.append(k)
                index = j
                cat = current_cat
        if index < len(s):
            token = s[index:]
            k = Token(token, index, cat)
            words.append(k)
        return words
    
    def tokenize(self, s):
        """This method takes a string as argument and splits it alphabetical
        substrings from the space to space"""
        i = 0
        l = [] # An array for our future list of substrings
        # Check each object(index,character) whether it is alpha or not
        if len(s) == 0:
            l = []
        for j,c in enumerate(s):
            # If there's an alphabetical character
            # And its index isn't more than 0
            #or the previous character isn't alpha
            # Write it as a beginning of a substring
            if c.isalpha():
                if not(((j > 0) or (s[j-1].isalpha()))):
                    i = j
            else:
                i = j + 1
                
            # If there is a non-alphabetical character
            # And its index is more than 0 and the previous one is alpha
            # It means that there is the end of the substring
            # If the previous character is also non-alpha, we move on
            
            if (j+1 <= len(s)-1):
                if c.isalpha() and not s[j+1].isalpha():
                    l.append(s[i:j+1])
            
        # The part below adds the last alphabetical substring in the array
        # As no character stands after the last alphabetical character
        # Though we need an non-alphabetical one
        #to add any substring in the array

        if c.isalpha():
            l.append(s[i:])
            
        return l
def tokenize(s):
    i = 0
    l = [] # An array for our future list of substrings
    # Check each object(index,character) whether it is alpha or not
    if len(s) == 0:
        l = []
    for j,c in enumerate(s):
        # If there's an alphabetical character
        # And its index isn't more than 0
        #or the previous character isn't alpha
        # Write it as a beginning of a substring
        if c.isalpha():
            if not(((j > 0) or (s[j-1].isalpha()))):
                i = j
        else:
            i = j + 1
            # If there is a non-alphabetical character
            # And its index is more than 0 and the previous one is alpha
            # It means that there is the end of the substring
            # If the previous character is also non-alpha, we move on
        if (j+1 <= len(s)-1):
            if c.isalpha() and not s[j+1].isalpha():
                l.append(s[i:j+1])
            
        # The part below adds the last alphabetical substring in the array
        # As no character stands after the last alphabetical character
        # Though we need an non-alphabetical one
        #to add any substring in the array

    if c.isalpha():
        l.append(s[i:])
            
    return l
        
    
class Token(object):
    def __init__(self, token, index, cat):
        self.token = token
        self.index = index
        self.cat = cat
    def __repr__(self):
        return self.token + ":" + s(self.index) + s(self.cat)


def main():
    t = MyTokenizer()
    s = input()
    print(t.tokenize(s))
    print(tokenize(s))
    print(t.tokenize_all_substrings(s))
   

if __name__ == '__main__':
    main()

