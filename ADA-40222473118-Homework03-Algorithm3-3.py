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

#  گرافی که مسیرهای مستقیم خیلی طولانی‌اند و همه مسیرها از طریق گره‌های واسطه کوتاه‌تر می‌شن
graph_worst = [
    [0,     1000,  1000],
    [1000,   0,    1000],
    [1,      1,      0]
]

res = floyd_warshall(graph_worst)

print("\n بدترین حالت:")
for row in res:
    print(row)
