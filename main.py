username = input("Username:")
password = input("Enter Password:")
confirm_password = input("Confirm Password:")

if password == confirm_password:
    print('password confirmed')
else:
    while password != confirm_password:
        print('password incorrect')
        confirm_password = input("Retype Password")
