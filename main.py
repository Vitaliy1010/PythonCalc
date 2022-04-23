# 23.04.2022
activate = True
while activate:
    user = input("(+, -) > ")
    if user == "+":
        num1 = float(input("Num1: "))
        num2 = float(input("Num2: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif user == "-":
        num1 = float(input("Num1: "))
        num2 = float(input("Num2: "))
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif user == "exit" or user == "0":
        activate = False
        print("OFF")
    else:
        print("Выберите правельное действие!\n")

