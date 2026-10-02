user=input("Enter your username: ")
password=int(input("Enter your password: "))
if user=="admin" and password==1234:    
    print("Login successful.")
else:
    print("Login failed. Please check your username and password.")