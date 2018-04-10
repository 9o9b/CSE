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

        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")


class charerter(Persons):
    def __init__(self, name, age, uniform, ):
        self.name = name
        self.age = age
        self.uniform = uniform