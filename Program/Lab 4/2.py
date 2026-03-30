try:
    n = int(input("enter a number to print its multiplication table: "))
except ValueError:
    print("please enter a valid integer")
else:
    for i in range(1, 13):
        product = n * i
        if product % 3 == 0:
            continue  
        if product > 50:
            break  
        print(f"{n} x {i} = {product}")

input("______________________")