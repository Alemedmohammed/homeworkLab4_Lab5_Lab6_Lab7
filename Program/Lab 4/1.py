total = 0
count = 0
while count < 10:
    try:
        x = float(input(f"enter number {count+1}: "))
    except ValueError:
        print("nvalid try again")
        continue

    count += 1  

    if x < 0:
        continue 
    if x == 0:
        break  

    if x.is_integer() and int(x) % 2 == 0:
        total += int(x)

print("final sum of positive even integers:", total)
input()