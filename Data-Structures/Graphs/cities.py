from collections import deque
def search(city):
    metro_city = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Bengaluru", "Hyderabad", "Pune"]
    search_queue = deque()
    search_queue += graph[city]
    searched = set()
    # while search queue is not empty
    while search_queue:

        city1 = search_queue.popleft()
        if city1 not in searched:
            searched.add(city1)
            if city1 in metro_city:
                print(city1+" is the nearest metro city to "+city)
                return True
            search_queue += graph[city1]
    return False

graph = {
    "Delhi": ["Agra", "Jaipur", "Chandigarh", "Lucknow"],
    "Agra": ["Delhi", "Gwalior", "Jaipur"],
    "Jaipur": ["Delhi", "Agra", "Ahmedabad"],
    "Chandigarh": ["Delhi", "Amritsar"],
    "Lucknow": ["Delhi", "Kanpur", "Varanasi"],
    "Kanpur": ["Lucknow"],
    "Varanasi": ["Lucknow", "Patna"],
    "Patna": ["Varanasi", "Kolkata"],
    "Kolkata": ["Patna", "Bhubaneswar"],
    "Bhubaneswar": ["Kolkata", "Visakhapatnam"],
    "Visakhapatnam": ["Bhubaneswar", "Vijayawada"],
    "Vijayawada": ["Visakhapatnam", "Hyderabad", "Chennai"],
    "Hyderabad": ["Vijayawada", "Bengaluru"],
    "Bengaluru": ["Hyderabad", "Chennai", "Mysuru"],
    "Chennai": ["Bengaluru", "Vijayawada"],
    "Mysuru": ["Bengaluru", "Mangaluru"],
    "Mangaluru": ["Mysuru", "Goa"],
    "Goa": ["Mangaluru", "Mumbai"],
    "Mumbai": ["Goa", "Surat", "Pune"],
    "Pune": ["Mumbai", "Surat"],
    "Surat": ["Mumbai", "Pune", "Ahmedabad"],
    "Ahmedabad": ["Surat", "Jaipur"]
}

search("Kanpur")
