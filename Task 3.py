class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


my_list = []
while True:
    try:
        temp = input('Введите ваше число. Введите * чтобы закончить ')
        if temp != '*':
            if is_digit(temp):
                temp = float(temp)
                my_list.append(temp)
            else:
                raise OwnError('В список можно вводить только числа')
        else:
            print(my_list)
            break
    except OwnError as err:
        print(err)
