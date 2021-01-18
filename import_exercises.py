#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# ### 1.
# Import and test 3 of the functions from your functions exercise file.
# 
# Import each function in a different way:
# 
# - import the module and refer to the function with the `.` syntax
# - use `from` to import the function directly
# - use `from` and give the function a different name

# In[1]:


from function_exercises import is_two

is_two(2)


# In[2]:


import function_exercises

function_exercises.is_vowel('b')


# In[3]:


import function_exercises as fe

fe.word('like')


# #### For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 
# https://docs.python.org/3/library/itertools.html
# 
# ### 1. 
# ### How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[228]:


#from itertools import product
#
#p = 'abc'
#
#q = '123'
#
#def prod(p, q):
#    return list(product(p, q))
#
#prod(p, q)
#
##print len(prod)
#


# In[226]:


#create a list of ways to compbine abd & 123
from itertools import product

p = 'abc'

q = '123'

prod = list(product(p, q))

prod


# In[256]:


#count the prod list
len(list(product(p, q)))


# ### 2. 
# ### How many different ways can you combine two of the letters from "abcd"?

# In[231]:


from itertools import combinations

print (list(combinations('abcd', 2)))


# In[254]:


#from itertools import combinations
#def alpha_combo():
#    combos = list(combinations(['a', 'b', 'c', 'd'], 2))
#    for i in list(combos):
#        print(i)
#        
#alpha_combo()


# In[255]:


len(list(combinations('abcd', 2)))


# Save this file as `profiles.json` inside of your exercises directory. Use the `load` function from the `json` module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# - Total number of users
# - Number of active users
# - Number of inactive users
# - Grand total of balances for all users
# - Average balance per user
# - User with the lowest balance
# - User with the highest balance
# - Most common favorite fruit
# - Least most common favorite fruit
# - Total number of unread messages for all users

# In[7]:


import json
#this is parsing the file
#AKA read
with open('profiles.json') as json_file: #this OPENS the file
    profiles = json.load(json_file) # This reads the file
        
print(profiles)#print out the file profiles.json


# In[8]:


import pandas as pd
#read JSON as a datafrom with Pandas
df = pd.read_json('profiles.json')

df


# In[9]:


#This is a view of the first dictionary in the list[profiles]
profiles[0]


# ### Total number of users

# In[10]:


#counts the number of dictionaries
len(profiles)
print(f"The total number of users is {len(profiles)}")


# In[106]:


def num_users(p):
    len(profiles)
    print(len(profiles))

num_users(profiles)


# ### Number of active users

# In[11]:


isA = []
for indiv in range(len(profiles)):
    if profiles[indiv]['isActive'] == True:
        isA.append(True)
    
print(isA)
print(sum(isA))
print(f"The total number of ACTIVE users is {sum(isA)}")


# In[107]:


def active_users(p):
    isA = []
    for indiv in range(len(profiles)):
        if profiles[indiv]['isActive'] == True:
            isA.append(True)
    print(sum(isA))

active_users(profiles)


# ### Number of inactive users

# In[12]:


isInA = []
for indiv in range(len(profiles)):
    if profiles[indiv]['isActive'] == False:
        isInA.append(int(1))
    
print(isInA)
print(sum(isInA))
print(f"The total number of INACTIVE users is {sum(isInA)}")


# In[108]:


def inactive_users(p):
    isInA = []
    for indiv in range(len(profiles)):
        if profiles[indiv]['isActive'] == False:
            isInA.append(int(1))
    print(sum(isInA))
    
inactive_users(profiles)


# In[20]:


type(profiles)


# In[21]:


type(profiles[0])


# ### Grand total of balances for all users

# In[48]:


bal = [sub['balance'] for sub in profiles]

bal = list(bal)

print(bal)


# In[52]:


n_bal = [c.replace("$", "").replace(",", "") for c in bal]


print(n_bal)


# In[53]:


type(n_bal)


# In[257]:


bals = []

for item in n_bal:
    bals.append(float(item))

bals


# In[57]:


#print(sum(bals))
#print(f"The grand total of balances for all users is ${sum(bals)}")


# In[109]:


def total_bal(b):
    bals = []
    
    for item in n_bal:
        bals.append(float(item))
    print(sum(bals))
    
total_bal(bals)    


# ### Average balance per user

# In[260]:


avg_bal = sum(bals) / len(profiles)

(avg_bal)


# In[81]:


type(avg_bal)


# In[116]:


def avg_user_bal(p):
    avg = sum(bals) / len(profiles)
    print(round(avg, 2))
    
avg_user_bal(profiles)


# ### User with the lowest balance

# In[90]:


# used pandas to view the two columns i need for the 
# next 2 questions
#0: is starting at the first diction and running through them all
df.loc[0:, ['name', 'balance']]


# In[101]:


#for dictionary in profiles:
#    for key in dictionary:
#        print(key, ":", dictionary[key])


# In[261]:


#for key in profiles:
#    print(profiles[key])


# In[263]:


# created a list of all names
users = [sub['name'] for sub in profiles]

users = list(users)

users


# In[262]:


bals


# In[121]:


print(users)


# In[264]:


#merged the two lists together
#with balances as the key(1st), and users as the value(2nd)
zipbObj = zip(bals, users)

dictOfNamesAndBals = dict(zipbObj)

dictOfNamesAndBals


# In[130]:


#returns all of the values in the dict I created
#since I listed users 2nd, they are the values
dictOfNamesAndBals.values()


# In[131]:


#sorted() changed my dict of keys and values into a list() of tuples
# Sorted my dict in ASC order of keys
sorted(dictOfNamesAndBals.items())


# In[133]:


#selected the 1st in my list with the lowest balance
sorted(dictOfNamesAndBals.items())[0]


# In[134]:


type(sorted(dictOfNamesAndBals.items()))


# ### User with the highest balance

# In[136]:


#reversed my list to DESC order
sorted(dictOfNamesAndBals.items(), reverse = True)


# In[137]:


#selected the 1st in my list with the highest balance
sorted(dictOfNamesAndBals.items(), reverse = True)[0]


# ### Most common favorite fruit

# In[209]:


#created a list of fav fruit from dicts in profiles list
fruit = [sub['favoriteFruit'] for sub in profiles]

fruit = list(fruit)

fruit


# In[210]:


#tallied up the diff fruits
# https://docs.python.org/3/library/collections.html#collections.Counter.most_common
from collections import Counter

Counter(fruit)


# In[212]:


#identified my key/values from the dict I created above
#and returned the most common fruit

v = list(Counter(fruit).values())
k = list(Counter(fruit).keys())

max_fruit = k[v.index(max(v))]

max_fruit


# In[215]:


#printed both key and value
print(k[v.index(max(v))], ': ', v[v.index(max(v))])


# ### Least most common favorite fruit

# In[216]:


#fruit = [sub['favoriteFruit'] for sub in profiles]
#
#fruit = list(fruit)
#
#fruit


# In[217]:


#from collections import Counter
#
#Counter(fruit)


# In[206]:


#min_fruit = min(Counter(fruit), key = lambda k: Counter(fruit)[k])
#
#Counter(fruit)[min_fruit]


# In[208]:


# https://blog.finxter.com/how-to-get-the-key-with-the-maximum-value-in-a-dictionary/
#min(dict_name, key = dict_name.get)
#min function reviews all keys and returns the on with the min VALUE
#.get returns the value of the KEY
min_fruit = min(Counter(fruit), key = Counter(fruit).get)

min_fruit


# ### Total number of unread messages for all users

# In[192]:


#create a list of strings
#pulled from the 'greetings' key of the dict.s in [profiles]
greetings = [sub['greeting'] for sub in profiles]

greetings = list(greetings)

greetings


# In[142]:


type(greetings)


# In[143]:


greetings[0]


# In[144]:


[int(i) for i in greetings[0].split() if i.isdigit()]


# In[218]:


#[int(i) for i in greetings[0:20].split() if i.isdigit()]


# In[153]:


#for numbers in range(0, 19):
#    numberOfMessages = []
#    
#    numberOfMessages.append([int(i) for i in greetings[numbers].split() if i.isdigit()])
#    
#    print(numberOfMessages)


# In[167]:


#for numbers in range(0, 20):
#    numberOfMess = [int(i) for i in greetings[numbers].split() if i.isdigit()]
#
#    
#    print(numberOfMess)


# In[168]:


#messagesTotal = []
#for n in range(0, 19):
#    for i in greetings[n].split():
#        if (i.isdigit()):
#            messagesTotal.append(i)
#            
#print(messagesTotal)


# In[183]:


#created an empty list
messagesTotal = []
#for loop for the len of the list(greetings)
for n in range(len(greetings)):
    #split every character in each string 
    for i in greetings[n].split():
        #and checked if it was a digit, if so, appended to the empty list
        if (i.isdigit()):
            messagesTotal.append(i)
            
messagesTotal


# In[187]:


messagesTotal = []
for n in range(len(greetings)):
    for i in greetings[n].split():
        if (i.isdigit()):
            messagesTotal.append(i)
            
#converted the appended list of strings to int, and summed it
sum([int(i) for i in messagesTotal])


# In[180]:


#checking difference between range(0, 19) & len(greetings)
#messagesTotal = []
#for n in range(0, 19):
#    for i in greetings[n].split():
#        if (i.isdigit()):
#            messagesTotal.append(i)
#            
#messagesTotal = [int(i) for i in messagesTotal]
#
#messagesTotal


# In[174]:


#checking if sum function works
#messagesTotal = []
#for n in range(0, 19):
#    for i in greetings[n].split():
#        if (i.isdigit()):
#            messagesTotal.append(i)
#
#sum([int(i) for i in messagesTotal])

