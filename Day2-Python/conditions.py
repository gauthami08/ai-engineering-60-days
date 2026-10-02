name=input("Enter your name: ")
pythonmarks=int(input("Enter your python marks: "))
mathmarks=int(input("Enter your math marks: "))
computermarks=int(input("Enter your computer marks: "))
totalmarks=pythonmarks+mathmarks+computermarks
average=totalmarks/3
print(name)
print("Total marks:", totalmarks)
print("Average marks:", average)
if pythonmarks>=40 and mathmarks>=40 and computermarks>=40:
    print("PASS")
else:
    print("FAIL")
if average>=90:
    print("Grade: A")
    print("excellent")
elif average>=80:
    print("Grade: B")
    print("very good")
elif average>=70:
    print("Grade: C")
    print("good")
elif average>=60:
    print("Grade: D")
    print("satisfactory")
else:
    print("Grade: F")
    print("you need to work hard")