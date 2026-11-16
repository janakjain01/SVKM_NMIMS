# ALGORITHM: Depth First Search (DFS)
# 1. Start at node 1 and mark it visited.
# 2. Go to an unvisited neighbour and repeat (keep going deeper).
# 3. If there are no unvisited neighbours, go back to the previous node.
# 4. Stop when you are back at the start with nothing left to visit.

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
