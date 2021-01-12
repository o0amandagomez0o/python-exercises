"""
Create a Python script file named data_types_and_variables.py. 
Inside it, write some Python code, that is, variables and operators, 
to describe the following scenarios. 
Do not worry about the real operations to get the values, 
the goal of these exercises is to understand how real world conditions can be represented with code.
"""

# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
rental = 3
TheLittleMermaid = 3
BrotherBear = 5
Hercules = 1

Movies = [TheLittleMermaid, BrotherBear, Hercules]

sum(Movies)

totalbill = sum(Movies) * rental

totalbill

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

G_Payrate = 400
A_Payrate = 380
FB_Payrate = 350

G_hrs = 6
A_hrs = 4
FB_hrs = 10

totalPay = (G_Payrate * G_hrs) + (A_Payrate * A_hrs) + (FB_Payrate * FB_hrs)

totalPay

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
classFull = False
sch_conflict = False

student_enroll = not sch_conflict and not classFull

student_enroll

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
purchase2more = True
offerexp = False

applyoffer = purchase2more and not offerexp

applyoffer


# Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# # Create a variable that holds a boolean value for each of the following conditions:

username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters
minpswd = len(password)
minpswd >= 5

# the username must be no more than 20 characters
maxid = len(username)
maxid <= 20

# the password must not be the same as the username
username != password

# bonus neither the username or password can start or end with whitespace
username[0] and username[-1] and password[0] and password[-1] != ' '
