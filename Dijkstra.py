from queue import PriorityQueue

def dijkstra(start_vertex):
        D = {nodes:float('inf') for nodes in range(nodes)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            visited.append(current_vertex)

            for neighbor in range(nodes):
                if edges[current_vertex][neighbor] != -1:
                    distance = edges[current_vertex][neighbor]
                    if neighbor not in visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

nodes = 20
visited = []

data = [
    (0, 5, {'weight': 1}), (0, 7, {'weight': 9}), 
    (0, 11, {'weight': 11}), (0, 16, {'weight': 11}), (0, 17, {'weight': 3}), 
    (0, 18, {'weight': 9}), (1, 5, {'weight': 5}), (1, 7, {'weight': 1}), 
    (1, 9, {'weight': 10}), (1, 15, {'weight': 1}), (1, 16, {'weight': 6}), 
    (1, 19, {'weight': 12}), (2, 12, {'weight': 14}), (2, 16, {'weight': 4}), 
    (2, 19, {'weight': 13}), (3, 7, {'weight': 5}), (3, 15, {'weight': 1}), (3, 16, {'weight': 10}), 
    (3, 18, {'weight': 4}), (4, 7, {'weight': 3}), (4, 8, {'weight': 11}), (4, 11, {'weight': 12}), 
    (4, 13, {'weight': 13}), (4, 16, {'weight': 9}), (4, 18, {'weight': 8}), (5, 7, {'weight': 2}), 
    (5, 8, {'weight': 2}), (5, 9, {'weight': 13}), (5, 11, {'weight': 1}), (5, 14, {'weight': 12}), 
    (6, 7, {'weight': 8}), (6, 10, {'weight': 6}), (6, 13, {'weight': 13}), (6, 15, {'weight': 5}), 
    (6, 18, {'weight': 13}), (7, 8, {'weight': 2}), (7, 11, {'weight': 13}), (7, 16, {'weight': 4}), 
    (7, 17, {'weight': 6}), (7, 19, {'weight': 7}), (8, 13, {'weight': 8}), (8, 14, {'weight': 10}), 
    (8, 16, {'weight': 14}), (9, 16, {'weight': 9}), (10, 17, {'weight': 7}), (10, 19, {'weight': 5}), 
    (11, 13, {'weight': 12}), (11, 14, {'weight': 13}), (11, 15, {'weight': 2}), (12, 13, {'weight': 9}), 
    (12, 15, {'weight': 7}), (12, 17, {'weight': 8}), (13, 15, {'weight': 1}), (13, 18, {'weight': 9}),
    (13, 19, {'weight': 6}), (14, 18, {'weight': 9}), (15, 18, {'weight': 2}), (17, 18, {'weight': 14}), 
    (17, 19, {'weight': 13})]

edges = [[-1 for i in range(nodes)] for j in range(nodes)]

for i in data:
    for j in range(nodes):
        edges[i[0]][i[1]] = i[2]["weight"]
        edges[i[1]][i[0]] = i[2]["weight"]

D = dijkstra(0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])