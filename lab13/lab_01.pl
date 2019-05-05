# a.
#   i.
directlyIn(katrina, olga)
directlyIn(olga, natasha)
directlyIn(natasha, irina)

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z),
            in(Z, Y).

#   ii.
tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

trantran ([], []).

trantran([X|Y], [G|E]) :-
            tran(X, G),
            trantran(Y, E).


# b. Prolog can implement a generalized version of Modus Ponens.
#           For example,

mortal(X) :- human(X).
human(socrates).

# such that,

?- mortal(socrates)

#returns true.
