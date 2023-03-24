def add(x, y):
    print("Addition operation1")
    return x + y

def subtract(x, y):
    print("subtraction operation243")
    return x - y

def multiply(x, y):
    print("extra activites")
    return x * y

def divide(x, y):
    if y == 0:
        print("divide error")
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    print("getting power")
    return x ** y

def modulus(x, y):
    return x % y
