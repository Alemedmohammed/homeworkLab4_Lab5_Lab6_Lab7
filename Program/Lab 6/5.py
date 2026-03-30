names = []
for i in range(5):
    name = input(f"enter name {i+1}: ")
    names.append(name)

names_tuple = tuple(names)
print("tuple:", names_tuple)

lengths_dict = {name: len(name) for name in names}
unique_lengths = set(lengths_dict.values())

print("dictionary (name: length):", lengths_dict)
print("unique name lengths set:", unique_lengths)
input("")