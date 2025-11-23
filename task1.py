# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main program
def main():
    print("Welcome to the Python Calculator!")
    
    # Display operation options
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take user input for the operation
    choice = input("\nEnter choice (1/2/3/4): ")
    
    # Take user input for numbers
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the operation
    if choice == '1':
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the program
if __name__ == "__main__":
    main()
