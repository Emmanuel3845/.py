username = input("What is your name: ")
password = input("Insert Password: ")
confirm_password = input("Confirm Password: ")

if password == confirm_password:
    print("correct password")
else:
    while password != confirm_password:
        print("retry password")
        password = input("Insert Password: ")
        confirm_password = input("Confirm Password: ")

    if password == confirm_password:
        print("correct password")

# login

login_username = input("What is your login name: ")
login_password = input("Insert Login Password: ")
confirm_loginpassword = input("Confirm Login Password: ")

if password == confirm_loginpassword:
    print("correct password")
else:
    while password != confirm_loginpassword:
        print("retry password")
        password = input("Insert login Password: ")
        confirm_loginpassword = input("Confirm Password: ")

    if password == confirm_loginpassword:
        print("login password correct ")