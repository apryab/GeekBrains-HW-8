from abc import ABC, abstractmethod


class Warehouse:
    hist_dict = dict()
    n = 0

    def reception(self, product):
        if (type(product) == Xerox) or (type(product) == Scan) or (type(product) == Printer):
            self.n += 1
            self.hist_dict[self.n] = product
        else:
            print('Продукты такого типа мы не держим на складе')

    def transfer(self, prod_type, comp_name):
        check = 0
        if prod_type == 'Xerox':
            check = 1
            transfer_list = []
            keys_list = self.hist_dict.keys()
            for elem in keys_list:
                if type(self.hist_dict.get(elem)) == Xerox:
                    transfer_list.append(self.hist_dict.get(elem))
            print('Товары указанной категории отправлены по компании', comp_name)
            print('Количество товаров равно', len(transfer_list))
        if prod_type == 'Printer':
            check = 1
            transfer_list = []
            keys_list = self.hist_dict.keys()
            for elem in keys_list:
                if type(self.hist_dict.get(elem)) == Printer:
                    transfer_list.append(self.hist_dict.get(elem))
            print('Товары указанной категории отправлены по компании', comp_name)
            print('Количество товаров равно', len(transfer_list))
        if prod_type == 'Scan':
            check = 1
            transfer_list = []
            keys_list = self.hist_dict.keys()
            for elem in keys_list:
                if type(self.hist_dict.get(elem)) == Scan:
                    transfer_list.append(self.hist_dict.get(elem))
            print('Товары указанной категории отправлены компании', comp_name)
            print('Количество товаров равно', len(transfer_list))
        if check == 0:
            print('Такой категории для отправки нет')


class OrgTech(ABC):
    size = ''

    @abstractmethod
    def __init__(self, thing):
        pass


class Scan(OrgTech):
    size = 'small'

    def __init__(self, param):
        super().__init__(param)
        self.type = param


class Xerox(OrgTech):
    size = 'big'

    def __init__(self, param):
        super().__init__(param)
        self.color = param


class Printer(OrgTech):
    size = 'medium'

    def __init__(self, param):
        super().__init__(param)
        self.producer = param


my_printer = Printer('canon')
my_scan = Scan('laser')
my_xerox = Xerox('black')
my_warehouse = Warehouse()
my_warehouse.reception(my_printer)
my_warehouse.reception(my_scan)
my_warehouse.reception(my_xerox)
my_warehouse.transfer('Scan', 'Canon')
