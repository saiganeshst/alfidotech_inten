def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("---------------------")
    
    print("Select the input unit:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")
    
    choice = input("Enter choice (1/2/3): ")
    
    try:
        temp = float(input("Enter the temperature value: "))
        
        if choice == "1":  # Celsius
            print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
            print(f"{temp}°C = {celsius_to_kelvin(temp)} K")
        
        elif choice == "2":  # Fahrenheit
            print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
            print(f"{temp}°F = {fahrenheit_to_kelvin(temp)} K")
        
        elif choice == "3":  # Kelvin
            if temp < 0:
                print("Kelvin cannot be negative!")
            else:
                print(f"{temp} K = {kelvin_to_celsius(temp)}°C")
                print(f"{temp} K = {kelvin_to_fahrenheit(temp)}°F")
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    except ValueError:
        print("Invalid temperature input. Please enter a number.")

if __name__ == "__main__":
    main()
