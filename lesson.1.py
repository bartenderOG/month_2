class Hero:

    #Конструктор Класса
    def __init__(self, name, lvl, hp):
        #Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def rest(self):
        return f'{self.name} Отдыхает на чиле на расслабоне!!'


Lando = Hero('Lando', 80, 100500)
Lewis = Hero('Lewis', 79, 100000)

# print(Lando.rest())
# print(Lewis.rest())




#Объект|Экземпляр на основе класса
#Lando = Hero('Lando', 80, 100500)
# print(Lando.name)
# print(Lando.lvl)
# print(Lando.hp)
#
#
#Lewis = Hero('Lewis', 79, 100000)
# print(Lewis.name)
# print(Lewis.lvl)
# print(Lewis.hp)

# MageHero
# hero_lando

