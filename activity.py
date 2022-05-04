greeting = "Welcome to Code Nation"
greeting2 = "Welcome to Code Nations"
print(greeting)

length = len(greeting)



def evenodd(st,len):
    even_odd = length%2
    if even_odd == 0:
        # print(f"{st} is length {len} is even")
        print("{} is length {} is even".format(st, len))
    else:
        # print(f"{greeting} is length {length} is odd")
        print("{} is length {} is odd".format(st, len))


evenodd(greeting,length)
length = len(greeting2)

evenodd(greeting2,length)
# length = len(greeting)%2

# print (length)

# if length == 0:
