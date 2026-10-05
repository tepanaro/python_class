palabra = input("Write a word: ")
letras = list(palabra)
letras_reversed = list(reversed(letras))
print(letras_reversed)
print("".join(letras_reversed))

while letras_reversed != letras:
    print("Keep trying!")
    letras = input("Write another word ")
    letras_reversed = "".join(list(reversed(letras)))

print("This is a palindrome word!")