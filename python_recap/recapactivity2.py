##Create a list that represents the alphabet:

alphabet = ["a","b", "c", "d","e", "f","g", "h","i", "j", "k", "l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]

##Create a for loop to iterate through this and print each letter in order

for letter in alphabet:
    print(letter)

##Now using input, allow the user to type a number and print the letter it represents in the alphabet.

##Remember how index works - and think about how to structure your code

def letter_num():
    user_num=int(input("Please enter a number between 1 and 26:   >"))
    user_num -=1
    if user_num >=0 and user_num <=26:
        print(alphabet[user_num])
    else:
        print("Invalid entry please try again")
        letter_num()

letter_num()