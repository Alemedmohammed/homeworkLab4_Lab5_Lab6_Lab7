import re
import math
password = input("enter a password: ")
has_upper = re.search(r"[A-Z]", password) is not None
has_lower = re.search(r"[a-z]", password) is not None
has_digit = re.search(r"\d", password) is not None
if has_upper and has_lower and has_digit:
    print("password is strong")
else:
    print("password is weak")
grades_input = input("enter 5 grades separated by spaces: ")
try:
    grades = [float(x) for x in grades_input.split() if x.strip() != ""]
    if len(grades) != 5:
        print("you must enter exactly 5 grades")
    else:
        avg_func = lambda lst: sum(lst) / len(lst)
        avg = avg_func(grades)
        rounded_avg = math.ceil(avg)
        print("rounded-up average:", rounded_avg)
except ValueError:
    print("please enter valid numeric grades")
input(". ")