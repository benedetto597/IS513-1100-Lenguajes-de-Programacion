/*
    Graph
    @author Edgar Benedetto
    @date 2020/07/30
    @version 0.1
*/

%Hechos
edge(0,1,1).
%Hay una arista entre el estado 0 y el estado 1 y su dimensión es 1
edge(1,5,1).
edge(1,2,1).
edge(2,6,1).
edge(2,3,1).

%Reglas
connected(X,Y) :- 
    edge(X,Y,1);
    edge(Y,X,1).

/*
    Como las reglas no permiten retornar, se debe mandar como parametro una varible
    que contendrá la respuesta del problema
*/

path(A,B,Path):-    
    %Guardar en una lista los nodos visitados
    %En la variable Q se guarda el resultado de travel
    travel(A,B,[A],Q),
    %Se debe dar vuelta a la lista dado que viene como 15, 7, 3, 2, 1, 0
    reverse(Q, Path).

/* 
    Caso Final
    EL salto de A a B para unos visitados en especifico con una ruta
    cuando se cumpla esa condición final es cuando se verifica si 
    A y B están conectados
*/
travel(A,B,P,[B|P]):-
    connected(A,B).

%Buscar Ruta entre A y B
travel(A,B,Visited,Path):-
    %Metodo recursivo
    %C es nodo conectado a A
    connected(A,C),

    %C es distinto a B
    C \== B,
    
    %C no es miembro de los visitados
    \+member(C,Visited),

    /*
        Solo cuando se cumpla todo lo anterior se seguira navegando en ese nodo C
        Para buscar el nodo B y se guarda a C al inicio de los visitados
    */
    %Seguir navegando en ese nodo C para buscar el nodo B
    travel(C,B[C|Visited],Path).