a_input = input("enter the first list of numbers separated by spaces: ")
b_input = input("enter the second list of numbers separated by spaces: ")
set_a = set(a_input.split())
set_b = set(b_input.split())
print("union:", set_a.union(set_b))
print("intersection:", set_a.intersection(set_b))
print("difference A - B:", set_a.difference(set_b))


input("")