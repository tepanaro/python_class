text = "Hello, welcome to Python!"

print("Original text:", text)
print("Uppercase text:", text.upper())

# upper() returns a new uppercase string.
# It does not change the original string.
print("Original text is still:", text)

user_text = input("Type something: ")
print("In uppercase:", user_text.upper())
