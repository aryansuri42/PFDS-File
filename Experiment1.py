num1 = int(input("Enter Num: "))
num2 = int(input("Enter Num: "))
oper = input("Enter Operation: ")
if oper == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif oper == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif oper == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif oper == '/':
    print(f"{num1} / {num2} = {num1 / num2}")