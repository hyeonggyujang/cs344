from tools.aima.probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.12a
bayes_net = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00})
    ])

# i
print("i.", enumeration_ask('Cloudy', dict(), bayes_net).show_approx())
# ii
print("ii.", enumeration_ask('Sprinkler', dict(Cloudy=T), bayes_net).show_approx())
# iii
print("iii.", enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=T), bayes_net).show_approx())
# iv
print("iv.", enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), bayes_net).show_approx())
# v
print("v.", enumeration_ask('Cloudy', dict(WetGrass=F), bayes_net).show_approx())