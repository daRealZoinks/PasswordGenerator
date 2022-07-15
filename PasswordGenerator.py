import string
import random

characters = string.ascii_letters + string.digits + "!@#$%^&*()"

length = int(
    input("how many characters would you like your password to have? "))

password = ""
for i in range(length):
    password = password+random.choice(characters)

print(password)