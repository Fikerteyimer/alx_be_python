# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_str = input("Enter the temperature to convert: ")
    try:
        temp_input = float(temp_str)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == "C":
        print(f"{temp_input}°C is {convert_to_fahrenheit(temp_input)}°F")
    elif unit == "F":
        print(f"{temp_input}°F is {convert_to_celsius(temp_input)}°C")
    else:
        print("Invalid unit. Please enter C or F.")

if __name__ == "__main__":
    main()
