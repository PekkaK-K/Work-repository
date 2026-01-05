# Example file for Advanced Python by Joe Marini
# Demonstrate how to use dictionary comprehensions

# define a list of temperature values
ctemps = [0, 12, 34, 100]

# Use a comprehension to build a dictionary
tempDict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
print(tempDict)
print(tempDict[12])

# Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}
newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
print(newTeam)

# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions
evenSquared = list(
    map(lambda e: e**2, filter(lambda e: e > 4 and e < 16, evens)))
print(evenSquared)

# Derive a new list of numbers frm a given list
evenSquared = [e ** 2 for e in evens]
print(evenSquared)

# Limit the items operated on with a predicate condition
oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]
print(oddSquared)

# Example file for Advanced Python by Joe Marini
# Sequence comparisons

import itertools


# define some lists
seq1 = [1, 2, 3, 6, 10, 15, 34, 56]
seq2 = [1, 2, 5, 7, 9, 18, 22, 38, 91]

# define a tuple
seq3 = (1, 2, 3, 6, 10, 15, 34, 56)

print(seq1 == seq2)
print(seq1 > seq2)
print(seq1 < seq2)

# sequences that have equal values but different number of items:
seq4 = [10, 20, 30]
seq5 = [10, 20, 30, 40, 50]

print(seq5 > seq4)

# Sequences must be of the same type to be compared
print(tuple(seq1) == seq3)

# use the all() function to compare two arbitrary sequences
print(all(x == y for x, y in itertools.zip_longest(seq1, seq3)))

# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# a slice is a subset of a sequence. The form is [start:stop:step]
print(names[1:4])

# using a step 
print(names[0:7:2])

# shorthand
print(names[:3])
print(names[5:])

# reversing with step of -1
print(names[::-1])

newnames = ["Andy", "Stanley", "Angela"]
names[2:4] = newnames
print(names)

# the del operator works with slices
del names[0:2]
print(names)

# not all sequence types support slicing, however
deque_names = deque(["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"])
for name in deque_names:
    print(name, " ", end="")
print()
print(len(deque_names))
print(deque_names[1:4]) # TypeError!

# Example file for Advanced Python by Joe Marini
# Demonstrate how to use set comprehensions

# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# build a set of unique Fahrenheit temperatures
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
ftemps2 = {(t * 9/5) + 32 for t in ctemps}
print(ftemps1)
print(ftemps2)

# build a set from an input source
sTemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in sTemp if not c.isspace()}
print(chars)