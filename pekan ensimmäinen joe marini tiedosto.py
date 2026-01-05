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