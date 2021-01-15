#!/usr/bin/env python
# coding: utf-8

# # Exercises
# ###### Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.
# 
# 1. Define a function named `is_two`. It should accept one input and return `True` if the passed input is either the number or the string 2, `False` otherwise.

# In[1]:


# is_two(n: int/string) -> int

def is_two(n):
    return n == 2 or n == '2'
    
is_two(2)


# 2. Define a function named `is_vowel`. It should return `True` if the passed string is a vowel, `False` otherwise.

# In[2]:


def is_vowel(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return n.lower() in vowels

is_vowel('U')


# 3. Define a function named `is_consonant`. It should return `True` if the passed string is a consonant, `False` otherwise. Use your `is_vowel` function to accomplish this.

# In[33]:


def is_consonant(n):
    if is_vowel(n.lower()):
        return False
    else: 
        return True

is_consonant('A')


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[38]:


def word(n):
    for char in n[0]:
        if is_consonant(char):
            return n.capitalize()
        else:
            return n
        
        
word('york')


# 5. Define a function named `calculate_tip`. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[40]:


def calculate_tip(bill_total, tip_percentage):
    return (f"If your bill total is $ {bill_total}, with a {tip_percentage}% tip, your total payment will be $ {bill_total * ((tip_percentage*.01) +1):.2f}")
    
    
calculate_tip(25.26, 15)    


# 6. Define a function named `apply_discount`. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[45]:


def apply_discount(original_price, discount_percentage):
    return (f"If the original price was ${original_price}, with a {discount_percentage}% discount, you'll only pay ${original_price * (1 - (discount_percentage * .01)):.2f}!")

apply_discount(66.98, 35)
    


# 7. Define a function named `handle_commas`. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[47]:


def handle_commas(n):
    return int(n.replace(',', ''))
    
    
handle_commas('1,538,456')    


# 8. Define a function named `get_letter_grade`. It should accept a number and return the letter grade associated with that number (A-F).

# In[53]:


def get_letter_grade(g):
    if g >= 90:
        return ("You have an A!")
    elif g >= 80:
        return ("You have an B!")
    elif g >= 70:
        return ("You have an C!")
    elif g >= 60:
        return ("Go to tutoring, you have an D!")
    else:
        return ("Go to tutoring, you have an F!")
    
get_letter_grade(23)


# 9. Define a function named `remove_vowels` that accepts a string and returns a string with all the vowels removed.

# In[74]:


def remove_vowels(s):
    s = s.lower()
    for char in s:
        if is_vowel(char):
            return str(s.replace(char, ''))
        
        
remove_vowels("amanda")


#def word(n):
#    for char in n[0]:
#        if is_consonant(char):
#            return n.capitalize()
#        else:
#            return n


# 10. Define a function named `normalize_name`. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[99]:


def normalize_name(intake):
    #intake = intake.encode("ascii", errors = "ignore").decode()
    intake = intake.lower()
    intake = intake.replace(" ", "_")
    intake = intake.strip()
    
    if intake.isidentifier() == False:
        return (f"{intake}: This does not pass the Python Identifiers")
    else:
        return intake
    
    
normalize_name(" John %doe")    
    


# In[101]:


def normalize_name(intake):
    #intake = intake.encode("ascii", errors = "ignore").decode()
    intake = intake.lower()
    intake = intake.replace(" ", "_")
    intake = intake.strip()
    
    for char in intake:
        if char.isascii():
            return ("" + char)
    #    elif intake.isidentifier() == False:
    #        return (f"{intake}: This does not pass the Python Identifiers")
    #    else:
    #        return intake
        
    
normalize_name(" John √do$e")    


# In[114]:


def normalize_name(intake):
    #intake = intake.encode("ascii", errors = "ignore").decode()
    intake = intake.lower()
    intake = intake.replace(" ", "_")
    intake = intake.strip()
    invalids  = ['~', '!','@','#','$','%','^','&','*','(',')','-','.','+'] #[ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "/", "\", |, /, ?, ., >, <, `, ~, ]
    intake = ''.join((filter(lambda x: x not in invalids, intake)))
    
    if intake.isidentifier() == False:
        return ''.join([i if ord(i) < 128 else '' for i in intake]) #(f"{intake}: This does not pass the Python Identifiers")|
    else:
        return intake
    
    
normalize_name(" Joh^n √do$e") 


# 11. Write a function named `cumulative_sum` that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[117]:


def cumulative_sum(lst):
    return [sum(lst[:n+1]) for n in range(len(lst))]
 
#cumulative_sum([1, 1, 1])
cumulative_sum([1, 2, 3, 4])


# In[121]:


#def cumulative_sum(lst):
#    x = 0
#    for s in range(0, len(lst)):
#        x += lst[s]
#        list.append(x)
# 
#cumulative_sum([1, 1, 1])
#cumulative_sum([1, 2, 3, 4])


# In[ ]:




