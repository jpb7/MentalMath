#
#   Jacob Bentley
#   01/07/2022
#   Mental math app
#

from problem import Add
from drill import Chapter


#   Run all drills for this chapter with `n` problems per drill.

class ChapterOne(Chapter):
    def __init__(self, n):
        """
        Initialize to first drill for `n` repetitions.
        """
        generators = iter((TwoDigitAddition(),
                           ThreeDigitAddition()))

        super().__init__(generators, n)


class TwoDigitAddition(Add):
    def __init__(self):
        self.start = 10
        self.stop = 99
        super().__init__(self.start, self.stop)


class ThreeDigitAddition(Add):
    def __init__(self):
        self.start = 100
        self.stop = 999
        super().__init__(self.start, self.stop)