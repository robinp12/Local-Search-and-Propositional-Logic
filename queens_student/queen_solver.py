from clause import *

"""
For the queen problem, the only code you have to do is in this file.

You should replace

# your code here

by a code generating a list of clauses modeling the queen problem
for the input file.

You should build clauses using the Clause class defined in clause.py

Read the comment on top of clause.py to see how this works.
"""


def get_expression(size, queens=None):
    expression = []
    # your code here

    return expression


if __name__ == '__main__':
    expression = get_expression(3)
    for clause in expression:
        print(clause)
