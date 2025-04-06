def is_safe(vertex, graph, color, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, k, color, vertex, n):
    if vertex == n:
        return True

    for c in range(1, k + 1):
        if is_safe(vertex, graph, color, c):
            color[vertex] = c
            if graph_coloring(graph, k, color, vertex + 1, n):
                return True
            color[vertex] = 0
    return False

def main():
    # Read from file
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    n, m, k = map(int, lines[0].split())
    edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]

    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize color assignment
    color = [0] * n

    if graph_coloring(graph, k, color, 0, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring NOT possible with {k} Colors")

if __name__ == "__main__":
    main()
