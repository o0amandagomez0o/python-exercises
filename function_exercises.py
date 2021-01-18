#!/usr/bin/env python
# coding: utf-8

# # Exercises
# ###### Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.
# 
# 1. Define a function named `is_two`. It should accept one input and return `True` if the passed input is either the number or the string 2, `False` otherwise.

# In[1]:


# is_two(n: int/string/anything) -> bool

def is_two(n):
    return n == 2 or n == '2'
    
is_two(2)


# 2. Define a function named `is_vowel`. It should return `True` if the passed string is a vowel, `False` otherwise.

# In[179]:


#in this ex vowels is a list
def is_vowel(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return n in vowels

is_vowel('U')


# In[182]:


def is_vowel(n):
    
    return n.lower() in 'aeiou'

is_vowel('a')


# In[ ]:


#in this ex vowels is a str
def is_vowel(n):
    vowels = 'aeiou'
    return n in vowels

is_vowel('U')


# 3. Define a function named `is_consonant`. It should return `True` if the passed string is a consonant, `False` otherwise. Use your `is_vowel` function to accomplish this.

# In[184]:


# is_consonant(character:str)-> bool
def is_consonant(n):
    if is_vowel(n.lower()):
        return False
    else: 
        return True

is_consonant('A')


# In[187]:


def is_consonant(n):
    return n.isalpha() and not is_vowel(n)

is_consonant('B')


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[38]:


#word(str)->str

def word(n):
    for char in n[0]:
        if is_consonant(char):
            return n.capitalize()
        else:
            return n
        
        
word('york')


# In[190]:


def capitalize_if_consonant(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word
    
#capitalize_if_consonant('codeup')    
capitalize_if_consonant('easley')   


# 5. Define a function named `calculate_tip`. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[40]:


#calculate_tip(percentage:float, bil: float)->float

def calculate_tip(bill_total, tip_percentage):
    return (f"If your bill total is $ {bill_total}, with a {tip_percentage}% tip, your total payment will be $ {bill_total * ((tip_percentage*.01) +1):.2f}")
    
    
calculate_tip(25.26, 15)    


# In[191]:


def calculate_tip(percentage, bill):
    tip_amt = percentage * bill
    return tip_amt

calculate_tip(.25, 50)


# In[194]:


def calculate_tip(percentage, bill):
    #if the user input is a whole number for the tip
    if percentage > 1:
        percentage /= 100
    tip_amt = percentage * bill
    return round(tip_amt, 2)

calculate_tip(25, 50)


# In[193]:


def calculate_tip(percentage, bill):
    #
    if 0 > percentage > 1:
        raise Exception{'percentage must be between 0 and 1'}
    tip_amt = percentage * bill
    return tip_amt

calculate_tip(25, 50)


# 6. Define a function named `apply_discount`. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[45]:


# apply_discount(price: float, discount: float)-> float

def apply_discount(original_price, discount_percentage):
    return (f"If the original price was ${original_price}, with a {discount_percentage}% discount, you'll only pay ${original_price * (1 - (discount_percentage * .01)):.2f}!")

apply_discount(66.98, 35)
    


# In[196]:


def apply_discount(price, discount):
    discount_amt = price * discount
    return price - discount_amt

apply_discount(66.98, .35)


# 7. Define a function named `handle_commas`. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[47]:


# handle_commas(n:str)->float

def handle_commas(n):
    return int(n.replace(',', ''))
    
    
handle_commas('1,538,456')    


# In[198]:


#by casting as a float, we can handle decimals as well
def handle_commas(n):
    return float(n.replace(',', ''))
    
    
handle_commas('1,538,456.65')  


# 8. Define a function named `get_letter_grade`. It should accept a number and return the letter grade associated with that number (A-F).

# In[53]:


#get_letter_grade(numeric_grade: float)->str

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

# Parenthesis are NOT necessary with returns. 
# python MAY think () = tuple


# 9. Define a function named `remove_vowels` that accepts a string and returns a string with all the vowels removed.

# In[74]:


#remove_vowels(s:str)->str

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


# In[200]:


def remove_vowels(string):
    #look ast each letter in the str
    #if a vowel, remove from str
    new_string = []
    for char in string:
        #char is the argument being called by the is_vowel function
        if not is_vowel(char):
            new_string.append(char)
    #empty str and squish the list together 
    #usually returns should be 'top' level NOT IN THE LOOP
    #If in the loop, the return would break the loop
    return ''.join(new_string)
        
remove_vowels("amanda")    


# ### General rule of thumb:
#    ### `return` 's go at the top-level of a function

# #### `print` stmts can help you develop/visualize your code:

# In[206]:


def remove_vowels(string):
    new_string = []
    print(f"  remove_vowels called! Processing: {string}")
    for char in string:
        print(f"- Start of for loop. Processing: {char}")
        if not is_vowel(char):
            print(f"  Inside if. Adding {char} to new_string ")
            new_string.append(char)
        print(f"  End of for loop. new_string: {new_string}")
    return ''.join(new_string)
        
remove_vowels("Amanda")  


# In[ ]:


def remove_vowels(string):
    #[]'s are used to state that the stmt is creating a list
    #similar to the str we created above: new_string
    return''.join([c for c in string if not is_vowel(c)])

remove_vowels("Amanda") 


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


#def normalize_name(intake):
#    #intake = intake.encode("ascii", errors = "ignore").decode()
#    intake = intake.lower()
#    intake = intake.replace(" ", "_")
#    intake = intake.strip()
#    
#    if intake.isidentifier() == False:
#        return (f"{intake}: This does not pass the Python Identifiers")
#    else:
#        return intake
#    
#    
#normalize_name(" John %doe")    
    


# In[165]:


# Winner Winner chicken dinner!
#normalize_name(s:str)->str
def normalize_name(intake):
    intake = ''.join([s for s in intake if s.isalnum() or s == ' ' or s == '_'])
    intake = intake.strip()
    intake = intake.lower().replace(" ", "_")
    
    if intake.isidentifier() == False:
        return ''.join([i if ord(i) < 128 else '' for i in intake]) 
    else:
        return intake

    
normalize_name(" Jo^h_n √do$e  ")    


# In[114]:


#def normalize_name(intake):
#    #intake = intake.encode("ascii", errors = "ignore").decode()
#    intake = intake.lower()
#    intake = intake.replace(" ", "_")
#    intake = intake.strip()
#    invalids  = ['~', '!','@','#','$','%','^','&','*','(',')','-','.','+'] #[ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "/", "\", |, /, ?, ., >, <, `, ~, ]
#    intake = ''.join((filter(lambda x: x not in invalids, intake)))
#    
#    if intake.isidentifier() == False:
#        return ''.join([i if ord(i) < 128 else '' for i in intake]) #(f"{intake}: This does not pass the Python Identifiers")|
#    else:
#        return intake
#    
#    
#normalize_name(" Joh^n √do$e") 


# In[132]:


#hard codes unicode as invalids to weed out

def normalize_name(intake):
    #intake = intake.encode("ascii", errors = "ignore").decode()
    intake = intake.lower()
    intake = intake.strip()
    intake = intake.replace(" ", "_")

    invalids  = ['~', '!','@','#','$','%','^','&','*','(',')','-','.','+','=','`','|','/','?','<','>',',','.'] #[ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "/", "\", |, /, ?, ., >, <, `, ~, ]
    intake = ''.join((filter(lambda x: x not in invalids, intake)))
    
    for char in range(len(intake)):
        char = str(char)
        if char.isidentifier() == False:
            return ''.join([i if ord(i) < 128 else '' for i in intake]) #(f"{intake}: This does not pass the Python Identifiers")|
                
        else:
            return intake
    
    
#normalize_name(" Joh^n √do$e") 
normalize_name(" Jo…h^n √d-=o$e") 


# In[216]:


def normalize_name(s):
    valid_identifier = []
    print(" removing non-whitespace or alnum")
    for char in s:
        print(f" inside for loop. Processing {char}")
        if char.isidentifier() or char == ' ':
            print(f" adding {char} to list...")
            valid_identifier.append(char)
        print(f"   valid_identifier:  {valid_identifier}")
    valid_identifier = "".join(valid_identifier)
    valid_identifier = valid_identifier.lower()
    print(f"Lowercased and converted to a str")
    print(f"- valid_identifier:  {valid_identifier}")
    valid_identifier = valid_identifier.strip()
    print(valid_identifier)
    valid_identifier = valid_identifier.replace(" ", "_")
    print(valid_identifier)
    
    return valid_identifier
    
normalize_name(" Fi%rst Name")    


# In[ ]:


# ZACH'S CODE

def normalize_name(s):
    valid_identifier = []

    for char in s:
        if char.isidentifier() or char == ' ':
            valid_identifier.append(char)
            
    #convert to string        
    valid_identifier = "".join(valid_identifier)
    #lowercase, remove leading and trailing whitespace
    valid_identifier = valid_identifier.lower()
    valid_identifier = valid_identifier.strip()
    #replace spaces with _
    valid_identifier = valid_identifier.replace(" ", "_")
    
    return valid_identifier
    
normalize_name(" Fi%rst Name")    


# In[152]:


#def normalize_name(intake):
#    #intake = intake.encode("ascii", errors = "ignore").decode()
#    intake = intake.lower()
#    intake = intake.strip()
#    intake = intake.replace(" ", "_")
#
#    #invalids  = ['~', '!','@','#','$','%','^','&','*','(',')','-','.','+','=','`','|','/','?','<','>',',','.'] #[ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "/", "\", |, /, ?, ., >, <, `, ~, ]
#    #intake = ''.join((filter(lambda x: x not in invalids, intake)))
#    
#    for char in range(len(intake)):
#        char = str(char)
#        if char.isidentifier() == False:
#            return ''.join([i if ord(i) < 128 else '' for i in intake]) #(f"{intake}: This does not pass the Python Identifiers")|
#                
#        else:
#            return intake
#    
#    
##normalize_name(" Joh^n √do$e") 
#normalize_name(" Jo…h^n √d-=o$e") 


# In[159]:


#def normalize_name(intake):
#    intake = str(intake)
#    intake = intake.lower()
#    intake = intake.strip()
#    
#    intake = intake.replace(" ", "_")
#
#    #invalids  = ['~', '!','@','#','$','%','^','&','*','(',')','-','.','+','=','`','|','/','?','<','>',',','.'] #[ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "/", "\", |, /, ?, ., >, <, `, ~, ]
#    #intake = ''.join((filter(lambda x: x not in invalids, intake)))
#    
#    for char in range(len(intake)):
#        char = str(char)
#        if char.isidentifier() == False:
#            return ''.join([i if (ord(i) < 128)   else '' for i in intake]) #(f"{intake}: This does not pass the Python Identifiers")|
#                
#        else:
#            return intake
#
#    
#    
##normalize_name(" Joh^n √do$e") 
#normalize_name(" Jo…h^n √d-=o$_e") 


# 11. Write a function named `cumulative_sum` that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[117]:


# cumulative_sum(list_of_numbers: list[int])-> list[int]

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


# In[224]:


#cumulative_sum([1,1,1]) == [1, 2, 3]
#[1, 1+1, 1+2]

def cumulative_sum(lst):
    sums = [lst[0]]
    print(f"Starting out. sums: {sums}")
    #for ea number in the list, add it to the prev total
    for n in lst[1:]:
        print(f"- start of for loop. Processing {n}")
        prev_total = sums[-1]
        sums.append(prev_total + n)
        print(f" End of for loop.  sums: {sums}")
    return sums
    
cumulative_sum([1, 1, 1])


# In[ ]:


def cumulative_sum(lst):
    
    #the 1st number is a special case
    sums = [lst[0]]
    #for ea number in the list, add it to the prev total
    
    #[1:] means take the 2nd element until the end
    #loop through remaining numbers
    for n in lst[1:]:
        #
        prev_total = sums[-1]
        sums.append(prev_total + n)
    return sums
    
cumulative_sum([1, 1, 1])


# ## Bonus
# 
# ### 1. 
# Create a function named `twelveto24`. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# 
#     Bonus write a function that does the opposite.

# In[172]:


def twelveto24(time):
    
    for x in range(len(time)):
        if x == "a":
            return time[:4]
        
        if x == "p":
            return str(int(time[:2]) + 12) + time[2:5]
        
twelveto24("09:45 am")


# In[177]:


def twelveto24(time):
    time = time.lower()
    
    #checking for midnight
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[3:5]
    #checking if am, return the reg time
    elif time[-2:] == "AM":
        return time[:-2]
    #
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    #
    else:
        return str(int(time[:2]) + 12) + time[2:5]
    
    
twelveto24("09:45 AM")    


# ### 2. 
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# 
# - `col_index('A')` returns 1
# 
# - `col_index('B')` returns 2
# 
# - `col_index('AA')` returns 27
#     
# 

# In[ ]:




