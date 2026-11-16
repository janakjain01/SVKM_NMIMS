# ======================================================================
# ALGORITHM: Minimax with Alpha-Beta Pruning
# ----------------------------------------------------------------------
# Idea: Minimax picks the best move in a two-player game tree, where
#       MAX tries to maximise the score and MIN tries to minimise it.
#       Alpha-Beta pruning skips branches that cannot affect the final
#       decision, giving the same result with fewer evaluations.
#
# Terms:
#   alpha (a) = best value MAX can guarantee so far (starts at -inf)
#   beta  (b) = best value MIN can guarantee so far (starts at +inf)
#
# Steps:
#   1. If the leaf level is reached (depth == 3), return the leaf value.
#   2. If it is MAX's turn: best = -inf; otherwise best = +inf.
#   3. For each child:
#        a. Recursively evaluate it with the turn flipped.
#        b. MAX node: best = max(best, value); alpha = max(alpha, best)
#           MIN node: best = min(best, value); beta  = min(beta, best)
#        c. PRUNE: if beta <= alpha, stop exploring the remaining
#           children (they cannot change the outcome).
#   4. Return best.
#
# Tree here: binary, depth 3, 8 leaf values in list v.
# Time complexity : O(b^(d/2)) best case, O(b^d) worst case
# Expected output : Optimal Value: 5
# ======================================================================

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
