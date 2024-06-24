def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def main():
    print("Welcome to the Temperature Conversion Program!\n")
    
    while True:
        try:
            temp = float(input("Enter temperature value: "))
            original_unit = input("Enter original unit (Celsius, Fahrenheit, or Kelvin): ").strip().lower()
            
            if original_unit == 'celsius':
                celsius = temp
                fahrenheit = celsius_to_fahrenheit(celsius)
                kelvin = celsius_to_kelvin(celsius)
                
            elif original_unit == 'fahrenheit':
                fahrenheit = temp
                celsius = fahrenheit_to_celsius(fahrenheit)
                kelvin = fahrenheit_to_kelvin(fahrenheit)
                
            elif original_unit == 'kelvin':
                kelvin = temp
                celsius = kelvin_to_celsius(kelvin)
                fahrenheit = kelvin_to_fahrenheit(kelvin)
                
            else:
                print("Invalid unit input. Please enter Celsius, Fahrenheit, or Kelvin.\n")
                continue
            
            print(f"\n{temp} {original_unit.capitalize()} is equal to:")
            print(f"{fahrenheit:.2f} Fahrenheit")
            print(f"{kelvin:.2f} Kelvin\n")
            
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.\n")
        except Exception as e:
            print(f"An error occurred: {str(e)}\n")
        
        choice = input("Would you like to convert another temperature? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nThank you for using the Temperature Conversion Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
