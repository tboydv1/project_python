#Conversion Program

def celcius_to_fahrenheit(celcius_float):
    """Convert Celsius to Fahrenheit."""
    return celcius_float * 1.8 + 32

# main part of the program
print("Convert Celcius to Fahrenheit.")
celsius_float = float(input("Enter a Celcius temp: "));
# call the conversion function
fahrenheit_float = celcius_to_fahrenheit(celsius_float)

print(celsius_float," convert to ", fahrenheit_float, "Fahrenheit")
