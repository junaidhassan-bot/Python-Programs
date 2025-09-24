#Practice Questions and answers
#Strings & Operations
#1.	Create a variable name with your name, and print it.

#name="Junaid"
#print(name)

#2.	Concatenate "Hello, " with your name and store it in a new variable. Print it.
#name="Junaid"
#greeting="Hello"
#concat=greeting+ " "+name
#print(concat)

#3.	Find the length of the string "Data Science
#field="Data Science"
#print(len(field))

#4.	Slice the word "Python" to get:
#o	First 3 letters
#o	Last 2 letters

#word="Python"
#print(word[0:3])
#print(word[-2:])

#5.	Use negative indexing to print the last character of the string "Welcome".
#str="Welcome"
#print(str[-1])

#6.	Get every second character of the string "abcdefg" using slicing.
#str="abcdefg"
#print(str[0::2])

#7.	Convert "hello world" to uppercase
#str="hello world"
#print(str.upper())

#8.	Remove leading and trailing spaces from " data science " using a string function.
#str=" data Science "
#print(str.strip())

#9.	Replace the word "bad" with "good" in this string: "This is a bad example".
#str="This is a bad example"
#print(str.replace("bad","Good"))

#10.	Count how many times the letter 'a' appears in "banana".
#str="banana"
#print(str.count("a"))

#___________________________________________________________________________________________________________

#Conditional Statements
#11.	Write a program to check if a number is positive, negative, or zero using if, elif, else.
#number=int(input("Enter a number"))
#if(number>0):
    #print("Number is positive :")
#elif(number<0):
    #print("Number is Negative :")
#else:
    #print("Number is Zero")

#12.	Ask the user to enter a name. If the name is "junaid", print "Welcome!", otherwise print "Access Denied".
#name=input("Enter the name")
#if(name.strip().lower()=="junaid"):
    #print("Welcome")
#else:
    #print("Access Denied")

#13.	Take a string from the user. If its length is greater than 5, print "Long word", otherwise "Short word".
#str=input("Enter the String : ")
#if len(str)>5:
    #print("Long Word")
#else:
    #print("Short Word")

#14.	Write a program to check if the first letter of a string is uppercase.
#word=input("Enter a String :")
#if word[0] == word[0].upper():
    #print("First Letter is Upper")
#else:
    #print("No first letter of the string is not upper")

#15.	Ask the user for a password. If the password is "admin123", print "Login successful", else "Incorrect password".
#password=input("Enter the password : ")
#if password == "admin123":
    #print("Login Sucessfull :")
#else:
    #print("Incorrect Password : ")

#______________________________________________________________________________________________________________________

#Nested Conditions
#16.	Write a program that checks:
#•	If a number is even and positive, print "Even and Positive"
#•	Else if it’s odd and positive, print "Odd and Positive"
#•	Else print "Other case"

# num=int(input("Enter the number : "))
# if num%2==0 and num>0:
#     print("Number is Even and Positive")
# elif num%2!=0 and num>0:
#     print("Number is odd and Positive")
# else:
#     print("Other case")

#17.Ask the user to enter a username and password. If username is "admin" and password is "1234", print "Access granted". Else, print "Wrong credentials".
# user_name=input("Enter the user name :")
# Pass_word=input("Enter the password :")
# if user_name=="admin":
#     if Pass_word=="1234":
#         print("Access granted :")
#     else:
#         print("Wrong Crdentials")
# else:
#     print("Wrong Credentials :")

#18.	If a string has more than 3 characters and starts with 'a', print "Valid", else "Invalid".
# word=input("Enter the string : ")
# if len(word)>3 and word[0] == 'a':
#     print("Valid :")
# else:
#     print("Inavlid")

#19.	Take a word input from the user. If it ends with 'ing', print "Present participle". Else, print "Not participle".

# word=input("Enter word :")
# if word.endswith("ing"):
#     print("Present participle :")
# else:
#     print("Not participle :")

#20.	Check if a string is empty or not. If empty, print "String is empty", else "String has content".
# str=input("Enter the string : ")
# if str=="":
#     print("String is empty :")
# else:
#     print("String has content")