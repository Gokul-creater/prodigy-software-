# TASK 1
Certainly! Here's a Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales based on user input. It prompts the user to enter a temperature value followed by the unit (C, F, or K), and then it converts that temperature to the other two units and displays the results.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Conversion Program")
    print("Enter the temperature value followed by the unit (e.g., 25 C, 98.6 F, 300 K):")
    
    user_input = input("Input temperature: ")
    parts = user_input.split()
    
    if len(parts) != 2:
        print("Invalid input format. Please enter a temperature value followed by the unit.")
        return
    
    try:
        temperature = float(parts[0])
        unit = parts[1].upper()
        
        if unit == 'C':
            celsius = temperature
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        elif unit == 'F':
            fahrenheit = temperature
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)
        elif unit == 'K':
            kelvin = temperature
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)
        else:
            print("Invalid unit. Please use C, F, or K.")
            return
        
        print(f"{temperature} {unit} is equal to:")
        print(f"{fahrenheit:.2f} F")
        print(f"{celsius:.2f} C")
        print(f"{kelvin:.2f} K")
    
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Conversion Functions**: 
   - `celsius_to_fahrenheit`, `celsius_to_kelvin`: Convert Celsius to Fahrenheit and Kelvin respectively.
   - `fahrenheit_to_celsius`, `fahrenheit_to_kelvin`: Convert Fahrenheit to Celsius and Kelvin respectively.
   - `kelvin_to_celsius`, `kelvin_to_fahrenheit`: Convert Kelvin to Celsius and Fahrenheit respectively.

2. **Main Function (`main()`)**:
   - Prompts the user to input a temperature value followed by the unit (C, F, or K).
   - Validates the input format and splits it into temperature value and unit.
   - Converts the input temperature to the other two units based on the original unit entered by the user.
   - Prints the converted temperatures formatted to two decimal places.

3. **Usage**:
   - Run the script.
   - Input a temperature value followed by the unit (e.g., `25 C`, `98.6 F`, `300 K`).
   - The program will display the converted temperatures in Fahrenheit, Celsius, and Kelvin.

This program handles basic temperature conversions and provides clear output to the user based on their input. You can extend or modify it further based on additional requirements or specific use cases you may have.
