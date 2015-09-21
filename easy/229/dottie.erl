-module(dottie).
-compile(export_all).

find_dottie(X) ->
    find_dottie(X, 0).

find_dottie(X, 100) ->
    X;
find_dottie(X, Count) ->
    find_dottie(math:cos(X), Count+1).
