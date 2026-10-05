print("How the len() function works with strings")
print("-----------------------------------------")

# len() counts every character between the quotation marks.
# Letters, numbers, spaces, and punctuation each count as one character.
examples = ["Hello", "Hello world!", " ", ""]

for text in examples:
    print("The string", repr(text), "has", len(text), "character(s).")

print()
user_text = input("Type a word or sentence: ")
print("You typed", len(user_text), "character(s).")

# Example: "Hi there!" has 9 characters:
# 2 letters + 1 space + 5 letters + 1 exclamation mark.
