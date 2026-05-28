
class Hero:



    def __init__(self, name, lvl, healthpoint, strength):
        self.name = name
        self.lvl = lvl
        self.healthpoint = healthpoint
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.lvl}')

    def attack(self):
        print(f'{self.name} наносит удар')
        self.strength -= 1

    def rest(self):
        print(f'{self.name} отдыхает...')
        self.healthpoint += 1




Lando = Hero('Lando', 80, 100, 99)
Lewis = Hero('Lewis', 60, 100, 80)

Lando.greet()
Lando.attack()
print(f'Сила после аттаки {Lando.strength}:')
Lando.rest()
print(f'Здоровье после отдыха {Lando.healthpoint}')


print('-' * 40)


Lewis.greet()
Lewis.attack()
print(f'Сила после аттаки {Lewis.strength}:')
Lewis.rest()
print(f'Здоровье после отдыха {Lewis.healthpoint}')





