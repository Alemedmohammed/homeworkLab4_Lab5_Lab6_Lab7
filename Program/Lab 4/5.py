for i in range(1, 6):
    for j in range(1, i + 1):
        if i * j > 6:
            break 
        if j == 3:
            continue 
        print(j, end=' ')
    print()

input("_________________________")
