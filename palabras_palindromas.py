palabra = input("Write a word: ")
letras = list(palabra)
letras_reversed = list(reversed(letras))
print(letras_reversed)
print("".join(letras_reversed))
if letras_reversed == letras:
    print("This is a palindrom word")
else:
    print("Keep trying!")