# Example 8.3 Read and Display Loop
#
# Uses a for loop to provide custom list printing

import BTCInput

sales = []

for count in range(1, 11):
    prompt = "Enter the sales for stand " + str(count) + ": "
    sales.append(BTCInput.read_int(prompt))

# print a heading
print("Sales Figures")
count = 1
for sales_value in sales:
    print("Sales for stand", count, "are", sales_value)
    count = count + 1
