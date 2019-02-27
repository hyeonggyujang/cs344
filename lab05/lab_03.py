
from tools.aima.probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# create the Bayes Network
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

print("Exercise 5.3")
# a.i. P(Raise | sunny)
print("a. i.  ", enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
# a.ii. P(Raise | happy ^ sunny)
print("   ii. ", enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

# b.i. P(Raise | happy)
print("b. i.  ", enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
# b.ii. P(Raise | happy ^ -sunny)
print("   ii. ", enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

"""
The results don't make sense to me, because the Bayes Network in this case is a small-scale directed graph, 
which 'Happy' doesn't point towards 'Sunny' or 'Raise'. However, for some reason, I get the probability distribution. 
"""
