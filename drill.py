#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#   

from add import Add
from subtract import Subtract
from multiply import Multiply


#   Base class for drills, which run problem generators.

class Drill():
    def __init__(self, problemGen, numProblems):
        """
        Specify number of problems to generate.
        """
        self.generator = problemGen     # TODO: verify gen type
        self.problems = numProblems


    def run(self):
        """
        Generate and output problems.
        """
        for i in range(self.problems):
            self.generator.shuffle()
            self.generator.dump()
        

#   Test.

# drill = Drill(Add(10, 100), 5)
# drill.run()
# 
# drill = Drill(Subtract(10, 100), 5)
# drill.run()
# 
# drill = Drill(Multiply(10, 100), 5)
# drill.run()
# 
# 