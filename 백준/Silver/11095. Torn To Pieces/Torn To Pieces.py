def find_route(graph, start, end):
    visited = set()
    path = []

    def dfs(current):
        if current in visited:
            return False
        visited.add(current)
        path.append(current)
        if current == end:
            return True
        for neighbor in graph.get(current, []):
            if dfs(neighbor):
                return True
        path.pop()
        return False

    if dfs(start):
        return ' '.join(path)
    else:
        return 'no route found'


def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().split('\n')

    n = int(lines[0])
    graph = {}

    for i in range(1, n + 1):
        parts = lines[i].split()
        station = parts[0]
        connections = parts[1:]
        if station not in graph:
            graph[station] = []
        for conn in connections:
            graph[station].append(conn)
            if conn not in graph:
                graph[conn] = []
            graph[conn].append(station)  # 양방향 연결

    start, end = lines[-1].split()
    print(find_route(graph, start, end))


if __name__ == "__main__":
    main()
