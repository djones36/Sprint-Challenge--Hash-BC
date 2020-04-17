#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)
'''

Plan:

What am I looking for?
weights = [] items weight
limit = limt of the items weight

will produce a tuple of the index pairs
it sumes up the integer pairs 

runs in linear time with a loop.
loop through the weights 
    limit - wieght[i] = difference
    find index

insert into hastable

have a check that if the pairs do not exist it returns none


'''


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)  # the size of the hash table. what we insert into
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        difference = hash_table_retrieve(ht, limit - weights[i])

        if difference is not None:
            return (difference, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
