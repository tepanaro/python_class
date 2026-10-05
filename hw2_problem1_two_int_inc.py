i1 = int(input("Insert integer i1 "))
i2 = int(input("Insert integer i2, greater than i1 "))
while i1 >= i2:
    i2 = int(input("i2 should be greater than i1. Please, insert a greater integer "))
inc = int(input("Insert an increment "))
while inc <= 0:
    inc = int(input("The increment must be greater than 0. Please, insert a greater integer 1 "))
k = 0
j = 0
print("\nc:")
while j < i2 - inc:
    j = i1 + k * inc
    k = k + 1
    print(j, end=" ")

print("\nd:")
k = 0
j = 0
while j <= i2 - inc:
    j = i1 + k * inc
    k = k + 1
    print(j, end=" ")

print("\ne:")
k = 0
j = 0
while j > i1 + inc:
    j = i2 + k * inc * -1
    k = k + 1
    print(j, end=" ")