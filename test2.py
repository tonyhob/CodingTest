import re   #Standard Liabrary of Python From: https://docs.python.org/3.5/library/re.html

str1 = input()

def removechar(temp):
    newstr = re.sub(r'\W+', '', temp)
    return newstr

def compare(a):
        length = len(a)
        half = int(length / 2)
        for x in range(half):
                if a[x] != a[length-x-1]:
                        return 'No'
        return 'Yes'

print(compare(removechar(str1)))
