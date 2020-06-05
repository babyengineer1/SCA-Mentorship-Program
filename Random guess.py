
# coding: utf-8

# In[1]:


import random
guess = random.randint(0, 20)


# In[2]:


enter_guess = int(input("Please enter your Guess: "))
if enter_guess == guess:
    print("Perfect")
elif enter_guess < guess:
    print("Ooops, your guess is too low")
else:
    print("Ooops, your guess is too high")

