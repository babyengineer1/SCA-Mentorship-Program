
# coding: utf-8

# In[1]:


import string
import random


# In[2]:


length = int(input("Please how long is your password: "))
if length < 6:
    print("Password too short, ensure your password is more than 6 characters")
    length = int(input("Please how long is your password: "))
    
else:
    if length > 6:
        length = int(input("Please how long is your password: "))
        def getpass(length):
            characters = string.ascii_letters + string.punctuation  + string.digits
            return "".join(random.choice(characters) for x in range(length))
    
password = getpass(length)
print(password)

