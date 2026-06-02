#Принципы ООП. Инкапсуляция, Абстракция. Гит-Ветки



#Инкапсуляция


import random
import string


class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password
        self._balance = balance

    def get_user_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return'Неверный пароль'

    def __random_pass(self):
        data = string.ascii_letters + string.digits
        password = ''.join(random.choice(data) for _ in range(6))
        return password

    def get_random_pass(self):
        return self.__random_pass()

# class VIPaccount(BankAccount):
#     pass



# ardager = BankAccount('Ardager', "1234748", 10000)
# print(ardager._BankAccount__random_pass())

# print(dir(BankAccount))





#Абстракция



from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def move(self):
        return 'Step'
    def make_sound(self):
        return "Woof Woof"

guffi = Dog()

# print(guffi.make_sound())
# print(guffi.move())


class SendSMS(ABC):
    @abstractmethod
    def send_otp_to_phone(self, phone):
        pass

class KGSendSms(SendSMS):

    def request(self, data):
        pass

    def send_otp_to_phone(self, phone):
        data = f'''
        <Phone>{phone}</Phone>
        <text>Ваш ко; 098673</text>
        '''
        self.request(data)


class RUSendSms(SendSMS):
    def request(self, data):
        pass
    def send_otp_to_phone(self, phone):
        data = {
            'phone': phone,
            'text': 'Ваш код: 563785'
        }
        self.request(data)




