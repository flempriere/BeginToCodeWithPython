# Exercise 7.2.4: Fahrenheit to Celsius
#
# Version of Fahrenheit to Celsius that uses BTCInput

import BTCInput

temperature_fahrenheit = BTCInput.read_float("Enter a temperature in Fahrenheit: ")
temperature_centigrade = (temperature_fahrenheit - 32) / 1.8
print("The temperature is", temperature_centigrade, "degrees Celsius")
