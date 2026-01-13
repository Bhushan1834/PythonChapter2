# PythonChapter2
# Question: Find the greatest of four numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a>b and a>c and a>d):
    print("Greatest number is a:",a)
elif(b>a and b>c and b>d):
    print("Greatest number is b:",b)
elif(c>a and c>b and c>d):
    print("Greatest number is c:",c)
elif(d>b and d>b and d>c):
    print("Greatest number is d:",d)



# Question: Check if a student has passed or failed.
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = (m1 + m2 + m3) / 300

if total >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Pass")
else:
    print("Fail")


# Question: Detect spam comments using keywords.
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = " click this"

message = input("Enter your comment: ")

if((p1 in message)or (p2 in message)or(p3 in message)or(p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")   

# Question: Check username length.
username = input("Enter username: ")

if (len(username) < 10):
    print("Your username contain less than 10 characters")

else:
    print("All is well")


# Question: Check whether a name exists in a list.
names = ["Sachin", "Rohan", "Bhushan", "Shubham"]

name = input("Enter name: ")

if name in names:
    print("Name is present")
else:
    print("Name is not present")


# Question: Calculate grade based on marks
marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "EX"
elif(marks<90 and marks>=80):
    grade = "A"    
elif(marks<80 and marks>=70):
    grade = "B"    
elif(marks<70 and marks>=60):
    grade = "C"    
elif(marks<60 and marks>=50):
    grade = "D"    
elif(marks<50):
    grade = "F"    

print("Youor grade is: ", grade)


# Question: Check if a post mentions bhushan.
post = input("Enter post: ")

if ("Bhushan".lower() in post.lower()):
    print("This post is talking about bhushan")
else:
    print("This post is not talking about bhushan")
