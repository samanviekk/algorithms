class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


myFraction = Fraction(3, 5)
myFraction.show()
print(myFraction)
print(myFraction.__str__())
print(str(myFraction))

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(f1.__add__(f2))