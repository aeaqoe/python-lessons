class Goose():
    def __init__(self, name):
        self.name = name
        self.color = 'yellow'
    def __sub__(self, other):
        new_name = list(set(self.name)-set(other.name))
        new_name = ''.join(new_name)
        return Goose(new_name)
    def __len__(self):
        return len(self.name)
    def change_color(self, color):
        self.color = color
gray = Goose('mikhail')

white = Goose('lol')

new_goose = gray - white

print(new_goose.__dict__)

new_goose.change_color('yellow')

gray = Goose('семен')
print(new_goose.__dict__)
print(new_goose.__dict__)



