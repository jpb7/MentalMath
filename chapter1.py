#
#   Jacob Bentley
#   01/07/2022
#   Mental math app
#

from random import randrange
from problem import Add, Subtract
from drill import Chapter


#   Run all drills for Chapter 1 with `n` problems per drill.

class ChapterOne(Chapter):
    def __init__(self, n):
        """
        Initialize to first drill for `n` repetitions.
        """
        generators = iter((TwoDigitAddition(),
                           ThreeDigitAddition(),
                           TwoDigitSubtraction(),
                           ThreeDigitSubtraction(),
                           UsingComplements()))

        super().__init__(generators, n)


#   For adding two digit numbers.

class TwoDigitAddition(Add):
    def __init__(self):
        self.start = 10
        self.stop = 99
        super().__init__(self.start, self.stop)


#   For adding three digit numbers.

class ThreeDigitAddition(Add):
    def __init__(self):
        self.start = 100
        self.stop = 999
        super().__init__(self.start, self.stop)


#   For subtracting two digit numbers.

class TwoDigitSubtraction(Subtract):
    def __init__(self):
        self.start = 10
        self.stop = 99
        super().__init__(self.start, self.stop)


#   For subtracting three digit numbers.

class ThreeDigitSubtraction(Subtract):
    def __init__(self):
        self.start = 100
        self.stop = 999
        super().__init__(self.start, self.stop)


#   For finding two-digit complements that sum to 100.

class UsingComplements(Subtract):
    def __init__(self):
        self.start = 10
        self.stop = 99
        super().__init__(self.start, self.stop)
    

    def shuffle(self):
        self.a = randrange(self.start, self.stop)
        self.b = 100

