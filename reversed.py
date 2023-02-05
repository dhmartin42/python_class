# an iterable is anythinf you can loop over using a for loop
# e.g.: lists, tuples, strings, sets, and dictionaries
# a sequence seq() is a subset of iterabels that have a length, 
# index, and you can sliced them.
# e.g: strings, lists, tuples. 
# iterables that are not sequences: dictionaries, sets, files, generators
# every sequenc in pythin has a reverse function

countries = ['Netherlands','Nigeria','Jordan','Nepal','Niger','Japan']
countries.reverse() # lost original ordering
countries[::-1]

# reversed() returns an iterator that counts backwards
for country in reversed(countries):
    print(country)

reversed_countries = list(reversed(countries)) # doesn't make copies just returns an iterator that is reversed
print(reversed_countries)

# the reverse() method creates a copy of the object and reverses it, where
# reversed() returns an iterator that is reversed. it doesn't modify the original 
# item and it is much faster

#reverse(): reverses a mutable sequence in place     not available for immutable sequences
#Slicing[::-1]: creates a reversed copy of a sequence      fastest, but makes a copy fo the sequence, memory considerations to reverse millions of items, used for both mutable and immutable sequences
#reversed(): returns a reverse iterator     scales well to millions of items used for both mutable and immutable sequences
