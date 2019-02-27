
from tools.aima.probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# create the Bayes Network
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

print("Exercise 5.2")
# a. P(Cancer | test1 ^ test2)
print("a. ", enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# b. P(Cancer | test1 ^ -test2)
print("b. ", enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

"""
The results make sense, having one test failed will decrease the probability of the subject decrease by a great extent. 
"""