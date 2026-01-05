# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
for d in days:
    print(d)

# use iter() to create an iterator over a collection
# the next() function retrieves the next value from an iterator
i = iter(days)
print(next(i))  # Sun
print(next(i))  # Mon
print(next(i))  # Tue

# iterate using a function and a sentinel
with open("testfile.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)

        # Example file for Advanced Python by Joe Marini
# The for-else loop construct

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# The else clause on a for loop is only executed if the loop completes every iteration
def findname(target):
    for name in names:
        if name == target:
            print("Name found");
            return True
    else:
        print("Name not found")
        return False

print(findname("Creed"))
print(findname("Tom"))

# Check if a number is prime

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

is_prime(31)
is_prime(56)

# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
cycler = itertools.cycle(names)
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))


# use count to create a simple counter
counter = itertools.count(100, 10)
print(next(counter))
print(next(counter))
print(next(counter))


# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]
acc = itertools.accumulate(vals, max)
print(list(acc))


# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
update = lambda balance, payment: round(1.04 * balance) - payment
balances = itertools.accumulate(payments, update, initial=2_000)
print(list(balances))

# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
x = itertools.chain("ABCD", "1234")
print(list(x))

# make a prepend function
def prepend(val, iterable):
    return itertools.chain([val], iterable)

result = prepend(5, [1, "A", True, 10])
print(list(result))

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']
result = itertools.chain.from_iterable([s1,s2,s3])
print(list(result))

# Example file for Advanced Python by Joe Marini
# Itertools: dropwhile, takewhile, filterfalse

import itertools
import pprint
from dataclasses import dataclass


vals = [10, 20, 30, 40, 50, 40, 30, 25, 55, 45, 40, 30]

# dropwhile and takewhile will return values until
# a certain condition is met that stops them
def testFunction(x):
    return x < 40

# dropwhile() drops values until the predicate expression is True
result = list(itertools.dropwhile(testFunction, vals))
print(result)

# takewhile() is the opposite of dropwhile() - it returns values from
# the iterable while the predicate is True, then stops
result = list(itertools.takewhile(testFunction, vals))
print(result)

# filterfalse() returns elements from the iterable for which the predicate
# function returns False. 
result = list(itertools.filterfalse(lambda x: x % 2 == 0, vals))
print(result)

# These functions can work on complex objects
@dataclass
class wcdata:
    game: str
    attendance: int
    team1: str
    team2: str
    score: str

worldcupdata = [
    wcdata("Final", 88966, "Argentina" , "France" , "3 (4) -- 3 (2)" ),
    wcdata("3rd Place", 44137, "Croatia" , "Morocco" , "2 -- 1" ),
    wcdata("Semifinal", 68294, "France" , "Morocco" , "2 -- 0" ),
    wcdata("Semifinal", 88966, "Argentina" , "Croatia" , "3 -- 0" ),
]

result = list(itertools.filterfalse(lambda x: x.attendance < 80000, worldcupdata))
pprint.pp(result)

# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(cards, suits))
print(len(deck), "cards")
print(deck)


# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")
result = itertools.permutations(teams, 2)
print(list(result))


# combinations() will create combinations of a given length with no repeats
result = itertools.combinations("ABCD", 3)
print(list(result))


# combinations_with_replacement() will create combinations of a given length with repeats
result = itertools.combinations_with_replacement("ABCD", 3)
print(list(result))

# Example file for Advanced Python by Joe Marini


import itertools

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# the enumerate function
for i, m in enumerate(days, start=1):
    print(i, m)

# use zip to combine sequences
for m in zip(days, daysFr):
    print(m)

# use enumerate and zip together
for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], "=", m[1], "in French")

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="-")
print("Result: ")
for item in result:
    print(item)
    
    