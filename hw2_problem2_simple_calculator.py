operation = input("Introduce the operation and use spaces to separate the operand from the numbers ")
#operation_list = operation.split() If we use this method it would be quicker, but not sure if accepted for this homework.



operation_list = list(operation)
i = 0
operand1 = ""
operand2 = ""
operation_sign = ""
result = ""
while i < len(operation_list):
    if operand1 == "":
        if operation_list[i] == " ":
            operand1 = result
            result = ""
        else:
            result = result + operation_list[i]
    elif operation_sign == "":
        operation_sign = operation_list[i]
    elif operand2 == "":
            if operation_list[i] != " ":
                result = result + operation_list[i]
                if i == len(operation_list) - 1:
                     operand2 = result                 
    i = i + 1
# print("operand 1", operand1)
# print("operation sign", operation_sign)
# print("operand 2", operand2)

operation_list_result = [operand1, operation_sign, operand2]

operand1 = float(operation_list_result[0])
operand2 = float(operation_list_result[2])
operation_sign = operation_list_result[1]

result = 0
if operation_sign == "+":
    result = operand1 + operand2
elif operation_sign == "-":
    result = operand1 - operand2
elif operation_sign == "*":
    result = operand1 * operand2
else:
    result = operand1 / operand2

print("The result is", result)