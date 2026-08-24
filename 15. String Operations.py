text = "Python Programming"

# Slice words
word1 = text[:6]
word2 = text[7:]
print("Word 1:", word1)
print("Word 2:", word2)

# Insert 'java' if missing
if "java" not in text.lower():
    new_text = word1 + " java " + word2
else:
    new_text = text

print("Modified text:", new_text)
print("Length of new text:", len(new_text))
print("Word count:", len(new_text.split()))
print("Capitalized:", new_text.title())
print("Without spaces:", new_text.replace(" ", ""))

# Frequency matching exact case
for ch in ["A", "P", "R", "M"]:
    print(f"Count of '{ch}':", new_text.count(ch))