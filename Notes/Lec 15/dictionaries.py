''' Dictionary
Indexed by keys(can be anything that can be put in a set)
'''

actors={}
actors['Tom Hanks'] = 41
actors['Colin Hanks'] = 11

#Keys are anything that is hashable,they are stored as a set
#integers,strings,tuple,boolean
#Values in a dictionary can be anything
#you can delete a certain item or key with actors.del(),and you can pop an item with actors.pop()
#pop will remove the item and return it as a tuple,returns a random value,