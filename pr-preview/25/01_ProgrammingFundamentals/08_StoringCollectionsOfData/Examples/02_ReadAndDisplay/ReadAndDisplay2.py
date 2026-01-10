# Example 8.2.2 Read and Display 2
#
# Improved version of Read and Display which allows the user to specify
# the number of stands

import BTCInput

# create an empty list to populate
sales = []

number_of_stands = BTCInput.read_int("Enter the number of stands: ")
for count in range(1, number_of_stands + 1):
    prompt = "Enter the sales for stand " + str(count) + ": "
    sales.append(BTCInput.read_int(prompt))

print(sales)
