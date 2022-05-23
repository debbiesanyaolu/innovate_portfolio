# import random
# # print is how we display information in a terminal
# print("this is my current file")

# # strings are for representing character
# print ("Hello my name is Klong")
# print("1234")

# #This is an integer - a whole number
# print(1234)

# #this is a floating point - anything with a decimal
# print(1234.5)

# #booleans - True and False
# print(True)
# print(False)

# #none - a blank, or a null type
# print(None)

# #len - provides how many characters in string
# print(len("hello  "))

# #index position - starts its count at 0
# print("hello"[-1])

# #.notation is a way of accessing methods
# print("hello".upper())

# print(random.random())
# print (random.uniform(1,10))
# print(random.randint(1,10))

# import random
# from random import random, randint, uniform

# print(uniform())

# my_name = "Debbie"
# my_age = 26

# print(my_name)

# print("Hello my name is",my_name)
# print("Hello my name is " + my_name)
# print("Hello my name is {} and I am {} years old".format(my_name,my_age))
# print(f"Helo my name is {my_name} and I am {my_age} years old")

# #Arithmetic operators
# print(1+2) #Addition
# print(2-1) #Subtraction
# print(2*3) #Multiplication
# print(3**3) #To the power of
# print(15/3) #Division - tends to give decimal answers even if whole
# print(15%3) #Modules (remainder after division )

# balance = 100
# amount = 50

# print(balance-amount)
# balance = balance - amount #This is making the balance equal what balance was before minus the amount
# # print(balance)

# # input("What is your name?   >  ") #Input allows us to ask the user a question and wait for their response as their may be certain types of information we are unable to store as there could be many answers. I.E. Names for characters in a game

# character_name = input("What is your name?   >  ")

# print(f"Welcome, {character_name}")

# ################IfElse##################

# music = "classical" #Variable - music Data - Classical (String)

# if music == "classical":
#     print("Oh no! It's classical music again.") #So if variable music is classical, print this statement

# elif music == "no music": 
#     print("Aah, peace and quiet!") #Or if it is no music then print this

# else:
#     print("Nice and noisy.") #If anything else is the variable then print this

# # = is an assingment operator, it says something is something
# # == is a comparison operator, is something something?
# # != it is not equal to

# ##example###
# print(10%2==0) #Comparison operators give us boolean type of data (true/false)  

# num1=10
# num2=20

# if num1 > num2:
#     print("number 1 is the bigger number")
# elif num1 < num2:
#     print("number 2 is the bigger number")
# else:
#     print ("number 1 and number 2 are the same")

# place = "Manchester"
# weather = "Rainy"

# if place=="Manchester" and weather=="Rainy":
#     print("Of course")
# elif place=="Manchester" and weather=="Sunny":
#     print("Check again")
# else:
#     print("It's bloody cold")


# day="Mondayy"

# if day=="Saturday" or day=="Sunday":
#     print("Yay it's a day off")
# else:
#     print("Time to go to Code Nation")

# day="Monday"
# bank_holiday=True

# if day=="Saturday" or day=="Sunday" or bank_holiday==True:
#     print("Yay it's a day off")
# else:
#     print("Time to go to Code Nation")

# ################Functions##################

# def light_switch():
#     print("Who turned out the lights?")
# light_switch()

# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawaing {amount} from account {accnum}")

# cash_withdrawal(100, 12345678)
# cash_withdrawal(200, 23456789)
# cash_withdrawal(300, 34567890)
# cash_withdrawal(400, 45678901)

# ################Lists##################

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# print(cake_ingred)

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# print(cake_ingred[-1])

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# cake_ingred[-1]="Vanilla extract"        #This will change the last item in the list
# print(cake_ingred)

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# cake_ingred[2]="Nutmeg"                   #This will change 3rd item in the list
# print(cake_ingred)

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# cake_ingred.append("Nutmeg")                 #This will add to the list but will only add 1 item

# print(cake_ingred)


# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# cake_ingred.pop()                               #Removes the last item on the list

# print(cake_ingred)

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# cake_ingred.pop(1)                                #Removes the 2nd item in the list
# print(cake_ingred)

# ################Loops##################

# # For Loops

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# for i in cake_ingred:                                #Output will be to list the items for as many as there are. i.e. the code will run and give the first item in the list, it will then run again and give the second item until it gets to the end. This means the loop will run 5 times are there are 5 items in the list.
#     print(i)

# cake_ingred = [
#     "Flour",
#     "butter",
#     "sugar",
#     "eggs",
#     "love"
# ]

# for i in cake_ingred:                               
#     print("Mmm delicous!")                      #Again "mmm delicious will be printed  as many times as there are items in the list"

# while loop

# num=0

# while num <10:
#     print("hello")                         # hello will then print forever as it is asking while num is less than 10 print hello. 0 is less than 10 and so hello will continue to print unless it is given the chance to be broken

# num=0

# while num <10:
#     num +=1
#     print("hello")                           # hello will then stop once it has gotten to 10th run as it is asking to run up until num is less than 10.