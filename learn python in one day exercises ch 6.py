# which of the following statements are true

a = 2 > 5
print(a)
# false
b = 9 < 11
print(b)
# true
c = 7 >= 3
print(c) 
# true
d = 8 <= 8 
print(d)
# true
e = 10 != 12
print(e)
# true
f = 6 == 3
print(f)
# false
g = 4 > 2 and 7 != 9
print(g)
# true
h = 3 > 1 and 9 == 9 and 1 > 2
print(h)
# false
i = 2 > 3 or 5 > 1
print(i)
# true
j = 3 > 1 or 5 == 5
print(j)
# true
k = 3 > 1 or 10 != 8 or 9 < 2
print(k)
# true

# Question 2

# determine the outcome without running the code

num = 1
if num == 1:
    print('num is 1')
elif num == 2:
    print('num is 2')
else:
    print('num is neither 1 nor 2')

# output
#  num is neither 1 nor 2

# Question 3

userInput = int(input("Please enter an integer:  "))

if userInput > 0:
    print(userInput)
elif userInput < 0:
    userInput = (userInput * -1)
    print(userInput)
else:
    print("You entered zero")

# Question 4

# userInput = int(input("Please enter an integer from 0 and 100 inclusive:  "))

# if userInput (70 <= 100):
#     print('A')
# elif userInput (60 <= 69):
#     print('B')
# elif userInput (50 <= 59):
#     print('C')
# elif userInput ( 0 <= 49):
#     print('Fail')
# else:
#     print("Invalid")

# Question 5
# determine output



print("Orange Juice" if userInput == 5  else 'Peanut Butter')




# prints Orange Juice

# Question 6

num1 = int(input(" Please enter an integer:  "))

if (num1%2 == 0):
    print('Even')
else:
    print('Odd')

# Question 7
# in list below have program print numbers 1 by 1

Numbers = [1,21,12,45,2,7]

for myNumbers in Numbers:
    print(myNumbers)

# question 8

numbers2 = [12, 4, 3, 17, 20, 19, 16]

for mynumbers2 in numbers2:
    print(mynumbers2)

print(sum(numbers2))

# question 9

# given that classRanking = ['Jane, 'Peter', 'Michael', 'Tom' ] use a for loop and the enumerate()
# method to display the following output
# 1      Jane
# 2        Peter
# 3        Michael
# 4        Tom



classRanking = ['Jane', 'Peter', 'Michael', 'Tom']
    
for index, myclassRanking in enumerate(classRanking, start = 1):
    print(index, "\t", myclassRanking)



# Question 10
# Given that testScores = {'Aaron':12, 'Betty': 17, 'Carol':14 } write a for loop that gives the 
# following output:

# Aaron scored 12 marks
# Betty scored 17 marks
# Carol scored 14 marks


testScores = {'Aaron':12, 'Betty': 17, 'Carol':14}

for i in testScores:
    print("%s scored %d marks" %(i, testScores[i]))

# or
# using the items method

for i,j in testScores.items():
    print ("%s scored %d marks" %(i,j))


# Question 11

# Determine the output of the following code without running the code:

ages = {'Abigail':7, 'Bond':13, 'Calvin': 4}

for i, j in ages.items():
    print('%s\t%s' %(j, i))
    # print('%s\t%s' %(i, j))
# prints 
#  7    Abigail
#  13   Bond
#  4    Calvin

# question 12

message = 'Happy Birthday'

for i in message:
    if (i == 'a'):
        print('@')
    else:
        print(i)

# h
# @
# p
# p
# y
# B
# i
# r
# t
# h
# d
# @
# y

# question 13
# determine the output of the following code without running the code

for i in range(10):
    print(i)

for i in range(2,5):
    print(i)

for i in range (4,10,2):
    print(i)    

#0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 2
# 3
# 4
# 4
# 6
# 8

# question 14

# what is wrong with the following code:

# DO NOT UNCOMMENT - WILL GO ON FOREVER AND YOU WILL HAVE TO FORCE EXIT AND COME BACK IN
# #i = 0
# #while i < 5:
#  #   print('The value if i =',i)

# it will always be less than 5 and never end(results in an infinite loop)

# modify the code so that it produces the following output
# the value of i = 0
# the value of i = 1
# the value of i = 2
# the value of i = 3
# the value of i = 4

i = 0
while i < 5:
    print('The value if i =',i)
    i = i + 1
# NEED THE (variable + 1 in this case (i + 1) or again, will be infinite and have to force quit (exit and come back in))

# Question 15

i = 5

while i>0:
    if i%3 == 0:
        print(i, 'is a multiple of 3')
        i = i - 1
    else:
        print(i, 'is not a multiple of 3')
        i = i - 1

# output 
# 5 is not a multiple of 3
# 4 is not a multiple of 3
# 3 is a multiple of 3
# 2 is not a multiple of 3
# 1 is not a multiple of 3

# NEED THE (variable + 1 in this case (i + 1) or again, will be infinite and have to force quit (exit and come back in))

# Question 16

# write a while loop that repeatedly prompts a user to enter a number or enter 'END' to exit
# if user types 'END' output is 'Goodbye' and ends

while i != "END":
    i = input("Enter a number or END to exit:  ")
    if i == "END":
        print("Goodbye!")
        break
    else:
        print(i)

        
# output
# Enter a number or END to exit:3
# 3
# # Enter a number or END to exit:123
# 123
# Enter a number or END to exit:-2
# -2
# Enter a number or END to exit:END
# END

# Question 17
while i != -1:
    i = int(input("Enter a positive integer or -1 to exit:  "))
    
    if i == -1:
        print("Goodbye!")
        break
    else:
        sum = 0
        for number in range(i):
            sum +=(int(input("Enter a positive integer or -1 to exit: ")))
            print(sum)
            # i = i
            # j = i + i
            # print(i + j)

# now it adds up but does not exit at -1
# unless you subtract total to 0, then enter -1

# Question 18

# modify program so that it displays "you entered a non positive integer" if enter integer other than -1

while True:
    i = int(input("Enter a positive integer or -1 to exit:  "))
    if i < -1:
        print("You entered a non positive integer")
        continue
    elif i == -1:
        print("Goodbye!")
        break
    else:
        sum +=(int(input("Enter a positive integer or -1 to exit: ")))
        print(sum)
            # i = i
            # j = i + i
            # print(i + j)

# now it adds up but does not exit at -1(EXITS IF U ENTER -1 twice after you get totaL to 0)

# question 19

# write a program that prompts the user to enter two integers

p = int(input("Please enter the number of rows:  "))
q = int(input("Please enter the number of asterisks per row:  "))

for _ in range (p):
    print('*' * q)

# def banner(border = '*'):
#     line = border * q
#     print(line)

# banner()

# working on solving this using 
# https://opentechschool.github.io/python-beginners/en/loops.html

for name in "John", "Sam", "Jill":
    print("Hello " + name)


for i in range (10):
    print (i)

total = 0
for i in 5,7,11,13:
    print(i)
    total = total + i

print(total)

for _ in range(10):
    print("Hello")













# def banner(message, border='-'):
#     line = border * len(message)
#     print(line)
#     print(message)
#     print(line)

# banner("Norwegian Blue")

# banner("Sun, Moon and Stars","*")

# banner("Sun, Moon and Stars", border='*')
