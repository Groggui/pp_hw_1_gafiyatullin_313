def calc(num1, symb, num2):
    if symb == '+':
        return num1 + num2
    elif symb == '-':
        return num1 - num2
    elif symb == '*':
        return num1 * num2
    elif symb == '/':
        return num1 / num2


print(calc(int(input('enter the number: ')), input('enter +, -, * or /: '), int(input('enter the number: '))))
