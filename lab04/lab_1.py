'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from tools.aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576



# Exercise 4.1
# a.
# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())


# b.
# by hand:
'''
P(Cavity|catch) = P(Cavity ^ catch) / P(catch)
                = (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144)
                = (0.18) / (0.34)
                = 0.529
'''
# Compute P(Cavity|Catch=T)  (see the text, page 493).
PC_1 = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC_1.show_approx())

# c.
C = JointProbDist(['Coin1', 'Coin2'])
H, T = True, False
C[H, H] = 0.25; C[H, T] = 0.25
C[T, H] = 0.25; C[T, T] = 0.25
PC_2 = enumerate_joint_ask('Coin2', {'Coin1': T}, C)
print(PC_2.show_approx())

'''
Can you see now why the full joint is generally not used in probabilistic systems?
Yes, we need to have full list of probability distribution for all possible outcomes, which is 
extremely inefficient when there are many variables and many dimensions of variables. 
'''
