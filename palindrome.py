#Mark Wspanialy
#ICS4U0
#21/09/2018
#Palindrome checker
#gets the string to test
string_to_test = input("What word or phrase would you like to test as a palindrome?")
#definition to check the palindrome
def palindrome_test(check_string):
    #Takes out spaces from the palindrome, only testing for letters
    check_string.replace(" ","")
    #makes a second string that is the first string reversed
    reverse_to_check = check_string[::-1]
    #Checks if the string is equal to its reversed self
    if reverse_to_check == check_string:
        #If it is, make it known
        check_string = "palindrome"
        #return the value
        return check_string
    else:
        #if not, don't call it one
        check_string = "incorrect"
        #return the value
        return check_string
#puts the string through the tester, and gives it a value of palindrome or incorrect
check_string = palindrome_test(string_to_test)
#checks if it is listed as a palindrome
if check_string == "palindrome":
    #if it is, print so
    print("This is a palindrome!")
else:
    #if it isn't, prints this.
    print("This is not a palindrome.")
