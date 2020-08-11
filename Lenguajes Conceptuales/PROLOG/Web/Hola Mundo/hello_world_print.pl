:- use_module(library(http/http_server)).

:- initialization
    http_server([port(8080)]).

:- http_handler(root(.),
                http_redirect(moved, location_by_id(home_page)),
                []).
                
:- http_handler(root(home), home_page, []).
home_page(_Request) :-
        format('Content-type: text/html~n~n'),
        format('<html>
                        <head>
                                <h1 style="color: #3A4593; text-align: center;"> Creación de Aplicaciones Web usando Prolog y SWI-Prolog </h1>
                             
                                <h3> Alumno </h3>
                                <h3> Lenguajes de programación </h3>
                                <h3> Jose Manuel Inestroza </h3>
                                <h3> Universidad Nacional Autonoma de Honduras</h3>
                        </head>
                </html>~n').