class Data:

    def __init__(self, string):
        self.string = string

    @classmethod
    def str_to_numb(cls, string):
        temp_list = string.split('-')
        answer_list = []
        if len(temp_list) != 3:
            print('Неправильный формат записи. Будет возвращён пустой список')
            return []
        else:
            try:
                for elem in temp_list:
                    answer_list.append(int(elem))
                print('Всё хорошо! Будет возвращён список с числами')
                return answer_list
            except(TypeError, ValueError):
                print('Нельзя преобразовать в число. Будет возвращён пустой список')
                return []

    @staticmethod
    def validate(string):
        temp_list = string.split('-')
        valid_list = []
        valid_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        check = 1
        if len(temp_list) != 3:
            print('Неправильный формат записи.')
        else:
            try:
                for elem in temp_list:
                    valid_list.append(int(elem))
            except(TypeError, ValueError):
                print('Неправильный формат данных')
                check = 0
            if check == 1:
                if not 0 < valid_list[1] < 13:
                    check = 0
                    print('Такого месяца не существует')
            if check == 1:
                if not 0 < valid_list[2] < 2021:
                    check = 0
                    print('Такого года ещё не было')
            if check == 1:
                if valid_list[1] == 2:
                    if valid_list[2] % 4 == 0:
                        if not 0 < valid_list[0] < 30:
                            check = 0
                            print('Такого дня не было')
                    else:
                        if not 0 < valid_list[0] < 29:
                            check = 0
                            print('Такого дня не было')
                else:
                    if not 0 < valid_list[0] <= valid_dict.get(valid_list[1]):
                        check = 0
                        print('Такого дня не было')
            if check == 0:
                print('Дата не подтверждена')
            else:
                print('Дата прошла проверку')


my_data = Data('28-03-2019')
print(my_data.str_to_numb(my_data.string))
Data.validate(my_data.string)
