"""This is a pretty good example of attaining an array of alphabetical substrings"""

s = input()

def letters(s):
    """Takes a string as input and divides it into alphabetical symbols"""
    i = 0
    l = []
    # Creates a tuple(index,character)
    for j,c in enumerate(s):
        # if there's an alphabetical character
        # and its index isn't more than 0 or the previous character isn't alpha
        # write it as a beginning of a substring
        if c.isalpha():
            if not((j > 0) and (s[j-1].isalpha())):
                i = j
        # if there is a non-alphabetical character
        # and its index is more than 0 and the previous one is alpha
        # it means that there is the end of the substring
        # if the previous character is also non-alpha, we move on
        else:
            if (s[j-1].isalpha()) and (j > 0):
                    l.append(s[i:j])
            if not (s[j-1].isalpha()):
                    i = j + 1
    # while i is less than a string's length
    # add to the array a slice from i to j
    if i < len(s):
        l.append(s[i:])
    return l

y = letters(s)
print(y)

