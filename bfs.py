# ======================================================================
# ALGORITHM: Breadth First Search (BFS)
# ----------------------------------------------------------------------
# Idea: Visit all nodes at the current level (distance) before moving
#       to the next level.
# Data structure: Queue (FIFO) + a 'visited' set.
#
# Steps:
#   1. Create an empty queue; mark the source node visited and enqueue it.
#   2. While the queue is not empty:
#        a. Dequeue the front node (current) and print/process it.
#        b. For each neighbour of current:
#             - If not visited, mark it visited and enqueue it.
#   3. Stop when the queue becomes empty.
#
# Time complexity : O(V + E)  (note: list.pop(0) is O(n); use
#                   collections.deque for a true O(1) dequeue)
# Space complexity: O(V)
# Expected output : 1 2 5 7 3 4 6
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
def bfs(node, visited):
  queue = []
  visited.add(node)
  queue.append(node)
  while queue:
      current = queue.pop(0)
      print(current, end=" ")
      for neighbor in graph[current]:
          if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
visited = set()
bfs(1, visited)
