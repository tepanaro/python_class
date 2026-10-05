i1 = int(input("Insert integer i1 "))
i2 = int(input("Insert integer i2, greater than i1 "))
while i1 >= i2:
    i2 = int(input("i2 should be greater than i1. Please, insert a greater integer "))
inc = int(input("Insert an increment "))
while inc <= 0:
    inc = int(input("The increment must be greater than 0. Please, insert a greater integer 1 "))
k = 0
j = 0
print("\nc while loop, i2 not included:")
while j < i2 - inc:
    j = i1 + k * inc
    k = k + 1
    print(j, end=" ")

print("\nd while loop, i2 included:")
k = 0
j = 0
while j <= i2 - inc:
    j = i1 + k * inc
    k = k + 1
    print(j, end=" ")

print("\ne while loop, i1 not included:")
k = 0
j = i2
while j > i1 + inc:
    j = i2 + k * inc * -1
    k = k + 1
    print(j, end=" ")

print("\nf while loop, i1 included:")
k = 0
j = i2
while j >= i1 + inc:
    j = i2 + k * inc * -1
    k = k + 1
    print(j, end=" ")

print("\ng for loop, i2 not included:")
for i in range(i1, i2, inc):
    print(i, end=" ")

print("\nh for loop, i2 included:")
for i in range(i1, i2 + 1, inc):
    print(i, end=" ")

print("\ni for loop, i2 not included but reversed:")
for i in range(i2 - inc, i1 - 1, -inc):
    print(i, end=" ")

print("\nj for loop, i1 not included but reversed:")
for i in range(i2, i1, -inc):
    print(i, end=" ")