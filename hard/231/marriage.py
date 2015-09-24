'''
For a set of men {A,B,...,Z} and a set of women {a,b,...,z} they have a
preference table - A would prefer to marry b, but will be satisfied to marry c;
c would prefer to marry B, will be OK to marry C, etc. Matches are considered
unstable if there exists a pair who likes each other more than their spouses.
The challenge is then to construct a stable set of marriages given the
preferences.

Sample input:
    A, b, c, a
    B, b, a, c
    C, c, a, b
    a, C, B, A
    b, A, C, B
    c, A, C, B

"The Gale–Shapley algorithm involves a number of "rounds" (or "iterations"). In
the first round, first a) each unengaged man proposes to the woman he prefers
most, and then b) each woman replies "maybe" to her suitor she most prefers and
"no" to all other suitors. She is then provisionally "engaged" to the suitor she
most prefers so far, and that suitor is likewise provisionally engaged to her.
In each subsequent round, first a) each unengaged man proposes to the
most-preferred woman to whom he has not yet proposed (regardless of whether the
woman is already engaged), and then b) each woman replies "maybe" to her suitor
she most prefers (whether her existing provisional partner or someone else) and
rejects the rest (again, perhaps including her current provisional partner). The
provisional nature of engagements preserves the right of an already-engaged
woman to "trade up" (and, in the process, to "jilt" her until-then partner).
This process is repeated until everyone is engaged."
-https://en.wikipedia.org/wiki/Stable_marriage_problem
'''

import sys

def find_stable_marriages(preferences, partners):
    matches = {}
    free_men = [man for man in partners if man.isupper()]
    free_women = [woman for woman in partners if woman.islower()]
    while len(free_men) > 0:
        man = free_men[0]
        # get the next preferred woman
        woman = preferences[man].pop(0)

        # get her preferences
        female_preferences = preferences[woman]

        # both are unattached
        if woman in free_women:
            # add to match, removing from free men in the process
            matches[woman] = man
            # remove the woman from free women
            free_women.remove(woman)
            free_men.remove(man)
        # woman is already paired off but likes this guy more
        elif female_preferences.index(man) < \
                female_preferences.index(matches.get(woman)):
            # add previous guy back to free men
            free_men.append(matches.get(woman))
            # update couples and remove new guy from free men
            matches[woman] = man
            free_men.remove(man)
    return matches

def main():
    #read input
    if len(sys.argv) == 1:
        print("include input file")
        return
    File = sys.argv[1]
    preferences = {}
    partners = []
    raw_preferences = open(File, 'r')
    for line in raw_preferences:
        pref_list = line.strip("\n").split(", ")
        person = pref_list[0]
        partners.append(person)
        preferences[person] = pref_list[1:]
    pairs = find_stable_marriages(preferences, partners)
    print(pairs)

main()
