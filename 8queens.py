# ALGORITHM: 8 Queens (Backtracking)
# 1. Place one queen in each row, starting from row 0.
# 2. For the current row, try each column from 0 to 7.
# 3. A column is safe if no earlier queen is in the same column or diagonal.
# 4. If safe, place the queen and go to the next row.
# 5. If no column is safe, go back to the previous row and move its queen.
# 6. Stop when 8 queens are placed.

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
