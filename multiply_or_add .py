def multiply_or_add(a, b):
    """Multiplies two numbers if their product is less than 1000, otherwise adds them."""
    mul = a * b
    if mul < 1000:
        return mul
    else:
        return a + b

# Taking input from user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calling the function and printing the result
result = multiply_or_add(a, b)
print("The result is:", result)

