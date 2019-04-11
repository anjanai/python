

# Question 1: Accept two int values from user and return their product. If the product is greater than 1000, then return their sum
def exercise1():
    int1 = int(input("Int1:"))
    int2 = int(input("Int2:"))
    
    prod = int1 * int2
    if prod > 1000:
        prod = int1 + int2
        
    print(prod)


# Question 2: Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number
def exercise2():
    nums = range(6,12)
    prev = 0
    for x in nums:
        sum = x + prev
        print ("{0} + {1} = {2}".format( prev, x, sum))
        prev = x



# Question 3: Accept string from the user and display only those characters which are present at an even index
def exercise3():
    #str = input("string:")
    str = "abcdefg"
    for x in range(0,len(str),2):
        print(str[x])


#Question 4: Given a string and an int n, remove characters from string starting from zero upto n and return a new string
def exercise4(str,n):
    print (str[n:])


#Question 5: Given a list of ints, return True if first and last number of a list is same
def exercise5(list):
    return (list[0] == list[-1])

#Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def exercise6(list):
    for n in list:
        if (n % 5) == 0:
            print (n)

#Question 7: Return the number of times that the string “Emma” appears anywhere in the given string
def exercise7(str):
    print (str.count("Emma"))

# Question 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5  
def exercise8():
    for x in range(1,6):
        s = (str(x) + ' ')*x
        print (s)
            

#Question 9: Reverse a given number and return true if it is the same as the original numbera
def exercise9(num):
    s = str(num)
    t = s[::-1]
        
    print (s,t)
    return (t == s)


#Question 10: Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list
def exercise10 (l1,l2):
    ret = []
    for x in l1:
        if x % 2 == 1:
            ret.append(x)
    for x in l2:
        if x % 2 == 0:
            ret.append(x)

    return (ret)

print (exercise9(234321))
print (exercise10([1,2,3,4],[11,22,33,44]))
    
