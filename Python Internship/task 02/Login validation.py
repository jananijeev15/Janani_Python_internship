correct_username = "admin"
correct_password = "password123"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")