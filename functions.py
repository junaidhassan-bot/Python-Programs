# Program 1 student's numerical score

while True:
    score=int(input("Enter the student's score (0-100): "))

    if score==-1:
        print("Exiting the program : ")
        break
    if score<0 or score >100:
        print("Invalid Input! Please Enter the a score between 0 and 100 :")
        continue
    if score>=90:
        print("Garade: A")
    elif score >=80:
        print("Grade: B")
    elif score>=70:
        print("Grade: C")
    elif score>=60:
        print("Grade: D")
    else:
        print("Grade: F")


#________________________________________________________________________

#Program 2 Rock, Paper, Scissors Game

import random
options=["Rock","Paper","Scissors"]
computer=random.choice(options)
print("Computer chose : ",computer)

user=input("Enter your choice (Rock,Paper, or Scissors): ").lower()
print("You Chose : ",user)


if user==computer:
    print("its tie : ")
elif (user=="Rock" and computer =="Scissors") or\
     (user=="Scissors" and computer =="Paper")or\
     (user=="Paper" and computer =="Rock"):
    print("You Win")
elif user in ["Rock","Paper","Scissors"]:
    print("You Lose!:")

else:
    print("Invalid input! Please chose Rock,Paper, or Scissors")

#________________________________________________________________________________

#Program 3 Simple ATM Simulator

# balance =1000
# while True:
#     print("ATM Menu : ")
#     print("1. Check Balance :")
#     print("2. Deposit : ")
#     print("3. Withdraw")
#     print("4. Exit")

#     choice=input("Enter your choice (1-4):")

#     if choice=="1":
#         print("Your Balance is :",balance)
    
#     elif choice =="2":
#         amount=int(input("Enter the amount to deposit :"))
#         if amount>0:
#             balance+=amount
#             print("Deposit successfull! New Balance is : ",balance)
#         else:
#             print("Invalid Deposit")
#     elif choice == "3":
#         amount = int(input("Enter amount to withdraw: "))
#         if amount > 0:
#             if amount <= balance:
#                 balance -= amount
#                 print("Withdrawal successful! New balance is:", balance)
#             else:
#                 print("Insufficient funds!")
#         else:
#             print("Invalid withdrawal amount.")
#     elif choice == "4":
#         print("Thank you for using the ATM. Goodbye!")
#         break

#--------------------------------------------------------------------------------------------




   

