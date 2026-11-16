# ALGORITHM: Breadth First Search (BFS)
# 1. Put the start node in a queue and mark it visited.
# 2. Take the first node out of the queue and print it.
# 3. Add all its unvisited neighbours to the end of the queue (mark them visited).
# 4. Repeat steps 2-3 until the queue is empty.

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
