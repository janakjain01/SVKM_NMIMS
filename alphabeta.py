# ALGORITHM: Alpha-Beta Pruning (game tree search)
# 1. MAX player picks the biggest value, MIN player picks the smallest.
# 2. Go down the tree to the leaves and read their values.
# 3. Come back up, choosing max or min at each level.
# 4. alpha = best score MAX has found so far, beta = best score MIN has found so far.
# 5. If beta <= alpha, skip the remaining children (they cannot change the answer).

#alpha beta pruning
def ab(d, n, maxp, v, a, b):
    if d == 3:
        return v[n]

    best = float('-inf') if maxp else float('inf')

    for i in range(2):
        x = ab(d + 1, n * 2 + i, not maxp, v, a, b)

        if maxp:
            best = max(best, x)
            a = max(a, best)
        else:
            best = min(best, x)
            b = min(b, best)

        if b <= a:
            break

    return best


v = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal Value:", ab(0, 0, True, v, float('-inf'), float('inf')))
