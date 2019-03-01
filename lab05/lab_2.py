
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

"""
Hand-work:
a. P(Cancer|test1^test2) = a <P(Cancer|test1^test2), P(-Cancer|test1^test2)>
                         = a <0.01 * 0.9 * 0.9 , 0.99 * 0.2 * 0.2>
                         = a <0.0081, 0.0396>
                         = <0.170, 0.830>

b. P(Cancer|test1^-test2) = a <P(Cancer|test1^-test2), P(-Cancer|test1^-test2)>
                         = a <0.01 * 0.9 * 0.1, 0.99 * 0.2 * 0.8>
                         = a <0.0009, 0.1584>
                         = <0.0006, 0.994>                        
"""