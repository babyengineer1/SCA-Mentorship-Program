import random
import string

chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
#password = " "
while True:
    #password = " "
    num_alp = int(input("How many letters do you want?:"))
    nums = int(input("How many numbers do you want?: "))
    length = int(input("Please how long is your password: "))
    if length > 6:
        print("Good")
        break
    else:
        print("Password too short, ensure your password is more than 6 characters")

def getpass(num_alp,nums,length):
    password = ""  
    for i in range(num_alp):
        password += random.choice(string.ascii_letters)
    for x in range(nums):
        password += random.choice(string.digits)
    for y in range(length):
        password += random.choice(string.punctuation)
    pass_word = list(password)
    shuff = random.shuffle(pass_word)
    new_pass = "".join(pass_word)
    return new_pass

new_password = getpass(num_alp,nums,length)
print(new_password)
#password = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits) for x in range(length,nums,num_alp))
#print(password)