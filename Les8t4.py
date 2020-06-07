#Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.


class Warehouse:

    count = 0
    send_count = 0
    catalog = {}
    send_catalog = {}

    def __init__(self, object):
        Warehouse.count += 1
        Warehouse.catalog[Warehouse.count] = str(object)

    #def __del__(self):
        #print('Товар удален из каталога')

    def send(self, number):
        self.number = number
        if self.number in Warehouse.catalog.keys():
            send_box = Warehouse.catalog[self.number]
            Warehouse.send_count += 1
            Warehouse.send_catalog[Warehouse.send_count] = send_box
                #if Warehouse.object.count == key:
                    #object.__del__(self)
                #print(send_box)
            print(f'Товар удален из каталога: {send_box}')
            del Warehouse.catalog[self.number]



class OfficeEquipment:

    def CheckValueInt(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def CheckValueStr(x):
        if isinstance(x, str):
            return True
        return False

    def __init__(self, inv_number, cost, model):
        if OfficeEquipment.CheckValueInt(inv_number):
            self.inv_number = inv_number
        else:
            print('Неправильно введена запись')
        if OfficeEquipment.CheckValueInt(cost):
            self.cost = cost
        else:
            print('Неправильно введена запись')
        if OfficeEquipment.CheckValueStr(model):
            self.model = model
        else:
            print('Неправильно введена запись')



class Printer(OfficeEquipment):
    def __init__(self, inv_number, cost, model, expen_materials):
        super().__init__(inv_number, cost, model)
        if Printer.CheckValueInt(expen_materials):
            self.expen_materials = expen_materials
        else:
            print('Неправильно введена запись')

    def __str__(self):
        return f'Категория: Принтер, Инв.Номер: {self.inv_number}, Модель: {self.model}, Стоимость: {self.cost}, Стоимость расх.материалов: {self.expen_materials}'



class Laptop(OfficeEquipment):
    def __init__(self, inv_number, cost, model, core):
        super().__init__(inv_number, cost, model)
        if Laptop.CheckValueInt(core):
            self.core = core
        else:
            print('Неправильно введена запись')

    def __str__(self):
        return f'Категория: Ноутбук, Инв.Номер: {self.inv_number}, Модель: {self.model}, Стоимость: {self.cost}, Ядро: {self.core}'


class Scaner(OfficeEquipment):
    def __init__(self, inv_number, cost, model, resol):
        super().__init__(inv_number, cost, model)
        if Scaner.CheckValueStr(resol):
            self.resol = resol
        else:
            print('Неправильно введена запись')

    def __str__(self):
        return f'Категория: Сканер, Инв.Номер: {self.inv_number}, Модель: {self.model}, Стоимость: {self.cost}, Разрешение: {self.resol}'

Categ = OfficeEquipment('jyvy ' , 300, 'что-то')

toshiba_34 = Laptop(12, 3000, 'Toshiba RHD200', 4)
print(toshiba_34)
Canon1020 = Printer(15, 6000, 'Canon1020', 5000)
print(Canon1020)
Panasonic_2 = Scaner(3, 4500, 'Panasonic RDX100', '300dpi')
print(Panasonic_2)
pr_1 = Warehouse(Canon1020)
print(Warehouse.catalog)
pr_2 = Warehouse(Panasonic_2)
print(Warehouse.catalog)
pr_3 = Warehouse(toshiba_34)
pr_1.send(1)
print(Warehouse.catalog)
print(Warehouse.send_catalog)

