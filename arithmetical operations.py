# program to perform basic arithmetic operations

# function to add two numbers
def add(a, b):
    return a + b

# function to subtract two numbers
def subtract(a, b):
    return a - b

# function to multiply two numbers
def multiply(a, b):
    return a * b

# function to divide two numbers
def divide(a, b):
    return a / b

# take user input
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1/2/3/4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
