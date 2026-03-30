words = []
for i in range(5):
    w = input(f"enter word {i+1}: ")
    words.append(w)

t = tuple(words)
print("first word:", t[0])
print("last word:", t[-1])
print("total words:", len(t))

search = input("enter a word to check: ")
if search in t:
    print("word is in the tuple")
else:
    print("word is not in the tuple")