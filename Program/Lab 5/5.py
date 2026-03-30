import re
import math


text = input("enter a paragraph: ")
vowel_words = re.findall(r"\b[aeiouAEIOU]\w*\b", text)
vowels_total = len(re.findall(r"[aeiouAEIOU]", text))
lengths = list(map(lambda w: len(w), vowel_words))
avg_len = (sum(lengths) / len(lengths)) if lengths else 0
avg_len_rounded = round(avg_len, 2)
print("words starting with a vowel:", vowel_words)
print("total vowels in paragraph:", vowels_total)
print("average length of vowelstarting words (rounded to 2 decimals):", avg_len_rounded)



input(".")