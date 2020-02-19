#!/bin/python3
import collections 

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    word_file = open(dictionary_file, "r")
    words = []
    for word in word_file:

        words.append(word.strip("\n"))

    word_ladder = []
    
    word_ladder.append(start_word)

    que = collections.deque()

    que.appendleft(word_ladder)

    while que:
        current_stack = que.pop()
        for word in words:
            if _adjacent(current_stack[-1], word):
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                stack_copy = current_stack.copy()
                stack_copy.append(word)
                que.appendleft(stack_copy)

                words.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    >>> verify_word_ladder(['dog', 'fog', 'bog','hog'])
    True
    '''
    if not ladder:
        return False

    position = 0

    while position < (len(ladder) - 2):
        
        first_word = ladder[position]
        second_word = ladder[position + 1]
        status =  _adjacent(first_word, second_word)
        
        if status:
            position += 1
        else: 
            return False

    return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False

    count = 0 
    
    for i in range(len(word1)):  
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True

    return False

print(word_ladder('angel', 'child'))
