
from collections import deque

# Binary Tree based on ABENDAN
#             A
#           /   \
#          B     E
#         / \   / \
#        N   D A   N

binary_tree = {
    "A": ["B", "E"],
    "B": ["N", "D"],
    "E": ["A_left", "N_right"],
    "N": [],
    "D": [],
    "A_left": [],
    "N_right": []
}

display_name = {
    "A": "A",
    "B": "B",
    "E": "E",
    "N": "N",
    "D": "D",
    "A_left": "A",
    "N_right": "N"
}


# Breadth-First Search
def tree_bfs(root):
    visited = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        visited.append(display_name[current])

        for child in binary_tree[current]:
            queue.append(child)

    return visited


# Depth-First Search
def tree_dfs(root):
    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        visited.append(display_name[current])

        for child in reversed(binary_tree[current]):
            stack.append(child)

    return visited


if __name__ == "__main__":
    print("=== BINARY TREE TRAVERSALS ===")
    print("BFS:", " -> ".join(tree_bfs("A")))
    print("DFS:", " -> ".join(tree_dfs("A")))
