string_to_test = input("What word or phrase would you like to test as a palindrome?")
def palindrome_test(check_string):
    check_string.replace(" ","")
    reverse_to_check = check_string[::-1]
    if reverse_to_check == check_string:
        check_string = "palindrome"
        return check_string
    else:
        check_string = "incorrect"
        return check_string
check_string = palindrome_test(string_to_test)
if check_string == "palindrome":
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")
