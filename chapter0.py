#
#   Jacob Bentley
#   12/30/2022
#   Mental math app
#

from random import randrange, choice
from problem import Multiply, Square
from drill import Chapter


#   Run all drills for Chapter 0 with `n` problems per drill.

class ChapterZero(Chapter):
    def __init__(self, n):
        """
        Initialize to first drill for `n` repetitions.
        """
        generators = iter((MultiplyByEleven(10, 100),
                           MultiplyByEleven(100, 999),
                           SquareTwoDigitEndingInFive(),
                           MultiplyComplementaryOnesDigit(),
                           CalculateTip(10, 100)))

        super().__init__(generators, n)


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


#   For finding a 15-percent tip given a check amount.

class CalculateTip(Multiply):
    def __init__(self, start, stop):
        """
        Initialize random check amount and 15%.
        """
        super().__init__(start, stop)
        self.b = 0.15
        self.shuffle()
    

    def shuffle(self):
        """
        Set random value for `a`.
        """
        self.a = randrange(self.start, self.stop)

    
    def solve(self):
        """
        Multiply `a` by 0.15 and round to two decimal places.
        """
        return round(self.a * self.b, 2)


#   Tests.

# d = ChapterZero(3)
# print(list(d.runAll()))

