from collections import deque
def search(node):
    search_queue = deque()
    searched = set()


    while search_queue:
        search_queue += graph[node]
        node1 = search_queue.popleft()
        if node1 not in searched:
            if node1 == "G":
                return True
            searched.add(node1)
            search_queue.append(graph[node1])
    return False

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
if result == True:
    print("Path A to G exists.")
else:
    print("There is no path from A to G.")

