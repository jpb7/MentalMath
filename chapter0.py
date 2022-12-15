#
#   Jacob Bentley
#   12/14/2022
#   Mental math app
#

from random import randrange, choice
from multiply import Multiply
from square import Square


#   For multiplying two-digit numbers by 11.

class MultiplyByEleven(Multiply):
    def __init__(self, start, stop):
        """
        Initialize random value and ... 11.
        """
        super().__init__(start, stop)
        self.b = 11
        self.shuffle()
    

    def shuffle(self):
        """
        Randomly select a value for `a`.
        """
        self.a = randrange(self.start, self.stop)


#   For squaring two-digit numbers ending in 5.

class SquareTwoDigitEndingInFive(Square):
    def __init__(self):
        """
        Initialize target values and instantiate base-class object.
        """
        self.numbers = (5, 15, 25, 35, 45, 55, 65, 75, 85, 95)
        self.shuffle()

    
    def shuffle(self):
        """
        Randomly select target value from above.
        """
        self.a = self.b = choice(self.numbers)


#   For multiplying two-digit numbers whose ones digits sum to 10.

class MultiplyComplementaryOnesDigit(Multiply):
    def __init__(self):
        """
        Initialize `a` and `b` to values with same tens and
        complementary ones digits.
        """
        self.shuffle()
    

    def shuffle(self):
        """
        Randomly select a two-digit value and then find a complement.
        """
        self.a = randrange(10, 100)
        self.b = self.a + 10 - 2*(self.a % 10)

#   Tests.

p = MultiplyByEleven(10, 100)

print("\nMultiply two-digit numbers by 11:")
for i in range(3):
    p.shuffle()
    p.dump()

p = MultiplyByEleven(100, 999)

print("\nMultiply three-digit numbers by 11:")
for i in range(3):
    p.shuffle()
    p.dump()

p = SquareTwoDigitEndingInFive()

print("\nSquare two-digit numbers ending in 5:")
for i in range(3):
    p.shuffle()
    p.dump()

p = MultiplyComplementaryOnesDigit()

print("\nMultiply two-digit numbers whose ones digits sum to 10:")
for i in range(3):
    p.shuffle()
    p.dump()

print()

