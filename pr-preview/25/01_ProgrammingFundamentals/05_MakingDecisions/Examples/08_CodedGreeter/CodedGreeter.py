# Example 5.8: Coded Greeter
#
# Asks the user for a follow on code to confirm their ID
# before the program greets them

name = input("Enter your name: ")

if name.upper() == "ROB":
    code = input("Enter the codeword: ")
    if code == "secret":
        print("Hello, Oh great one")
    else:
        print("Begone. Imposter")
