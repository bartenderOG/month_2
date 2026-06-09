# class Math:
#
#     def add(self, a, b):
#         return a + b
#
# obj_test = Math()
# print(obj_test.add(12, 12))



# class Bank:
#     #Атрибуты класса
#     name = "Mbank"
#     def __init__(self, value):
#         self.value = value
#     #Атрибуты экземпляра класса
#     def get_value(self):
#         return self.value
#
#     @classmethod
#     def get_name(cls):
#         return cls.name
#
#     @classmethod
#     def base_create(cls):
#         return cls('Base value')
#
#
#
#
#
# bank = Bank('Ardager')
# bank_1 = Bank.base_create()

# print(bank.get_value())
# print(bank.get_name())
# print(bank_1.get_value())
# print(bank_1.get_name())

# class Product:
#     def __init__(self, price):
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price

#     def get_price(self):
#         return self.__price
#
# iphone = Product(1250)

# print(iphone.get_price())
# print(iphone.price)



    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError("Price must be positive")
    #     self.__price = value
    #
    # def get_price(self):
    #     return self.__price

# iphone = Product(1250)
#
# print(iphone.price)
# iphone.price = 200
# print(iphone.price)
# iphone.price = -200


# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return self.first_name + " " + self.last_name
#
# ardager = User('Ardager', 'Kartanbekov')
#
# print(ardager.full_name)


def simple_decarator(func):
    def wrapper():
        print('До выполнения!')
        func()
        print('После выполнения!')
    return wrapper


@simple_decarator
def say_hello():
    print('Hello kitty')

# say_hello()

def greeting_decorator(func):
    def wrapper(name):
        print(f'Hello {name}')
        func(name)
    return wrapper

@greeting_decorator
def greeting(name):
    print(f'Hello {name}')

# greeting('Kitty')

def repeat_decoraor(value):
    def decorator(func):
        def wrapper():
            for i in range(value):
                func()
        return wrapper
    return decorator

@repeat_decoraor(1000)
def hello():
    print('Hello kitty<3')

# hello()

def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print('New action')
    return NewClass
@class_decorator
class OldClass:
    def action(self):
        print('Old action')


test_obj = OldClass()

test_obj.action()


