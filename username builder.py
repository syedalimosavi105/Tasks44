import random

full_name = input("Enter your full name: ")
clean_name = full_name.replace(" ", "").lower()
number = random.randint(10, 99)
username = clean_name + str(number)
print(f"Generated username: {username}")