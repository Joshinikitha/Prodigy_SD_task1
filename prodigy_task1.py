# Temperature Conversion Program

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Function to convert temperature based on the input unit
def convert_temperature(value, unit):
    if unit == 'C':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        return f"Temperature in Fahrenheit: {f:.2f}°F, Temperature in Kelvin: {k:.2f}K"
    elif unit == 'F':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        return f"Temperature in Celsius: {c:.2f}°C, Temperature in Kelvin: {k:.2f}K"
    elif unit == 'K':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        return f"Temperature in Celsius: {c:.2f}°C, Temperature in Fahrenheit: {f:.2f}°F"
    else:
        return "Invalid unit. Please enter 'C', 'F', or 'K'."

# Main program
try:
    temp_value = float(input("Enter the temperature value: "))
    temp_unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    result = convert_temperature(temp_value, temp_unit)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number for temperature.")