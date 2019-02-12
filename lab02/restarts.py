"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.0001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.

    #print('Initial                      x: ' + str(p.initial)
    #      + '\t\tvalue: ' + str(p.value(initial))
    #      )

    # Solve the problem using hill-climbing.
    # Implement random-start hill-climbing
    startTime = time.time()

    solutions = {}          # Create an empty dictionary
    numIteration = 20       # Set the number of iteration
    for i in range(numIteration):     # Do 20 random starts
        maximum = 30.0
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=1.0)
        solutions.update({p.value(hill_climbing(p)): hill_climbing(p)})  # Add an key:value as value:x

    endTime = time.time() - startTime

    fsolutionval = max(solutions.keys())             # Find and store the maximum value
    fsolutionx = solutions[fsolutionval]             # Find and store the x value of the maximum value
    average = sum(solutions.keys()) / numIteration   # Find and store the average of the values

    print('Hill-climbing solution (random-restart)       x: ' + str(fsolutionval)
          + '\tvalue: ' + str(fsolutionx)
          + '\t\ttime: ' + str(endTime)
          + '\t\taverage: ' + str(average)
          )

    # Solve the problem using simulated annealing.
    # Implement random-start simulated annealing
    # Documentation is not repeated, as the algorithm is parallel to that of hill-climbing.
    startTime = time.time()
    solutions = {}
    numIteration = 20
    for i in range(numIteration):
        maximum = 30.0
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=0.10)
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        solutions.update({p.value(annealing_solution): annealing_solution})
    endTime = time.time() - startTime

    fsolutionval = max(solutions.keys())
    fsolutionx = solutions[fsolutionval]
    average = sum(solutions.keys()) / numIteration


    print('Simulated annealing solution (random-start)   x: ' + str(fsolutionval)
          + '\tvalue: ' + str(fsolutionx)
          + '\t\ttime: ' + str(endTime)
          + '\t\taverage: ' + str(average)
          )
