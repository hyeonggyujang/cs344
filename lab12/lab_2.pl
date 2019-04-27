# a.
# i.
# 	1. yes
# 	2. no
# 	8. yes, X = bread
# 	9. yes, X = sausage, Y = bread
# 	14. no
# ii. 
#	1. not satisfied. 
#	2. not satisfied.
#	3. not satisfied.
#	4. satisfied.
#	5. satisfied.
#	Prolog creates a proof search tree by assigning each unique input variable with a specific value followed by an underscore. Then with that value, Prolog verifies whether each functor is true until it finds a solution or until all of its functors run out.

# b.
# It doesn't seem to utilize unification as Prolog does. Unification becomes practically useful when it's used with variables, but in propositional logic, variables are not used. 

# c.
# Prolog uses resolution. To provides a resolution for a given query, Prolog creates a search tree for proving.
