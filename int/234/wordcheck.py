import sys

'''
Looking for location where word diverges from any options

Expects as arguments (in order): list of words to check, input to build
    dictionary from
'''

def check_word(word, word_dict):
    '''
    same traversal method as in setup
    '''
    path = word_dict
    location = 0
    for (index, letter) in enumerate(word):
        if not path:
            location = index
            break
        path = path.get(letter)
    return word[:location] + "<" + word[location:] if location < len(word)-1 \
        else word

def setup_trie(word_dict):
    '''
    doing this for the sake of setting up a basic trie
    '''
    trie = {}
    for word in word_dict:
        current_branch = trie
        for letter in word.strip():
            current_branch = current_branch.setdefault(letter, {})
        current_branch[0] = 0
    return trie

def main():
    word_input = open(sys.argv[1])
    word_dict = setup_trie(open(sys.argv[2]))
    for word in word_input:
        print(check_word(word.strip(), word_dict))

if __name__ == "__main__":
    main()
