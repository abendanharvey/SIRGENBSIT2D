
from collections import deque

# Graph based on ABENDAN
# Repeated letters have unique keys:
# A1, A2, N1, and N2

graph = {
    "A1": ["B", "E"],
    "B": ["A1", "N1", "D"],
    "E": ["A1", "A2", "N2"],
    "N1": ["B", "D"],
    "D": ["B", "N1", "A2"],
    "A2": ["E", "D", "N2"],
    "N2": ["E", "A2"]
}

display_name = {
    "A1": "A",
    "B": "B",
    "E": "E",
    "N1": "N",
    "D": "D",
    "A2": "A",
    "N2": "N"
}


# Breadth-First Search
def graph_bfs(start):
    visited = []
    queue = deque([start])
    seen = {start}

    while queue:
        current = queue.popleft()
        visited.append(display_name[current])

        for neighbor in graph[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


# Depth-First Search
def graph_dfs(start):
    visited = []
    seen = set()

    def visit(current):
        seen.add(current)
        visited.append(display_name[current])

        for neighbor in graph[current]:
            if neighbor not in seen:
                visit(neighbor)

    visit(start)
    return visited


if __name__ == "__main__":
    print("=== GRAPH TRAVERSALS ===")
    print("BFS:", " -> ".join(graph_bfs("A1")))
    print("DFS:", " -> ".join(graph_dfs("A1")))
