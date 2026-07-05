import string

password = input("Enter a password: ")

length = len(password) >= 8
uppercase = any(c.isupper() for c in password)
lowercase = any(c.islower() for c in password)
digit = any(c.isdigit() for c in password)
special = any(c in string.punctuation for c in password)

score = sum([length, uppercase, lowercase, digit, special])

if score <= 2:
    print("Password Strength: Weak")
elif score == 3 or score == 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")