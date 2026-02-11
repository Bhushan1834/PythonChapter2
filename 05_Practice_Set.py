#1 write a program to store 7 fruits in a list entered by thr user 
fruits =[]
f1 = input("Enter Fruit Name: ")
fruits.append(f1)
f2 = input("Enter Fruit Name: ")
fruits.append(f2)
f3 = input("Enter Fruit Name: ")
fruits.append(f3)
f4 = input("Enter Fruit Name: ")
fruits.append(f4)
f5 = input("Enter Fruit Name: ")
fruits.append(f5)
f6 = input("Enter Fruit Name: ")
fruits.append(f6)
f7 = input("Enter Fruit Name: ")
fruits.append(f7)
print(fruits)

#2 Write a program to accept of 6 students and disply them in a sorted manager
Marks =[]
f1 = int(input("Enter Marks here: "))
Marks.append(f1)
f2 = int(input("Enter Marks here: "))
Marks.append(f2)
f3 = int(input("Enter Marks here: "))
Marks.append(f3)
f4 = int(input("Enter Marks here: "))
Marks.append(f4)
f5 = int(input("Enter Marks here: "))
Marks.append(f5)
f6 = int(input("Enter Marks here: "))
Marks.append(f6)
Marks.sort()
print(Marks)

#3 Check tuple a type cannot be changed in python 
a = (54,54, "Bhushan")
a[2] = "Bhussh"

#4 Write a program to sum a list with 4 numbers 
b = (1,2,3,5)
print(sum(b))

#5 Write a program to count the number of zeros in the follwing tuple : a = (7,0,8,0,0,9)
a = (7,0,8,0,0,9)
n = a.count(0)
print(n)
