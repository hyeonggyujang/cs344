witch(X):- burn(X).
burn(X):- wood(X).
floats(X):-
	wood(X);
	duck(X).
wood(X):- weighs_the_same_as_duck(X).
weighs_the_same_as_duck(person)

# ?- witch(person)