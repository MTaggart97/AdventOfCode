top_tiles = []
cave = []

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        tile = [int(i) for i in list(line.strip())]
        row = []
        for i in range(5):
            for j in tile:
                num = (i+j)
                if num >= 10:
                    num = 1 + (num % 10)
                row.append(num)
        top_tiles.append(row)

for i in range(5):
    for row in top_tiles:
        new_row = []
        for element in row:
            num = (i+element)
            if num >= 10:
                num = 1 + (num % 10)
            new_row.append(num)
        cave.append(new_row)

for row in cave:
    print(row)

start = (0, 0)
end = (len(cave)-1, len(cave[-1])-1)

print(f'Starting at {start} and finishing at {end}')

def get_neighbors(position: tuple) -> tuple:
    neigbours = []
    i, j = position
    if (j > 0):
        neigbours.append([(i, j - 1), cave[i][j-1]])
        if (i > 0):
            neigbours.append([(i-1, j - 1), cave[i-1][j-1]])
    if (j < len(cave[i])-1):
        neigbours.append([(i, j + 1), cave[i][j+1]])
    if (i > 0):
        neigbours.append([(i-1, j), cave[i-1][j]])
    if (i < len(cave)-1):
        neigbours.append([(i+1, j), cave[i+1][j]])
    return neigbours
    
def a_star_algorithm(start_node, stop_node, h):
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest risk level
            for v in open_list:
                if n == None or g[v] + h(v) < g[n] + h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

def h(position: tuple) -> int:
    return cave[position[0]][position[1]]

risk = sum(h(pos) for pos in a_star_algorithm(start, end, h))
risk -= h(start)
print(risk)
