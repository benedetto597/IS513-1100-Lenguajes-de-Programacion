:- use_module(library(http/http_server)).

:- initialization
    http_server([port(8080)]).

:- http_handler(root(.),
                http_redirect(moved, location_by_id(say_hi)),
                []).
                
:- http_handler(root(home), say_hi, []).

/*
Iniciar servidor de forma manual
start_server(Port) :-
        http_server(http_dispatch, [port(Port)]).
*/

stop_server(Port) :-
        http_stop_server((Port),[]).

say_hi(Request) :-
	reply_html_page(
	   [title('Howdy')],
	    [\page_content(Request)]).
       
page_content(_Request) -->
	html(
	   [
  % these are html tags
	    h1('A Simple Web Page'),
  % if the argument is a list then it's elements are concatted
  % and list or no list you can nest tags
            p(['The ', b(first), ' paragraph']),
	    p(i('this is a para in italics with no list')),
  % with arity 2 the first is a k=v list of arguments
  % (and a side issue, the plain html version omits the closing tag,
  %  so we're large for a while)
	    p([style='font-size: 36pt', title='tooltip text'], 'With some text'),
  % Atoms are quoted, so the angle brackets are turned into entities
	    '<b>this wont be bold</b>',
  % - is used for format-argument_list
	    'this has ~w arguments that ends in ~w' - [2, onions],
  % A list preceeded by \ is literal material included.
  % this is useful for including 'normal' html
	    \['<i>in italic</i>', '<b>now we have bold</b>'],
  % You can do the format-argument_list trick with literal lists too
	    \['<i>~w</i>' - ['lemony fun']],
  % if you preceed a dcg with \ it's an included nonterminal
	    \some_included_stuff,
  % and you can use a term to pass arguments
	    \more_included_stuff('Whoop Whoop!'),
  % if your included stuff is in another moduled you have to include the
  % module. Because of the operator priorities you have to use parens here
  % You can include entities
            &(copy),
  % theres a bunch of handy syntax to construct attribute values.
  % You can use + to concatenate and - to do format-arglist
	    p([style='font-size: ' + '15pt',
	       title='another tooltip'], 'this has lots of attributes'),
  % you can urlencode query string members
   a([href='http:example.com?foo=' + encode('some value with & illegal chars')],
             'a link'),
   p('just to make links on diff line'),
  % Another way to do arguments
   a([href='http:example.com?' + [foo=7, bar='I need & urlencoded', baz=9]],
           'a link with more args'),
  % and just a list as a value becomes a space separated list.
  % this is useful for class lists
  p(class=[someclass, someotherclass], 'this has class'),
  % You can expand a location defined by an ID
  % (covered later) location_by_id(ID)
     % (I'll give example later when I cover this)
     %Falta poner el pre antes del code
     pre([style = ['background-color: #eee; padding:8px; border: 1px solid #999; display: block']], code("
         :- use_module(library(http/http_server)).

         :- initialization
            http_server([port(8080)]).

         :- http_handler(root(.),
                        http_redirect(moved, location_by_id(home_page)),
                        []).
                        
         :- http_handler(root(home), home_page, []).

         home_page(_Request) :-
            reply_html_page(
               title('Demo server'),
               [ h1('Hello world!'),
               span(class(product_class), 'Computers'),
               p(['This example demonstrates generating HTML ',
                                    'messages from Prolog'
                                    ])
                  
               ]).

      "))
	   ]).

some_included_stuff -->
	html([p('Some included stuff')]).

more_included_stuff(X) -->
	html([p(['More included stuff: ', b(X)])]).
