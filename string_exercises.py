#Exercise Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given String

def exercise1(s):
    l = int(len(s)/2)
    return (s[l-1:l+2])

#Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
def exercise2(s1, s2):
    l = int(len(s1)/2)
    return (s1[0:l] + s2 + s1[l:])

#Exercise Question 3: Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string
def exercise3(s1, s2):
    s = ""
    s += s1[0] + s2[0]
    s += s1[int(len(s1)/2)] + s2[int(len(s2)/2)] + s1[-1] +  s2[-1]
    return (s)


#Exercise Question 4: arrange String characters such that lowercase letters should come first
def exercise4 (s):
    defer = ''
    ret = ''
    for i in s:
        if (i < 'Z'):
            defer += i
        else:
            ret += i

    ret += defer
    return (ret)


#Exercise Question 5: Given an input string Count all lower case, upper case, digits, and special symbols
def exercise5 (s):
    d = {}
    for i in s:
        if i >= 'a' and i <= 'z':
            type = 'lower'
        elif i >= 'A' and i <= 'Z':
            type = 'upper'
        elif i >= '0' and i <= '9':
            type = 'digit'
        else:
            type = 'other'
        d[type] = d.get(type, 0)
        d[type] += 1
    return (d)

#Exercise Question 6: Given two strings, s1 and s2, create a mix String
#mixString("Pynative", "Website") = PeytniastbievWe
def exercise6 (s1, s2):
    r2 = s2[::-1]
    z = list(zip(s1,r2))
    ret = ''
    for i,j in z:
        ret += i + j
    return (ret)

#Exercise Question 7: String characters balance Test
# if all the chars in the string1 are there in s2. characters position doesn't matter.
# stringBalanceCheck("yan", "Pynative") = True
def exercise7 (s1, s2):
    for c in s1:
        if c not in s2:
            return False
    return True

#Exercise Question 8: Find all occurrences of 'USA' in given string ignoring the case
def exercise8 (s):
    s = s.lower()
    return (s.count("usa"))

#Exercise Question 9: Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
def exercise9 (s):
    import re

    a = re.findall('\d+',s)
    s = sum(int(i) for i in a)
    return (s, s/len(a))



#Exercise Question 10: Given an input string, count occurrences of all characters within a string
def exercise10 (s):
    count = {}
    for i in s:
        count[i] = count.get(i,0)
        count[i] += 1
    return (count)

print (exercise10("USA is 100, a is 200, b is 300") )
