try:
    n = int(input("enter n: "))
except ValueError:
    print("elease enter a valid integer")
else:
    count = 0
    for num in range(1, n + 1):
        if num > 50:
            break  
        if num % 8 == 0:
            continue 
        if num % 4 == 0:
            count += 1
    print("count of numbers from 1 to", n, "divisible by 4 (excluding multiples of 8, stop if >50):", count)
    input("_________________________")