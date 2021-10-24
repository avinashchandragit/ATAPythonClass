#Loop through the items in the fruits list.fruits = ["apple", "banana", "cherry"]
Fruits=["apple","banana","cherry"]
for i in range(0,len(Fruits)):
    print(Fruits[i])

#Print First 5 natural numbers using while/for loop
for i in range(1,6):
    print(i) 

i=1
while i<6:
    print(i)
    i+=1

#Using for loop calculate the sum of all numbers from 1 to 10
total=0
for i in range(1,11):
    total=total+i
print(total)

#Write a program to print a multiplication table of 3 from 1 to 10 
x=input("what multiplication table is required: ")
y=input("Until what number you want the table: ")
x=int(x)
y=int(y)

for i in range(1,y+1,1):
    print(x," X ",i," = ",x*i)

#Write a program to display only those numbers which are divisible by five from a list
list5=[1,5,10,12,13,18,20,15,16]
print(len(list5))
i=0
while i<len(list5):
    if list5[i] % 5 == 0:
        print(list5[i])
    i+=1

#Given a list, replace the smallest value with the largest one.

ListA = [4,5,6,2,9]
for i in range(0,len(ListA)):
    if ListA[i]==min(ListA):
        ListA[i]=max(ListA)
print(ListA)