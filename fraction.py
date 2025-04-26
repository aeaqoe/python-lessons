class Fraction:
    def __init__(self, number, denom):
        self.number = number
        self.denom = denom
    def __str__(self):
        return f'{self.number} / {self.denom}'
    def __add__(self, other):
        new_ch1 = self.number * other.denom
        new_ch2 = self.denom * other.number
        res_newch = new_ch1 + new_ch2
        newzn = self.denom * other.denom
        new_frac = Fraction(res_newch, newzn)
        return new_frac
        
oneHlaff = Fraction(1, 2)
twoThird = Fraction(2, 3)
print(oneHlaff + twoThird)

