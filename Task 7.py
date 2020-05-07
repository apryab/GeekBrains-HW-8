class Complex:

    def __init__(self, var1, var2):
        try:
            self.a = float(var1)
            self.b = float(var2)
        except(TypeError, ValueError):
            print('Неверный тип данных. Будет создано нулевое число')
            self.a = 0
            self.b = 0

    def __add__(self, other):
        if type(other) == Complex:
            answer_a = self.a + other.a
            answer_b = self.b + other.b
            return Complex(answer_a, answer_b)
        else:
            print('Неверный тип правого операнда')
            raise TypeError

    def __mul__(self, other):
        if type(other) == Complex:
            answer_a = self.a * other.a - self.b * other.b
            answer_b = self.a * other.b + self.b * other.a
            return Complex(answer_a, answer_b)
        else:
            print('Неверный тип правого операнда')
            raise TypeError

    def __str__(self):
        str_a = str(self.a)
        str_b = str(self.b)
        big_str = str_a + ' ' + '+' + ' ' + 'i' + ' ' + '*' + ' ' + str_b
        return big_str


my_numb_1 = Complex(3, 5)
my_numb_2 = Complex(1, 7)
add_answer = my_numb_1 + my_numb_2
mul_answer = my_numb_1 * my_numb_2
print(add_answer)
print(mul_answer)