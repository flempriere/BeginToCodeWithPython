# Exercise 7.2.4: Fahrenheit to Celcius
#
# Version of Fahrenheit to Celcius that uses BTCInput

import BTCInput

temperature_fahrenheit = BTCInput.read_float("Enter a temperature in Fahrenheit: ")
temperature_centrigrade = (temperature_fahrenheit - 32) / 1.8
print("The temperature is", temperature_centrigrade, "degrees Celcius")
