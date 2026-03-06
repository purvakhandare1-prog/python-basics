# Temperature Converter: Ask the user for a temperature in Celsius. Ask if they want to convert it to Fahrenheit or Kelvin, then show the result.
temperature = float(input("Enter temperature in Celsius: "))
user_choice = input("What do you want to convert it into? (Fahrenheit or Kelvin): ").lower()


if user_choice == "fahrenheit":
    result = (temperature * 1.8) + 32
    print(f"{temperature}°C is {result:.2f}°F")


elif user_choice == "kelvin":
    result = temperature + 273.15
    print(f"{temperature}°C is {result:.2f}K")


else:
    print("Sorry, I only understand 'Fahrenheit' or 'Kelvin'.")