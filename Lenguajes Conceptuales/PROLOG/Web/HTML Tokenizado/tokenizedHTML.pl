:- use_module(library(http/http_server)).
:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_error)).
:- use_module(library(http/html_write)).
:- initialization
    http_server([port(8080)]).

:- http_handler(root(.),
                http_redirect(moved, location_by_id(say_hi)),
                []).
                
:- http_handler(root(home), say_hi, []).
/* The implementation of /. The single argument provides the request
details, which we ignore for now. Our task is to write a CGI-Document:
a number of name: value -pair lines, followed by two newlines, followed
by the document content, The only obligatory header line is the
Content-type: <mime-type> header.
Printing is done with print_html, which takes a list of tokens and
prints them. It attempts to 'reasonably' format html when it recognizes
tags. */

say_hi(_Request) :-
	phrase(
	    my_nonterm,
	    TokenizedHtml,
	    []),
        format('Content-type: text/html~n~n'),
	print_html(TokenizedHtml).

my_nonterm -->
	html([html([head([title('Howdy')]),
	           body([h1('A Simple Web Page'),
		      p('With some text')])])]).