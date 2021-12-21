# Build an adjacency list as easier to iterate over nodes than and adjacency matrix
graph = dict()
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        nodes = line.strip('\n').split('-')
        if (nodes[0] in graph):
            graph[nodes[0]].append(nodes[1])
        else:
            graph[nodes[0]] = [nodes[1]]
        if (nodes[1] in graph):
            graph[nodes[1]].append(nodes[0])
        else:
            graph[nodes[1]] = [nodes[0]]

# Now just do a search from start to end (only adding to visited if large cave -- upper case)
start = 'start'
target = 'end'
visited = set()
queue = [[start, [start]]]
paths = 0
while queue:
    current_element, path = queue.pop()
    for neighbour in graph[current_element]:
        if ((neighbour.islower() and neighbour not in path) or neighbour.isupper()):
            if (neighbour == target):
                paths += 1
                print(path + [neighbour])
            else:
                queue.append([neighbour, path + [neighbour]])

print(paths)
