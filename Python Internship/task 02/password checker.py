
password = input("Password: ")

has_length = len(password) >= 8
has_number = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)

criteria_met = sum([has_length, has_number, has_uppercase])

if criteria_met == 3:
    print("Strong Password")
elif criteria_met == 2:
    print("Moderate Password")
else:
    print("Weak Password")