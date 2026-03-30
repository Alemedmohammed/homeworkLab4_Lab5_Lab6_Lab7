nums = []
i = 0
while i < 5:
    try:
        s = input(f"enter number _{i+1}: ")
        n = float(s)
    except ValueError:
        print("invalid input, please enter a numeric value")
        continue 
    except (EOFError, KeyboardInterrupt):
        print("\ninput cancelled")
        break
    else:
        nums.append(n)
        i += 1
if len(nums) == 0:
    print("no valid numbers were entered")
else:
    total = sum(nums)
    avg = total / len(nums)
    mx = max(nums)
    mn = min(nums)
    print(f"sum: {total}")
    print(f"average: {avg}")
    print(f"maximum: {mx}")
    print(f"minimum: {mn}")
input("")