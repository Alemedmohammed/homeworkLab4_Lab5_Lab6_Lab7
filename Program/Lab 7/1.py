try:
    a = float(input("enter the first number: "))
    b = float(input("enter the second number: "))
    result = a / b
except ZeroDivisionError:
    print("error: division by zero is not allowed")
except ValueError:
    print("error: non-numeric input")
else:
    print("division result:", result)


input("________________________")