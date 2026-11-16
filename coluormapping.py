# ALGORITHM: Graph Colouring (Backtracking)
# 1. Take the next region that has no colour.
# 2. Try a colour. It is allowed only if no neighbour already has it.
# 3. If allowed, give it that colour and move to the next region.
# 4. If no colour works, go back to the previous region and change its colour.
# 5. Stop when every region has a colour.

# graph colouring
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
color_map = {}

def safe(r, c):
    for n in graph[r]:
        if color_map.get(n) == c:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    r = regions[0]
    for c in colors:
        if safe(r, c):
            color_map[r] = c
            if solve(regions[1:]):
                return True
            del color_map[r]
    return False

solve(list(graph))
print(color_map)
