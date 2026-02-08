# Example 9.9 Alarm Access Control
#
# Demonstrates the use of a dictionary as a lookup table to translate
# keys into associated values

import BTCInput

access_control = {1234: "complete", 1111: "limited", 4342: "limited"}

access_code = BTCInput.read_int("Enter your access code: ")
if access_code in access_control:
    print("You have", access_control[access_code], "access")
else:
    print("You are not allowed access")
