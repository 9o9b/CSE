YYclass Item(object):
        self.name = name

    def pick_up(self):

        print("You pick up the %s" % self.name)


class Weapon(Item):
    def __init__(self, name):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


    def attack(self):
        print("You attack with the %s" % self.name)



bat = Weapon("Bat", 10)
sword = Weapon("Sword", 10)
S12k = Weapon("S12k", 25)
Scar = Weapon("Scar", 30)
M1911 = Weapon("M1911", 15)


class Armour(Item):
    def _init_(self, name, armour):
        super(armour, self)._init_(name)
        self.armour = armour
