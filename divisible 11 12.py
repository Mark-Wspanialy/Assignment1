#Mark Wspanialy
#ICS4U0
#21/09/2018
#Number checker (divisible by 11 and 12)
#gets the range of numbers to check
print("Select two numbers, and this will find the any, if present, numbers divisable by both 11 and 12 between the numbers.")
#Makes sure the user knows what they might be getting into with a large range
print("WARNING: too large of a range will result in a long run time (e.g. over 10000 difference between the numbers)")
#Starts a loop to collect the integers
while True:
    try:
        #Takes the numbers
        number_one = int(input("What is the starting number?"))
        number_two = int(input("What is the end of the range?"))
        break
    except ValueError:
        #If one is not a number, it will print this and ask again
        print("Both must be numbers!")
#Makes a value to see how many numbers in total were divisible by both 11 and 12
numbers_divisible = 0
#Starts checking
for i in range(number_one,number_two):
    #if it is divisible, print so
    if i>0:
        if i%11 == 0 and i%12 == 0:
            print(i, "is divisible by both 11 and 12!")
            numbers_divisible = numbers_divisible + 1
        else:
            #Ignore non-divisible numbers
            continue
    elif i<0:
        #If the number is negative divide by negative numbers
        if i%-11 == 0 and i%-12 == 0:
            print(i, "is divisible by both 11 and 12!")
            numbers_divisible = numbers_divisible + 1
        else:
            #Ignore non-divisible numbers
            continue
    #If the number is 0 its non divisible
    else:
        continue
#Prints Total Numbers
print(numbers_divisible, "number(s) were divisible by 11 and 12.")
