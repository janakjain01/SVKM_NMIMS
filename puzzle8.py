# ALGORITHM: 8 Puzzle using BFS (Breadth First Search)
# 1. Put the starting board in a queue and mark it visited.
# 2. Take the first board from the queue. If it is the goal, stop and return its moves.
# 3. Find the blank (0) and try moving it Up, Down, Left, Right (if inside the 3x3 grid).
# 4. Each move gives a new board. If it is not visited, mark it visited and add it to the queue.
# 5. Repeat until the goal is found. BFS guarantees the fewest moves.

from collections import deque

initial = (1, 2, 3, 5, 4, 7, 9, 8, 0)
goal = (1, 2, 3, 4, 5, 7, 8, 9, 0)

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}
    moves = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        z = state.index(0)
        r, c = divmod(z, 3)

        for dr, dc, move in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                lst = list(state)
                lst[z], lst[nz] = lst[nz], lst[z]
                nxt = tuple(lst)
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [move]))

solution = bfs(initial, goal)
print("BFS Solution:", solution)
print("Number of moves:", len(solution))
