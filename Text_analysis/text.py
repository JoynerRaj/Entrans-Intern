import string

file = open("sample.txt", "r")
text = file.read()

characters = len(text)

sentences = text.count(".")

text = text.lower()

for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()

total_words = len(words)

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Total Characters:", characters)

print("\nTop 3 Frequent Words:")

for word, count in sorted_words[:3]:
    print(word, "->", count)