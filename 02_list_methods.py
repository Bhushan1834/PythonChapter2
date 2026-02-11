friends =["apple","56","92.5","akash","false"]
print(friends[2])
friends.append("Bhushan")
print(friends)

#List Method 
l1 = [5,6,1,2,2,0,3,9,5,15,21]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(5,887)# Insert 887 such that its index in the list is 5 
print(l1)

value = l1.pop(5)
print(value)
print(l1)


l1.remove(21)
print(l1)

l1.clear() # Clear is used for clearing all list 
print(l1)

# l1.count(5) #Counts how ma nytimes an element appears in the list.
# print(l1)
l1 = [5,6,1,2,2,0,3,9,5,15,21]
print(l1.count(5)) 

l2 = [1, 2, 3]
l3 = l2.copy()

