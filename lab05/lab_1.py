'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

The implementation by kvlinden is implemented into this file.
@revisor: hj35
@date: 02/28/2019
'''

from tools.aima.probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# # Compute P(Burglary | John and Mary both call) using the enumeration-ask and elimination-ask algorithms
# # See the explanation of the algorithms in Section 14.4.
# print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
#

print("Exercise 5.1")
# a.i. P(Alarm | burglary ^ -earthquake)
print("a. i.   ", enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# a.ii. P(John | burglary ^ -earthquake)
print("   ii.  ", enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# a.iii. P(Burglary | alarm)
print("   iii. ", enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# a.iv. P(Burglary | john ^ mary)
print("   iv.  ", enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

"""
The probability of Alarm going off given there is burglary but not earthquake is 0.94.
The probability of John calling given there is burglary but not earthquake is  0.849.
The probability of burglary happening when alarm goes off is 0.374.
The probability of burglary happening when both John and Mary calling is 0.284.
"""
