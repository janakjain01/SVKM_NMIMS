# ======================================================================
# ALGORITHM: 8 Queens Problem using Backtracking
# ----------------------------------------------------------------------
# Goal: Place 8 queens on an 8x8 chessboard so that no two queens
#       attack each other (no shared row, column, or diagonal).
#
# Representation: A tuple c where c[i] = column of the queen in row i.
#
# Steps:
#   1. If c already has 8 queens, a full solution is found -> return it.
#   2. For the next row (len(c)), try every column x from 0 to 7.
#   3. A column x is SAFE if, for every earlier queen (row i, column y):
#        - x != y                      (not in the same column)
#        - abs(x - y) != len(c) - i    (not on the same diagonal)
#      (Rows never clash because one queen is placed per row.)
#   4. If safe, place the queen (c + (x,)) and recurse to the next row.
#   5. If the recursion returns a solution, pass it up.
#      Otherwise BACKTRACK and try the next column.
#   6. If no column works in this row, return None so the previous row
#      moves its queen.
#
# Time complexity : O(N!) worst case (heavily reduced by pruning)
# Output          : First solution found, drawn as an 8x8 board
#                   ('Q' = queen, '.' = empty square)
# ======================================================================

# 8 queens problem
def q8(c=()):
    if len(c) == 8:
        return c
    for x in range(8):
        if all(x != y and abs(x - y) != len(c) - i for i, y in enumerate(c)):
            r = q8(c + (x,))
            if r:
                return r


print("\nA solution to the 8 Queens problem:\n")
for x in q8():
    print(" ".join("Q" if j == x else "." for j in range(8)))
