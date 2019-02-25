from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search, recursive_best_first_search
import random
import math
import time

class TSP(Problem):
    """
    """

    def __init__(self, size, initial, distance):
        self.size = size
        self.distance = distance
        self.initial = initial

    def actions(self, state):
        swap_list = []
        for i in range(10):
            index1 = [random.sample(range(1, len(state)-1), 2)]
            swap_list.append(index1)
        return swap_list

    def result(self, state, actions):
        new_state = state[:]
        index1 = state[actions[0][0]]
        index2 = state[actions[0][1]]
        new_state[actions[0][0]] = index2
        new_state[actions[0][1]] = index1
        return new_state

    def value(self, state):
        dist_sum = 0
        for i in range(len(state) - 1):
            lst = [state[i], state[i+1]]
            lst.sort()
            dist_sum += self.distance[tuple(lst)]
        return -1 * dist_sum


if __name__ == '__main__':
    size_in = 5
    initial_in = [0, 1, 2, 3, 4, 0]
    distance_in = {(0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 2,
                   (1, 2): 1, (1, 3): 3, (1, 4): 3,
                   (2, 3): 3, (2, 4): 3,
                   (3, 4): 6}

    print('Start:    ' + str(initial_in))

    # Initialize the NQueens problem
    p = TSP(size=size_in, initial=initial_in, distance=distance_in)
    print('Value:    ' + str(p.value(initial_in)))

    # Solve the problem using hill climbing.
    hill_solution = hill_climbing(p)
    print('Hill-climbing:')
    print('\tSolution: ' + str(hill_solution))
    print('\tValue:    ' + str(p.value(hill_solution)))

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    print('Simulated annealing:')
    print('\tSolution: ' + str(annealing_solution))
    print('\tValue:    ' + str(p.value(annealing_solution)))