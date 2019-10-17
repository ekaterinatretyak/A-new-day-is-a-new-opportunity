"""This is a pretty good example of attaining an array of alphabetical substrings from a customized string"""

s = input()

def letters(s):
    """Takes a string as input and divides it into alphabetical symbols"""
    i = 0
    l = []  # Define an array
    # Creates a tuple(index,character)
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
    # While i is less than a string's length
    # Add to the array a slice from i to the string's end
    if i < len(s):
        l.append(s[i:])
    return l

y = letters(s)
print(y)

