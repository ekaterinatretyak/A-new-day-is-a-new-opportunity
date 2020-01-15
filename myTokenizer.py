"""This is a pretty good example of attaining an array
of alphabetical substrings from an arbitrary string"""

import unicodedata
def tokenize(s):
    """This function divides a string in a list of alphabetical substrings."""
    
    i = 0
    l = [] # An array for our future list of substrings
    if len(s) == 0:
        l = []
    # Check each object(index,character) whether it is alpha or not
    for j,c in enumerate(s):
        # If there's an alphabetical character
        # it can be the first char in string
        # or the previous character isn't alpha
        # Write it as a beginning of a substring
        if c.isalpha():
            if not(((j > 0) or (s[j-1].isalpha()))):
                i = j
        # Otherwise, we move on
        else:
            i = j + 1
        # Check whether it is not the last char in the string
        if (j+1 <= len(s)-1):
            # Find the end of alpha substring and add it to list
            if c.isalpha() and not s[j+1].isalpha():
                l.append(s[i:j+1])
            
    # The part below finds the last char in the string
    # and adds it to the array if it is alpha
    if c.isalpha():
        l.append(s[i:])
            
    return l

class MyTokenizer(object):
    """This class tokenizes a string based on the method 'tokenize'"""
    
    def tokenize(self, s):
        """This method takes a string as argument and splits it alphabetical
        substrings from the space to space"""
        i = 0
        l = [] # An array for our future list of substrings
        if len(s) == 0:
            l = []
        # We go through each char in the string
        # and check each object(index,character) whether it is alpha or not
        for j, c in enumerate(s):
            # If there's an alphabetical character
            # it can be the first char in string
            # or the previous character isn't alpha
            # Write it as a beginning of a substring
            if c.isalpha():
                if not(((j > 0) or (s[j-1].isalpha()))):
                    i = j
            # Otherwise, we move on
            else:
                i = j + 1
                
            # Check whether it is not the last char in the string
            if (j+1 <= len(s)-1):
                # Find the end of alpha substring and add it to list
                if c.isalpha() and not s[j+1].isalpha():
                    l.append(s[i:j+1])
            
        # The part below finds the last char in the string
        # and adds it to the array if it is alpha

        if c.isalpha():
            l.append(s[i:])
            
        return l
    
    @staticmethod
    def def_categories(char):
        """This method determines categories of chars in the string
        and adds chars to the arrays"""
        if c.isspace():   
           category = 'SPACE'
        if c.isalpha():
           category = 'ALPHA'
        if c.isdigit():
           category = 'DIGIT'
        if unicodedata.category(c)[0] == 'P':
           category = 'PUNCT'
        else:
           category = 'UNKNOWN'
        return category
              
    def tokenize_categories(self, s):
        """This method returns token, its category and
        index of the 1st and the last char os substring in the user's string"""
        
        i = 0
        words = []
        if len(s) == 0:
            words = []
        # We go through each char in the string
        # and check each object(index,character) whether it is alpha or not
        for i,c in enumerate(s):
            category = self.get_tokens_by_categories(c)
        
            if i == 0:
                index = i
                prevcat = category
            # Check whether it is not the last char in the string
            if (i+1 <= len(s)-1):
                # We compare categories of current and the previous characters
                # if they differ, it is the the last char of the category
                # and we add the substring
                if category != prevcat:
                    token = s[index:i]
                    k = Token(token, prevcat, index, i)
                    words.append(k)
                    index = i
                    prevcat = category
                    
         # The part below finds the last char in the string
         # and checks it
            token = s[index:]
            i = i + 1  
            k = Token(token, category, index, i) 
            words.append(k)         
        return words
         
        
class Token(object):
    """All the substrings belong to the class 'Token'.
    This class represents the next information about a token:
    token: the token itself.
    firstind: the position of the first character.
    lastind: the position of the last character.
    category: the category of the token"""
    
   def __init__(self, token, category, firstind, lastind):      
         self.firstindex = firstind
         self.lastindex = lastind
         self.token = token
         self.category = cat
            
   def __repr__(self):
         """Returns the object representation"""
        return ' ' + self.token + ' is  ' + self.category + ' located from ' + s(self.firstindex) + ' index to ' + s(self.lastindex) + ' index.' + '\n'

    
def main():
    t = myTokenizer()
    s = input()
    print(t.tokenize_categories(s))

if __name__ == '__main__':
    main()

