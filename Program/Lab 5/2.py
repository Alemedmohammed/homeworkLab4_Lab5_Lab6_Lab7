import re
text = input("enter a text containing numbers: ")
numbers_str = re.findall(r"-?\d+", text)
numbers = [int(s) for s in numbers_str]
def sum_numbers(nums):
    return sum(nums)
double = lambda x: x * 2
total = sum_numbers(numbers)
print("found numbers:", numbers)
print(numbers,"_", total,"_",double(total))

input("++++++++++++++++++++++++++")