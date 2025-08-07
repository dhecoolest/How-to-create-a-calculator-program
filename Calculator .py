import math
def add(*args):
    return sum(args)

def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    if not args:
        return "No numbers provided."
    result = args[0]
    try:
        for num in args[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
def power(base, exponent):
    return math.pow(base, exponent)

def square_root(num):
    if num < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(num)
def calculator():
    print("Welcome to the Variadic Calculator!")
    print("Operations available:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == '0':
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            nums = input("Enter numbers separated by spaces: ")
            args = list(map(float, nums.split()))
            
            if choice == '1':
                print("Result:", add(*args))
            elif choice == '2':
                print("Result:", subtract(*args))
            elif choice == '3':
                print("Result:", multiply(*args))
            elif choice == '4':
                print("Result:", divide(*args))
        
        elif choice == '5':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", power(base, exponent))
        
        elif choice == '6':
            num = float(input("Enter a number: "))
            print("Result:", square_root(num))
        
        else:
            print("Invalid choice. Please try again.")
calculator()
