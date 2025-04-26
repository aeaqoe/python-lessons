from random import randint
from functools import reduce
class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'this poition named: {self.name}'
    def __add__(self, other):
        self_len = len(self.name) // randint(1, len(self.name) - 1)
        other_len = len(other.name) // randint(1, len(other.name) - 1)
        new_name = self.name[:self_len] + other.name[other_len:]
        new_quanity = (self.quality + other.quality) // 2
        return Potion(new_name, new_quanity)
    
    def check_quality(self):
        print(self.name, self.quality)
        if self.quality > 75:
            print("very good poition")
        elif self.quality > 30:
            print("poition is average")
        else:
            print("poition has bad quality")

while True:
    count_poisitions = int(input("введи число зелий: "))
    list_poitions = []
    for i in range(1, count_poisitions + 1):
        name_poition = input(f"введите название {i} зелья: ")
        quality_potion = randint(10, 100)
        list_poitions.append(Potion(name_poition, quality_potion))
    new_poition = reduce(lambda x, y: x + y, list_poitions)
    new_poition.check_quality()