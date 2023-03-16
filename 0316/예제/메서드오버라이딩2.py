class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with a normal attack.")

class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength

    # 오버라이딩
    def attack(self):
        print(f"{self.name} attacks with a mighty swing.")

    def smash(self):
        print(f"{self.name} smashes the ground with a powerful blow.")

class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic

    # 오버라이딩
    def attack(self):
        print(f"{self.name} casts a magic missile.")

    def teleport(self):
        print(f"{self.name} teleports to a nearby location.")


c = Character("Bob", 10, 100)
c.attack()  # Bob attacks with a normal attack.

w = Warrior("Conan", 20, 200, 15)
w.attack()  # Conan attacks with a mighty swing.
w.smash()   # Conan smashes the ground with a powerful blow.

m = Mage("Merlin", 15, 150, 30)
m.attack()  # Merlin casts a magic missile.
m.teleport()  # Merlin teleports to a nearby location.
