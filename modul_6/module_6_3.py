import random

class Animal:  # ОПИСАНИЕ ЖИВОТНЫХ
    live = True  # ЖИВОЙ
    sound = None  # ГЛУХОНЕМОЙ по умолчанию
    _DEGREE_OF_DANGER = 0  # УРОВЕНЬ ОПАСНОСТИ

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве.
        self.speed = speed  # скорость передвижения существа (определяется при создании объекта)
        # [0, 0, 0] это список координат, к которым можно обращаться по индексу

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0 # z в _cords значение будет меньше 0, то значение не меняется

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f'Sorry, i''m peaceful :)')
        else:
            print(f'Be careful, i''m attacking you 0_0')

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz): # ныряние под воду
        self._cords[2] -= int(abs(dz) * self.speed / 2) # Скорость уменьшается в 2 раза
        if self._cords[2] < 0:
            self._cords[2] = 0 # Координата Z не может быть отрицательной

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"  # звук, который издаёт утконос


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
