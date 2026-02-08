# Exercise 4.2: Fahrenheit to Celsius
#
# Converts Fahrenheit to Celsius

temperature_fahrenheit = float(
    input("Enter a temperature in Fahrenheit: ")
)  # read in string, convert to float
temperature_centigrade = (temperature_fahrenheit - 32) / 1.8
print("The temperature is", temperature_centigrade, "degrees Celsius")
