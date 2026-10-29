class Тварина:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age} років")

    def sound(self):
        print("Тварина видає звук")


class Собака(Тварина):
    def sound(self):
        print("Гав-гав!")


class Кіт(Тварина):
    def sound(self):
        print("Няв-няв!")


dog = Собака("Рекс", 3)
cat = Кіт("Мурчик", 2)

print("Собака:")
dog.info()
dog.sound()

print()

print("Кіт:")
cat.info()
cat.sound()