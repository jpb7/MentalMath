#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#   

from problem import Problem


#   Base class for drills, which run problem generators.

class Drill():
    def __init__(self, problemGen, numProblems):
        """
        Initialize problem generator and number of problems.
        """
        self.reset(problemGen)
        self.problems = numProblems

    
    def reset(self, problemGen):
        """
        Set the problem generator to a given type.
        """
        if isinstance(problemGen, Problem):
            self.generator = problemGen
        else:
            raise ValueError("Not a valid problem generator.")


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