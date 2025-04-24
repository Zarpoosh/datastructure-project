from collections import deque

def shortest_path(graph, start, end):
    queue = deque([[start]])  # هر مسیر یک لیست از گره‌هاست
    visited = set()  # برای اینکه گرهی دوباره بررسی نشه

    while queue:
        path = queue.popleft()  # مسیر فعلی
        node = path[-1]  # آخرین گره مسیر

        if node == end:
            print("کوتاه‌ترین مسیر:", " -> ".join(path))
            return

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    print("مسیر پیدا نشد.")

#  تعریف گراف
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# فراخوانی تابع
shortest_path(graph, "A", "F")
