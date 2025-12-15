"""
Ford-Fulkerson Algorithm (Max Flow) - Visualization Friendly Implementation
---------------------------------------------------------------------------
Designed for educational and visualization purposes as part of a
Design and Analysis of Algorithms project.

Features:
- Step-by-step augmentation tracking
- Residual graph updates
- Path flow visualization support

Time Complexity: O(E * max_flow)
Space Complexity: O(V^2)
"""

from collections import deque


class FordFulkersonVisualizer:
    def __init__(self, graph):
        """
        graph: adjacency matrix representation of the graph
        graph[u][v] represents capacity from u to v
        """
        self.graph = graph
        self.n = len(graph)
        self.steps = []

    def bfs(self, source, sink, parent):
        visited = [False] * self.n
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v in range(self.n):
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]

    def run(self, source, sink):
        parent = [-1] * self.n
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink

            # Find minimum residual capacity along the path
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            # Store step for visualization
            self.steps.append({
                "action": "augment_path",
                "path_flow": path_flow,
                "current_max_flow": max_flow,
                "residual_graph": [row[:] for row in self.graph]
            })

            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow, self.steps


# Example execution
if __name__ == "__main__":
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    source = 0
    sink = 5

    visualizer = FordFulkersonVisualizer(graph)
    max_flow, steps = visualizer.run(source, sink)

    print("Maximum Flow:", max_flow)
    print("\nExecution Steps:")
    for step in steps:
        print(step)
