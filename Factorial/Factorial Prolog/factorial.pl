/*
    Factorial
    @author Edgar Benedetto
    @date 2020/07/30
    @version 0.1
*/

%Reglas
factorial(0,1).
%El factorial de 0 es 1 

factorial(N, Respuesta) :-
    N > 0, 
    
    %Mientras N sea mayor que 0 se crea la variable Nmenos1
    Nmenos1 is N - 1,
    factorial(Nmenos1,RespuestaNmenos1),

    %Se debe ir guardando la respuesta
    Respuesta is RespuestaNmenos1 * N.

%En consola factorial(0,X) o factorial(1,X) o factorial(2,X)...