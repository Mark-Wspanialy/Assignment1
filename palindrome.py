string_to_test = input("What word or phrase would you like to test as a palindrome?")
string_to_test.replace(" ","")
reversed_string = string_to_test[::-1]
if reversed_string == string_to_test:
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")
