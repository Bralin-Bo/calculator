def get_number(value):
    newValue = ''
    while type(newValue)!=int:
        number = input(value)
        try:
            newValue = int(number)
        except:
            print("Это не цифра")
    return newValue

def get_operation():
    newValue = ''
    allowedChars = ['/', '*', '+', '-']
    while newValue not in allowedChars:
        newValue = input("""Выберите операцию: 
    - = вычитание
    + = сложение
    / = деление
    * = умножение
    """)
    return newValue

def calculate(firstNumber, operation, secondNumber):
    if operation == '/' and secondNumber == 0:
        print('Нельзя делить на ноль!')
        return
    if operation == '+':
        print(firstNumber+secondNumber)
    elif operation == '-':
        print(firstNumber-secondNumber)
    elif operation == '/':
        print(firstNumber/secondNumber)
    elif operation == '*':
        print(firstNumber*secondNumber)

inProcess = True
while inProcess:
    firstNumber = get_number('Введите первую цифру: ')
    operation = get_operation()
    secondNumber = get_number('Введите вторую цифру: ')
    
    calculate(firstNumber, operation, secondNumber)
    print('\n\n\n')
    isStop = input('Вы хотите продолжить? \nДа - продолжить \nНет - закончить\n')
    if isStop == 'Да' or isStop == 'да':
        pass
    elif isStop == 'Нет' or isStop == 'нет':
        print('Спасибо за использование программы!')
        inProcess = False
        break
    else:
        print('Вы ввели что то другое, программа завершится')
        inProcess = False
        break

input()
