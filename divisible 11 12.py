print("Select two numbers, and this will find the any, if present, numbers divisable by both 11 and 12 between the numbers.")
while True:
    try:
        number_one = int(input("What is the starting number?"))
        number_two = int(input("What is the end of the range?"))
        break
    except ValueError:
        print("Both must be numbers!")
numbers_divisible = 0
for i in range(number_one,number_two):
    if i%11 == 0 and i%12 == 0:
        print(i, "is divisible by both 11 and 12!")
        numbers_divisible = numbers_divisible + 1
    else:
        continue
