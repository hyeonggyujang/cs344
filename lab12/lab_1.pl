# a.
# Exercise 1.4
killer(butch).
husband(marsellus, mia).
wife(mia, marsellus). # The marriage() is eparatedly constructed because the relationship between two arguments is always one way, while we want 2-way relationship between two subjects.
dead(zed).
kills(marsellus, X):- footmassages(X, mia).
loves(mia, X):- good_dancer(X). # X is the variable used for a person, Y is the variable used for objects.
eats(jules, Y):-
	nutritious(Y);
	tasty(Y).
# 1. yes
# 2. no
# 3. no
# 4. no
# 5. yes
# 6. Y = ron
# 7. no

# b. 
# Prolog implements modus ponens with :- operator. 
# premise1(p):- premise2(q)
# premise2(q)
# if compute ?- premise1(q), then the output would be "yes".

# c. 
# Prolog clauses are generally more descriptive, while the propositional logic is more concise.
# Prolog clauses representationally advantageous in legibility.
# Propositional logic is advantageous in definition precision.

# d. 
# By putting a variable in the ?- command, Prolog could operate TELL.
# By putting an atom in the ?- command, Prolog could operate ASK.
