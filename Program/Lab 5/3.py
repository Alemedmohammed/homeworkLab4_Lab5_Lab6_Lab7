import math
inp = input("enter a list of numbers separated by commas: ")
try:
    nums = [float(s.strip()) for s in inp.split(',') if s.strip() != ""]
    squares = list(map(lambda x: x**2, nums))
    max_square = max(squares) if squares else 0
    sum_squares = sum(squares)
    sqrt_sum = math.sqrt(sum_squares)
    print("numbers:", nums)
    print("squares:", squares)
    print("maximum square:", max_square)
    print("square root of sum of squares:", sqrt_sum)
except ValueError:
    print("please enter valid numeric values separated by commas")
input("============================== ")