# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
# Returns an error message if division by zero is attempted
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Main calculator function to handle user interaction and perform operations
def calculator():
    # Dictionary to map user choices to operation names and their corresponding functions
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide)
    }
    
    # Infinite loop to keep the calculator running until the user decides to quit
    while True:
        # Display the available operations to the user
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("q. Quit")  # Option to quit the calculator
        
        # Prompt the user to select an operation or quit
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
        
        # If the user chooses to quit, exit the loop
        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        
        # If the user enters an invalid choice, prompt them again
        if choice not in operations:
            print("Invalid input. Please try again.")
            continue
        
        # Try to get two numbers from the user and perform the selected operation
        try:
            num1 = float(input("Enter first number: "))  # First number
            num2 = float(input("Enter second number: "))  # Second number
            
            # Perform the operation based on the user's choice
            result = operations[choice][1](num1, num2)
            print(f"Result: {result}")  # Display the result
        except ValueError:
            # Handle cases where the user enters invalid numbers
            print("Please enter valid numbers.")

# Entry point of the program
if __name__ == "__main__":
    calculator()