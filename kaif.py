#Here I have modified the code to include invalid inputs(like non-numeric inputs) and show an error message
#Also I have changed the variable from int to float so that non-integral marks(like 80.5) can also be accepted
while True:
    sub1=input("Enter marks of the first subject: ")
    try:
        a = float(sub1)
        break
    except:
        print("Invalid input. You can enter only numbers between 0 and 100.")
while True:
    sub2=input("Enter marks of the second subject: ")
    try:
        b = float(sub2)
        break
    except:
        print("Invalid input. You can enter only numbers between 0 and 100.")
while True:
    sub3=input("Enter marks of the third subject: ")
    try:
        c = float(sub3)
        break
    except:
        print("Invalid input. You can enter only numbers between 0 and 100.")
while True:
    sub4=input("Enter marks of the fourth subject: ")
    try:
        d = float(sub4)
        break
    except:
        print("Invalid input. You can enter only numbers between 0 and 100.")
while True:
    sub5=input("Enter marks of the fifth subject: ")
    try:
        e = float(sub5)
        break
    except:
        print("Invalid input. You can enter only numbers between 0 and 100.")
avg=(a+b+c+d+e)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
elif(avg>=50 and avg<60):                          #At this point I have added a grade E category for marks between 50 and 60.
    print("Grade: E")
else:
    print("Grade: F")
