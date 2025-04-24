INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

#  گرافی که مسیرهاش از اول کوتاه‌ترین هستند
graph_best = [
    [0,     2,     9],
    [INF,   0,     3],
    [INF,   INF,   0]
]

res = floyd_warshall(graph_best)

print("بهترین حالت:")
for row in res:
    print(row)
