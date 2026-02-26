test_string = input("Enter a word").lower()
reverse=test_string[::-1]
if test_string==reverse:
    print("It is a palindrome")
else:
    print("not a palindrome")
