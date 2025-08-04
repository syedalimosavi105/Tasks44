print("----- USER REGISTRATION -----")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")

full_name = first_name + " " + last_name

print("\n----- REGISTRATION SUMMARY -----")
print(f"Welcome {full_name}!")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Profession: {profession}")
print("Registration completed successfully.")