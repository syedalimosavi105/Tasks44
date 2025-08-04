password = input("Enter a password: ")

length_ok = len(password) >= 8
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

score = sum([length_ok, has_lower, has_upper, has_digit, has_special])

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Password strength: {strength}")