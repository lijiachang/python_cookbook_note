from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.nam = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width  # 平方英尺


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        """计算可用空间"""
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return f'{self.name}:{self.living_space_footage} square foot {self.style}'

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


# 定义三种类型，不同大小的房子
h1 = House('h1', 'beijing')
h1.add_room(Room('Master bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))

h2 = House('h2', 'qingdao')
h2.add_room(Room('Master bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('kitchen', 12, 16))

h3 = House('h3', 'shanghai')
h3.add_room(Room('Master bedroom', 14, 21))
h3.add_room(Room('Living Room', 18, 20))
h3.add_room(Room('kitchen', 15, 17))
h3.add_room(Room('Office', 12, 16))

houses = [h1, h2, h3]
print('Is h1 bigger tan h2?', h1 > h2)
print('Is h2 smaller than h3?', h2 < h3)
print('Is h2 greater than or equal to h1?', h2 >= h1)
print('Which one is biggest?', max(houses))
print('Which is smallest?', min((houses)))
