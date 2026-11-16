# ======================================================================
# ALGORITHM: Depth First Search (DFS)
# ----------------------------------------------------------------------
# Idea: Go as deep as possible along one path before backtracking.
# Data structure: Recursion (implicit call stack) + a 'visited' set.
#
# Steps:
#   1. Start at the source node.
#   2. Mark the current node as visited and print/process it.
#   3. For each neighbour of the current node:
#        - If the neighbour is not visited, recursively call DFS on it.
#   4. When all neighbours are done, return (backtrack) to the caller.
#   5. Stop when the recursion returns from the source node.
#
# Time complexity : O(V + E)
# Space complexity: O(V)  (visited set + recursion stack)
# Expected output : 1 2 3 4 5 6 7
# ======================================================================

graph = {
    1: list((2, 5, 7)),
    2: list((3, 4)),
    3: [],
    4: list((3,)),
    5: list((4, 6)),
    6: [],
    7: list((6,)),
}
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
visited = set()
dfs(1, visited)
