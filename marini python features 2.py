# Example file for Advanced Python by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# the assignment operator is part of an expression
(x := 10)
print(x)

# The assignment expression is useful for writing concise code
while (thestr := input("value? ")) != "exit":
    print(thestr)

# The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l
}
pprint.pp(val_data)

# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything special.

    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: the second argument. Defaults to None. Whatever makes you happy.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()

# Example file for Advanced Python by Joe Marini
# using the print() and pprint() functions

import pprint
from dataclasses import dataclass

# The print() function has useful parameters to help you format
# output for increased readability
# basic print() function
values=["one", "two", "three", "four", "five"]
print(*values)

# use the 'sep' argument to control the separator between values:
print(*values, sep=' -- ')

# use the 'end' argument to control the line ending characters
# let's auto-print the current line number along with each item
for i in range(0, len(values)):
    print(values[i], end=f" [line: {str(i+1)}]\n")

# you can even redirect print() output to a file:
# newfile = open("output.txt","w")
# print(*values, sep=' -- ', file=newfile, flush=True)
# newfile.close()


# pprint() can be used to print more complex data 
# in a format that is more readable
worldcupdata = [
    { "game": "Final", "Attendance" : 88966, "Argentina" : "3 (4)", "France" : "3 (2)" },
    { "game": "3rd Place", "Attendance" : 44137, "Croatia" : 2, "Morocco" : 1},
    { "game": "Semifinal", "Attendance" : 68294, "France" : 2, "Morocco" : 0},
    { "game": "Semifinal", "Attendance" : 88966, "Argentina" : 3, "Croatia" : 0}
]

pprint.pp(worldcupdata, indent=3, width=40, underscore_numbers=True)

# pprint also works on newer complex structures, like dataclasses!
@dataclass
class wcdata:
    game: str
    attendance: int
    team1: str
    team2: str
    score: str

worldcupdata2 = [
    wcdata("Final", 88966, "Argentina" , "France" , "3 (4) -- 3 (2)" ),
    wcdata("3rd Place", 44137, "Croatia" , "Morocco" , "2 -- 1" ),
    wcdata("Semifinal", 68294, "France" , "Morocco" , "2 -- 0" ),
    wcdata("Semifinal", 88966, "Argentina" , "Croatia" , "3 -- 0" ),
]
pprint.pp(worldcupdata2);

# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope
x = 1

# define a local function with a variable "x"
def test():
    global x
    x = 10
    print(x)

# Run the test function and observe the two results
test()
print(x)

x = x + 5
print(x)
test()


# Nested functions create inner scopes. These are called closures:
def multiplier_maker(factor):
    def multiply(num):
        return num * factor
    return multiply

doubler = multiplier_maker(2)
tripler = multiplier_maker(3)

print(doubler(10))
print(doubler(15))
print(tripler(10))
print(tripler(15))

# Example file for Advanced Python by Joe Marini
# Using special module names

import collections


# __name__ is the name of the module
print("Module name:", __name__)

# __file__ contains the path to the file from which the module was loaded
print("File path:", __file__)

# __package__ indicates the package that the module belongs to.
print("Package:", __package__)
print(collections.__package__)

if __name__ == "__main__":
    print("This module is being run directly.")