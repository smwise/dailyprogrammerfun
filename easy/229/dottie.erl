-module(dottie).
-export([find_dottie/1, find_pi/1, find_golden_ratio/1,
         find_logistics_map/1]).

%% defining the calculations
dottie_fun(X) -> math:cos(X).
pi_fun(X) -> X - math:tan(X).
golden_fun(X) -> 1 + 1/X.
logistics_fun(X) -> 4*X*(1-X).

%% boiler plate function that gets passed the function
%% to use to calculate the next value of X
find_fixed_point(X, _, 100) ->
    X;
find_fixed_point(X, Manip, Count) ->
    find_fixed_point(Manip(X), Manip, Count+1).

%% Main problem, cos(x)
%% Passes in dottie_fun/1
find_dottie(X) ->
    find_fixed_point(X, fun dottie_fun/1, 0).

%% Bonus #1, fixed point of x-tan(x)
%% Uses pi_fun
find_pi(X) ->
    find_fixed_point(X, fun pi_fun/1, 0).

%% Bonux #2, fixed point of 1 + 1/x
find_golden_ratio(X) ->
    find_fixed_point(X, fun golden_fun/1, 0).

%% Bonus #3, 4X(1-X) don't know what this one is
find_logistics_map(X) ->
    find_fixed_point(X, fun logistics_fun/1, 0).
