secret = 7  
attempts = 0
while True:
    try:
        guess = int(input("guess the number (between 1 and 20): "))
    except ValueError:
        print("please enter an integer")
        continue
    if guess < 1 or guess > 20:
        print("guess out of range, try again")
        continue  
    attempts += 1 
    if guess == secret:
        print(f"congratulations You guessed correctly in {attempts} attempts")
        break
    elif guess < secret:
        print("try higher")
    else:
        print("try lower")
input("_______________________")