##Create variable that holds the text "Welcome to Code Nation".

greeting = "Welcome to Code Nation"

##Find the length of the string and save this to a new variable.

greeting_length=len(greeting)

print (len(greeting))

##Create a function that checks if the string length is even.
##If string length equals even, print the string, the length and an appropriate message in one sentence.

def phrase_checker():
    if greeting_length%2 ==0:
        print(f"The length of the string \"{greeting}\" is {greeting_length} and it is even")
    else:
        print(f"The length of the string \"{greeting}\" is {greeting_length} and it is odd") 

phrase_checker()