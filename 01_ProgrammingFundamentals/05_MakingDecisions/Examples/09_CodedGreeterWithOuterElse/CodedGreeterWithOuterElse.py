# Example 5.9: Coded Greeter with Outer Else
# Asks the user for a follow on code to confirm their ID
# before the program greets them
# Has an additional outer else clause for the case that the nested
# if does not run

name = input("Enter your name: ")

if name.upper() == "ROB":
    code = input("Enter the codeword: ")
    if code == "secret":
        print("Hello, Oh great one")
    else:
        print("Begone. Imposter")
else:
    print("You are not Rob. Shame.")
