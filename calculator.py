print("Ноль в качестве знака операции завершит работу калькулятора.")

while True:
    s = input("Операция (+, -, *, /): ")
    if s == '0':
        break

    elif s in ('+', '-', '*', '/'):

        x = float(input('Первое число: '))
        y = float(input('Второе число: '))

        if s == '+':
            print('%.2f' % (x + y))

        elif s == '-':
            print("%.2f" % (x - y))

        elif s == '*':
            print("%.2f" % (x * y))

        elif s == '/':
            if x != 0 and y != 0:
                print("%.2f" % (x / y))

            else:
                print("Деление на ноль!")

        else:
            print("Неверный знак операции!")