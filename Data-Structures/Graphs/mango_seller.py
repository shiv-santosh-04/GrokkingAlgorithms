from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a mango seller")
                return True
            else:
                #add his friends to search queue
                search_queue += graph[person]
                #mark the person as checked
                searched.add(person)
    return False

def person_is_seller(name):
    if name[-1] == "m":
        return 1


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search("you")

