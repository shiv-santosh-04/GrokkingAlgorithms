from collections import deque
def search(start):
    search_queue = deque()
    search_queue.append(start)
    searched = set()


    while search_queue:
        node = search_queue.popleft()

        if node == 'G':
            return True

        if node not in searched:
            searched.add(node)
            search_queue += graph[node]

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E", "F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
result = search("A")
if result:
    print("Path A to G exists.")
else:
    print("There is no path from A to G.")

