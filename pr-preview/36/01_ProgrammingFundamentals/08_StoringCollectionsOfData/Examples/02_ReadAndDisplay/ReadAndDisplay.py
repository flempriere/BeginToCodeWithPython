# Example 8.2.1 Read and Display
#
# Demonstrates using a loop to populate a list

import BTCInput

# create an empty list to populate
sales = []

for count in range(1, 11):
    prompt = "Enter the sales for stand " + str(count) + ": "
    sales.append(BTCInput.read_int(prompt))

print(sales)
