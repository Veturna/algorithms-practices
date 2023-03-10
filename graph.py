from collections import deque

#dict
graph = {
    'ja': ['alicja', 'bartek', 'cecylia'],
    'bartek': ['janusz', 'patrycja'],
    'alicja': ['patrycja'],
    'cecylia': ['tamara', 'jarek'],
    'janusz': [],
    'patrycja': [],
    'tamara': [],
    'jarek': []
}

def person_is_seller(name):
    return len(name) == 5

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' sprzedaje mango')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

#test
search('ja')
