/*
    Family Tree
    @author Edgar Benedetto
    @date 2020/07/30
    @version 0.1
*/

%Hechos
mujer('Gabriela').
mujer('Rosa Maria').
hombre('Alexis').
hombre('David').
hombre('Edgar').

progenitor/a('Alexis', 'Rosa Maria').
progenitor/a('Gabriela', 'Rosa Maria').
progenitor/a('Alexis', 'David').
progenitor/a('Gabriela', 'David').
progenitor/a('Alexis', 'Edgar').
progenitor/a('Gabriela', 'Edgar').

/* 
    Para que alguien sea madre, tienen que ser progenitor y mujer
    Para que alguien sea padre, tienen que ser progenitor y hombre
    Para que alguien sea hermano, tienen que tener los mismos padres y ser hombre
    Para que alguien sea hermana, tienen que tener los mismos padres y ser mujer
*/

%Reglas
madre(X,Y):- 
    progenitor/a(X,Y),
    mujer(X).

padre(X,Y):- 
    progenitor/a(X,Y),
    hombre(X).

hermano(X,Y):-
    madre(A,X),
    padre(B,X),
    madre(C,Y),
    padre(D,Y),
    A == B,
    C == D,
    hombre(X).

hermana(X,Y):-
    madre(A,X),
    padre(B,X),
    madre(C,Y),
    padre(D,Y),
    A == B,
    C == D,
    mujer(X).
