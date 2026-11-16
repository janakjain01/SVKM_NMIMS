# ======================================================================
# ALGORITHM: Graph Colouring (Map Colouring) using Backtracking
# ----------------------------------------------------------------------
# Goal: Assign a colour to every region (node) so that no two adjacent
#       regions share the same colour, using at most the given colours.
#
# Steps:
#   1. If no regions are left to colour, a valid solution is found
#      (base case) -> return True.
#   2. Pick the next uncoloured region r.
#   3. Try each colour c from the colour list:
#        a. SAFE check: c is allowed only if no neighbour of r already
#           has colour c.
#        b. If safe, assign c to r and recursively colour the
#           remaining regions.
#        c. If the recursive call succeeds, return True.
#        d. Otherwise BACKTRACK: remove the colour from r and try the
#           next colour.
#   4. If no colour works for r, return False (forces the previous
#      region to change its colour).
#
# Time complexity : O(m^V) worst case (m colours, V regions)
# Expected output : {'A': 'Red', 'B': 'Green', 'C': 'Blue', 'D': 'Red'}
# ======================================================================

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
