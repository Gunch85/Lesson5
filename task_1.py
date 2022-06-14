a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите операцию: ")

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
while a == 0 or b == 0 and c == '/':
    print("На ноль делить нельзя!")
    break