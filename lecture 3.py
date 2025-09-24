#1.	Create a list with 3 numbers and print it.

#numbers=[1,2,3]
#print(numbers)

#2.	Create a list with 4 strings (like "apple", "banana") and print the 2nd item
#fruits=["apple","banana","peech","strawberry"]
#print(fruits[1])

#3.	Create a list with any 5 items and print the first item.

#car=["Bmw","Nissan","Hounda"]
#print(car[0])

#4.	Create a list with any 5 items and print the last item.
#house=["House1","House2","House3","House4","House5"]
#print(house[-1])

#5.	Create a list of 5 numbers and change the first item to 99
#numbers=[1,2,3,4,5]
#print(numbers)
#print("After changing the list of first number : ")
#numbers.insert(0,99)
#print(numbers)

#6.	Create a list of 4 names and change the last name to "Junaid".
#names=["Ali","Hassan","Usman","Sam"]
#print(names)
#print("After changing the last name to junaid : ")
#names[3]="Junaid"
#print(names)

#7.	Create a list of 3 colors and add one more color at the end using +.
#colors=["Red","Black","White"]
#print(colors)
#print("After adding the next color : ")
#colors=colors+["Orange"]
#print(colors)

#8.	Create two lists and join them into one big list using +.
#lis1=[1,2,3,4,5]
#list2=[6,7,8,9,10]
#print("After joining these two lists two one big list")
#join=lis1+list2
#print(join)

#9.	Create a list of 5 numbers and print the 3rd and 4th items.
#numbers=[1,2,3,4,5]
#print(numbers[2:4])

#10.	Create a list of 3 numbers and replace the middle number with 100
#number=[1,2,3]
#print(number)
#number[1]=100
#print("After adding the number to the middle number is : ",number)

#write a program to ask the user to enter three names of thir fav movies and store them in list.
name1=input("Enter the name of fave movie 1")
name2=input("Enter the name of fave movie 2")
name3=input("Enter the name of fave movie 3")
list=[name1+name2+name3]
print(list)
