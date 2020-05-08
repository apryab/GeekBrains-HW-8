class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input('Введите ваше делимое '))
    b = float(input('Введите ваш делитель '))
    if b == 0:
        raise OwnError('На ноль делить нельзя')
    answer = a / b
    print('Результат деления -', answer)
except OwnError as err:
    print(err)
except(TypeError, ValueError):
    print('Вы ввели не число')
