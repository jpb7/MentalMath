#
#   Jacob Bentley
#   01/10/2022
#   Mental math app
#

from random import randrange
from problem import Multiply
from drill import Chapter


#   Run all drills for Chapter 2 with `n` problems per drill.

class ChapterTwo(Chapter):
    def __init__(self, n):
        """
        Initialize to first drill for `n` repetitions.
        """
        generators = iter((MultiplyTwoByOne(),
                           MultiplyThreeByOne()))

        super().__init__(generators, n)


#   Multiply two-digit numbers by one-digit numbers.

class MultiplyTwoByOne(Multiply):
    def __init__(self):
        self.start = 10
        self.stop = 99
        super().__init__(self.start, self.stop)
    

    def shuffle(self):
        self.a = randrange(10, 99)
        self.b = randrange(2, 9)


#   Multiply three-digit numbers by one-digit numbers.

class MultiplyThreeByOne(Multiply):
    def __init__(self):
        self.start = 100
        self.stop = 999
        super().__init__(self.start, self.stop)
    

    def shuffle(self):
        self.a = randrange(100, 999)
        self.b = randrange(2, 9)

