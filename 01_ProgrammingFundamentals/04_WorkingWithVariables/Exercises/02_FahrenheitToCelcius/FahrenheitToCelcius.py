# Exercise 4.2: Fahrenheit to Celcius
# Converts Fahrenheit to Celcius

temperature_fahrenheit = float(
    input("Enter a temperature in Fahrenheit: ")
)  # read in string, convert to float
temperature_centrigrade = (temperature_fahrenheit - 32) / 1.8
print("The temperature is", temperature_centrigrade, "degrees Celcius")
