#import numpy as np
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
def print_board(matrix,queens):
    for i,(x,y) in enumerate(queens):
        for a, mat in enumerate(matrix):
            for b, matt in enumerate(matrix):
                if(x == b and y == a):
                    matrix[a][b] = "1"
    print(matrix)  

def get_expression(size, queens=None):
    expression = []
    #matrix = np.array(np.zeros((size,size)))
    #print("Matrix preview")
    #print_board(matrix,queens)
    cols = []
    rows = []
    for q in queens:
        cols.append(q[0])
        rows.append(q[1])

    #check cols
    for x in range(size):
        clause = Clause(size)
        #Dans le cas ou aucune reine ne se situe sur cette col
        if x not in cols:
            # Clause avec seulement des positifs
            for y in range(size):
                clause.add_positive(x,y)
            # print("\nclause",clause)

            # Sous clause avec la negation de chacun des termes
            for y in range(size-1):
                for z in range(size-1):
                    # Ajouter les clauses sans doublons
                    if((x,y) != (x,z+1)):
                        clause2 = Clause(size)
                        clause2.add_negative(x,y)
                        clause2.add_negative(x,z+1)
                        expression.append(clause2)
                        # print("sous clause",clause2)

        # Dans le cas ou une reine se situe deja sur cette col
        else:
            for y in range(size):
                if (x,y) in queens:
                    clause.add_positive(x,y)
                else:
                    clause.add_negative(x,y)
            # print("\nclause",clause)
                
        expression.append(clause)
    print()

    print("#####\t Clauses by rows\t#####")
    #check rows
    for y in range(size):
        clause = Clause(size)
        #Dans le cas ou aucune reine ne se situe sur cette row
        if y not in rows:
            # Clause avec seulement des positifs
            for x in range(size):
                clause.add_positive(x,y)
            print("\nclause",clause)

            # Sous clause avec la negation de chacun des termes
            for x in range(size-1):
                for z in range(size-1):
                    # Ajouter les clauses sans doublons
                    if((x,y) != (z+1,y)):
                        clause2 = Clause(size)
                        clause2.add_negative(x,y)
                        clause2.add_negative(z+1,y)
                        expression.append(clause2)
                        print("sous clause",clause2)

        # Dans le cas ou une reine se situe deja sur cette row
        else:
            for x in range(size):
                if (x,y) in queens:
                    clause.add_positive(x,y)
                else:
                    clause.add_negative(x,y)
            print("\nclause",clause)
                
        expression.append(clause)
    print()
    
 
    # Check upper diagonal on left side
    # for y in range(size):
    #     for x in range(size):
    #         clause = Clause(size)
    #         for i, j in zip(range(x, -1, -1),
    #                         range(y, -1, -1)):
    #             if (i,j) in queens:
    #                 clause.add_positive(x,y)
    #             else:
    #                 clause.add_negative(x,y)
    #         # print("clause",clause)
    #         expression.append(clause)

    # Check lower diagonal on left side
    # for y in range(size):
    #     for x in range(size):
    #         clause = Clause(size)
    #         for i, j in zip(range(x, size, -1),
    #                         range(y, -1, -1)):
    #             if (i,j) in queens:
    #                 clause.add_positive(x,y)
    #             else:
    #                 clause.add_negative(x,y)
    #         # print("clause",clause)
    #         expression.append(clause)
    return expression


if __name__ == '__main__':
    expression = get_expression(3)
    for clause in expression:
        print(clause)
