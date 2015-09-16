-module(palindrome).

-export([check_palindrome/1, check_palindrome/0]).

check_palindrome(Input) when is_list(Input) ->
    Input0 = re:replace(string:to_upper(Input), "\\s+|\\W", "", [global,{return,list}]),
    Input1 = lists:reverse(Input0),
    if Input0 =:= Input1 -> io:format("Yes it's a palindrome\n");
       Input0 =/= Input1 -> io:format("Nope\n")
    end;
check_palindrome(_) ->
    io:format("Input must be a string\n").
check_palindrome() ->
    io:format("Expects one argument, a string\n").
