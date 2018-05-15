    def pick_up(self):

        print("You pick up the %s" % self.name)


class Weapon(Item):
    def __init__(self, name):


    def attack(self, x=print("You attack with the %s" % self.name):
        x


bat = Weapon("Bat", 10)
sword = Weapon("Sword", 10)
S12k = Weapon("S12k", 25)
Scar = Weapon("Scar", 30)
M1911 = Weapon("M1911",15)


class Armour(Item):
    def _init_(self, name, armour):
        super(armour, self)._init_(name)
        self.armour = armour


    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage




class Room(object):
    def __init__(self, name, north, south, east, west):
        self.name = name
        self.north = north
        self.south = south
        self.east = east

        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


hdum = Room()
room1 = Room(1)
room2 = Room(3)
current_node = hdum
while True:
    print(current_node['NAME'])  # Change
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']

    print(current_node['DESCRIPTION'])  # Change
    command = input('>_').lower().strip()

    if command == 'quit':
        quit(0)
    elif command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]
    if command in directions:
        try:





