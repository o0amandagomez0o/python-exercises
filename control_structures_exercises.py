#!/usr/bin/env python
# coding: utf-8

# # Exercises
# ## Do your work for this exercise in a file named control_structures_exercises.py.
# 
# ### 1. Conditional Basics
# 
# - a. prompt the user for a day of the week, print out whether the day is Monday or not

# In[1]:


today = input("What day of the week is today?")

if "Mon" in today:
    print ("Got a case of the Monday's")
else:
    print("TGI-NOT-M!")
print("Let's git some!")


# - b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[4]:


today = input("What day of the week is today?")
today = today.capitalize()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

if today in weekdays:
    print ("Today is a weekday… 💻")
elif today in weekends:
    print ("We're in the weekend! 🌈")
else:
    print("You may want to check your spelling.")


# - c. create variables and make up values for
#     - c.1 the number of hours worked in one week
#     - c.2 the hourly rate
#     - c.3 how much the week's paycheck will be

# In[5]:


hoursworked = 40
payrate = 25.50
paycheck = hoursworked * payrate

paycheck


# In[8]:


# clean up answer
hoursworked = 40
payrate = 25.50
paycheck = hoursworked * payrate

f"${paycheck:.2f} will be your total pay for this week"


#    - d. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
# 

# In[9]:


hrs = 43
rate = 25.5
regpay = hrs * rate
otpay = (rate * 40) + ((hrs-40) * (1.5 * rate))

if hrs > 40:
    print (otpay)
else:
    print (regpay)
    


# ### 2. Loop Basics
# 
# - a. While
# 
#      - a.1 Create an integer variable i with a value of 5.
#      - a.2 Create a while loop that runs so long as i is less than or equal to 15
#      - a.3 Each loop iteration, output the current value of i, then increment i by one.

# In[12]:


i = 5
while i <= 15:
    print (i)
    i += 1


#    - a.4 Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[13]:


n = 0
while n <= 100:
    print (n)
    n += 2


# - a.5 Alter your loop to count backwards by 5's from 100 to -10.

# In[14]:


d = 100
while d >= -10:
    print (d)
    d -= 5


# - a.6 Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# In[18]:


a = 2
while a <= 1000000:
    print (a ** 2)
    a += 1
    


# In[21]:


a = 2

while a <= 1000000:
    print (a)
    a = a ** 2


# - a.7 Write a loop that uses print to create the output shown below.
#     - list backwards by 5's from 100 to 5.

# In[25]:


s = 100
while s >= 5:
    print (s)
    s -= 5
    


# - b. For Loops
# 
#     - b.1 Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# 

# In[34]:


# newer version of str formatting
user_no = int(input("Type a number."))

for i in range(1, 11):
    print(f"{user_no} x {i} = {user_no * i}")


# In[35]:


# older version of str formatting
user_no = int(input("Type a number."))

for i in range(1, 11):
    print(user_no, "x", i, "=", user_no*i)


# In[30]:


# testing for loop
for i in range(1, 11):
    print (i)


# In[33]:


# testing w/o input
user_no = 2

for i in range(1, 11):
    print(user_no, "x", i, "=", user_no*i)


# - b.2 Create a for loop that uses print to create the output shown below.
#     - takes a number starting at 1( to 9) and prints the numeral the amt of times the number is.
# 
# 
# 

# In[36]:


# me trying to math it out
for num in range(1, 10):
    print(num * (11 ** (num - 1)))


# In[37]:


for num in range(1, 10):
    print(str(num) * num)


# - c. break and continue
# 
# - c.1 Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[58]:


# print all odd's and skips the input number
digit = int(input("Type an odd number between 1 - 50."))

for n in range(1, 51):
    if n % 2 == 0 or n == digit:
        continue
    print(f"Here is an odd number: {n}")


# In[73]:


# print all odd's and skips the input number
# takes data type into account and returns message if
#input is not a number but a str
digit = input("Type an odd number between 1 - 50.")

for n in range(1, 51):
    if digit.isdigit() == False:
        print("Please type the digit, do not spell out the word.")
        break
    elif n % 2 == 0: 
        continue
    elif n == int(digit):
        print(f"Yikes! Skipping number: {n}")
        continue
    print(f"Here is an odd number: {n}")
    


# In[127]:


#setting up user input
digit = input("Type an odd number between 1 - 50.")

#checks if input is number
while (digit.isdigit() == False):
    print(f"{digit} is not an ODD number between 1 & 50")
    digit = input("Type an odd number between 1 - 50.")
#checks if input is an even number between 1-50 & checks first while loop AGAIN    
while (int(digit) % 2 == 0) and (int(digit) <= 50 or digit >= 1):
    print(f"Sorry, {digit} not an ODD number between 1 & 50. Please try again.")
    digit = input("Type an odd number between 1 - 50.")
    while (digit.isdigit() == False):
        print(f"{digit} is not an ODD number between 1 & 50")
        digit = input("Type an odd number between 1 - 50.")

for n in range(1, 51):
    if digit.isdigit() == False:
        print("Please type the digit, do not spell out the word.")
        break
    elif n % 2 == 0: 
        continue
    elif n == int(digit):
        print(f"Yikes! Skipping number: {n}")
        continue
    print(f"Here is an odd number: {n}")
    


# - d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[112]:


# int user input
num = input("Please type a Positive Number: ")
#checks if input is a digit
while num.isdigit() == False:
    print(f"{num} is not a Number. Try Again!")
    num = input("Please type a Positive Number: ")
# checks if input is positive    
while (int(digit) < 0):
    print(f"{num} is a negative number. Try Again!")
    num = input("Please type a Positive Number: ")
    
    while num.isdigit() == False:
        print(f"{num} is not a Number. Try Again!")
        num = input("Please type a Positive Number: ")

for d in range(0, int(num) + 1):
    print (d)
    
    


# - e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[119]:


nbr = input("Please type a Positive Integer: ")
#1st loop to check if a digit
while nbr.isdigit() == False:
    print(f"{nbr} is not a Number. Try Again!")
    nbr = input("Please type a Positive Number: ")
    
#2nd loop to check if pos number AND a digit    
while (int(nbr) < 0):
    print(f"{nbr} is a negative number. Try again!")
    nbr = input("Please type a Positive Integer: ")
    
    while nbr.isdigit() == False:
        print(f"{nbr} is not a Number. Try Again!")
        nbr = input("Please type a Positive Number: ")
#3rd loop        
for n in range(int(nbr), 0, -1):
    print(n)
    n -= 1
    


# In[ ]:


#while x = input("Enter a positive number: ")


# ### 3. Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".

# In[123]:


for n in range(1, 101):
    if (n % 5 == 0) and (n % 3 == 0):
        print("FizzBuzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    elif n % 5 == 0:
        print("Buzz")
        continue
    print(n)


# ### 4. Display a table of powers.
# 
# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.

# In[131]:


number = input("What number would you like to go up to? ")

#def printTable(start, end):
for n in range(1, int(number) + 1):
    print(n, n**2, n**3)


# In[145]:


number = input("What number would you like to go up to? ")

#def printTable(start, end):
for n in range(1, int(number) + 1):
    print(n, n**2, n**3)
    
cont = input("Would you like to continue mathing? Y / N ")
cont = cont.upper()

while cont == "Y":
    number = input("What number would you like to go up to? ")
    for n in range(1, int(number) + 1):
        print(n, n**2, n**3)
    cont = input("Would you like to continue mathing? Y / N ")
    cont = cont.upper()
    #if cont == "N":
print("Have a great day!")


# In[ ]:




