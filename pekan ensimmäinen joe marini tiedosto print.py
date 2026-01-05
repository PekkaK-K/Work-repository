# Example file for Advanced Python by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# the assignment operator is part of an expression


# The assignment expression is useful for writing concise code


# The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
l = len(values)
s = sum(values)
val_data = {
    "length": l,
    "total": s,
    "average": s/l
}

# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
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


# use the 'end' argument to control the line ending characters
# let's auto-print the current line number along with each item


# you can even redirect print() output to a file:


# pprint() can be used to print more complex data 
# in a format that is more readable
worldcupdata = [
    { "game": "Final", "Attendance" : 88966, "Argentina" : "3 (4)", "France" : "3 (2)" },
    { "game": "3rd Place", "Attendance" : 44137, "Croatia" : 2, "Morocco" : 1},
    { "game": "Semifinal", "Attendance" : 68294, "France" : 2, "Morocco" : 0},
    { "game": "Semifinal", "Attendance" : 88966, "Argentina" : 3, "Croatia" : 0}
]


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

