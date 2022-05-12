import numpy as np
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
    matrix = np.array(np.zeros((size,size)))
    print("Matrix preview")
    print_board(matrix,queens)
    cols = []
    rows = []
    for q in queens:
        cols.append(q[0])
        rows.append(q[1])

    # Clause avec seulement des positifs
    for x in queens:
        oneclause = Clause(size)
        oneclause.add_positive(x[0],x[1])
        expression.append(oneclause)
        print("\nclause",oneclause)

    print("#####\t Clauses by cols\t#####")

    #check cols
    for x in range(size):
        clauseCol = Clause(size)
        #Dans le cas ou aucune reine ne se situe sur cette col
        if x not in cols:
            # Clause avec seulement des positifs
            for y in range(size):
                clauseCol.add_positive(x,y)
            print("\nclause",clauseCol)

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
        else:
            for y in range(size):
                if (x,y) not in queens:
                    oneclause = Clause(size)
                    oneclause.add_negative(x,y)
                    expression.append(oneclause)
                    print("\nclause",oneclause)
                
        expression.append(clauseCol)

    print("#####\t Clauses by rows\t#####")
    #check rows
    for y in range(size):
        clauseRow = Clause(size)
        #Dans le cas ou aucune reine ne se situe sur cette row
        if y not in rows:
            # Clause avec seulement des positifs
            for x in range(size):
                clauseRow.add_positive(x,y)
            print("\nclause",clauseRow)

            # Sous clause avec la negation de chacun des termes
            for x in range(size-1):
                for z in range(size-1):
                    # Ajouter les clauses sans doublons
                    if((x,y) != (z+1,y)):
                        clause2 = Clause(size)
                        clause2.add_negative(x,y)
                        clause2.add_negative(z+1,y)
                        expression.append(clause2)
                        # print("sous clause",clause2)
        else:
            for x in range(size):
                if (x,y) not in queens:
                    oneclause = Clause(size)
                    oneclause.add_negative(x,y)
                    expression.append(oneclause)
                    print("\nclause",oneclause)

        expression.append(clauseRow)
    print()
    print("#####\t Clauses by diags \t#####")
    
    for x in range(size):
        # check upper diag from top-left to bottom-right
        if x != 0:
            for (a,b) in zip(range(size),range(x,size,1)):
                for (i,j) in zip(range(size),range(x+1,size,1)):
                    print(i,j)
                print()
    #             # clauseDiag = Clause(size)
    #             # clauseDiag.add_negative(i,j)
    #             # clauseDiag.add_negative(i,j+1)
    #             # expression.append(clauseDiag)
    #             # print('clause upper right\t',clauseDiag)

        # check lower diag from top-right to bottom-left
            for (i,j) in zip(range(x,size,1),range(size-1,-1,-1)):
    #             for z in range(size-1):
    #                 if((i,j) != (i,z+1)):
                        clauseDiag1 = Clause(size)
    #                     clauseDiag1.add_negative(i,j)
    #                     clauseDiag1.add_negative(i,z+1)
    #                     expression.append(clauseDiag1)
                        print('clause lower right\t',clauseDiag1)

    for x in range(size):
    #     # check upper diag from top-right to bottom-left
        for (i,j) in zip(range(size),range(size-x-1,-1,-1)):
    #         for z in range(size-1):
    #             if((i,j) != (i,z+1)):
                    clauseDiag2 = Clause(size)
    #                 clauseDiag2.add_negative(i,j)
    #                 clauseDiag2.add_negative(i,z+1)
    #                 expression.append(clauseDiag2)
                    print('clause upper left\t',clauseDiag2)

    #     # check lower diag from top-left to bottom-right
        for (i,j) in zip(range(x,size,1),range(size)):
    #         for z in range(size-1):
    #             if((i,j) != (i,z+1)):
                    clauseDiag3 = Clause(size)
    #                 clauseDiag3.add_negative(i,j)
    #                 clauseDiag3.add_negative(i,z+1)
    #                 expression.append(clauseDiag3)
                    # print('clause lower left\t',clauseDiag3)

    return expression


if __name__ == '__main__':
    expression = get_expression(3)
    for clause in expression:
        print(clause)
