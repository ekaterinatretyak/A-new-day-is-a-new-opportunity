"""This is a pretty good example of attaining an array
of alphabetical substrings from an arbitrary string"""

s = input()

def letters(s):
    """Takes a string as input and divides it into alphabetical substrings"""
    i = 0
    l = []  # An array for our future list of substrings
    # Check each object(index,character) whether it is alpha or not
    for j,c in enumerate(s):
        # If there's an alphabetical character
        # And its index isn't more than 0 or the previous character isn't alpha
        # Write it as a beginning of a substring
        if c.isalpha():
            if not((j > 0) and (s[j-1].isalpha())):
                i = j
        # If there is a non-alphabetical character
        # And its index is more than 0 and the previous one is alpha
        # It means that there is the end of the substring
        # If the previous character is also non-alpha, we move on
        else:
            if (s[j-1].isalpha()) and (j > 0):
                    l.append(s[i:j])
            if not (s[j-1].isalpha()):
                    i = j + 1
   # The part below adds the last alphabetical substring in the array
   # As no character stands after the last alphabetical character
   # Though we need an non-alphabetical one to add any substring in the array
    
   if i < len(s):
        l.append(s[i:])
   return l

y = letters(s)
print(y)

