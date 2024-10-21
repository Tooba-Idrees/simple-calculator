import streamlit as st

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Create the Streamlit application
def main():
    st.title("Simple Calculator")

    # User inputs
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])
    
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
            st.success(f"The result is: {result}")
        elif operation == "Subtract":
            result = subtract(num1, num2)
            st.success(f"The result is: {result}")
        elif operation == "Multiply":
            result = multiply(num1, num2)
            st.success(f"The result is: {result}")
        elif operation == "Divide":
            result = divide(num1, num2)
            st.success(f"The result is: {result}")

# Run the app
if __name__ == "__main__":
    main()
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
                
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

# Run the calculator
calculator()
