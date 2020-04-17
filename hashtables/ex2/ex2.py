#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)
'''
Question?
Write a function `reconstruct_trip` to reconstruct your trip from your mass of flight tickets. Each ticket is represented as a Class

source = starting airport
destination = next airport

run in linear time

input is [tickets] and length
output is an array of strings the the trips route in order

They link is the Destination of previous ticket and the source of the next ticket

Solution:
loop through the array of tickets and instert into the hashtable

access the first flight from the hashtable if its source is none then its the first flight

find the next flight by checking the value of the previous ticket with the key of the next ticket.

'''


class Ticket:
    def __init__(self, source, destination):
        # starting
        self.source = source
        # next
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert all tickets in a hash table
    for new_ticket in tickets:
        hash_table_insert(hashtable, new_ticket.source, new_ticket.destination)

    # manually insert first ticket since its location is none.
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # insert tickets in order, skipping first
    # doing the order by the pervious distanation
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    return route[:-1]
