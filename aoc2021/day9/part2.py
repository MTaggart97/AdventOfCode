from dataclasses import dataclass
import math

@dataclass(eq=True, frozen=True)
class Point:
    val: int
    i: int
    j: int

def get_neighbours(i: int, j: int, map: list) -> list[Point]:
    neighbours = []
    if (j > 0):
        neighbours.append(Point(map[i][j-1], i, j-1))
    if (j < len(map[i])-1):
        neighbours.append(Point(map[i][j+1], i, j+1))
    if (i > 0):
        neighbours.append(Point(map[i-1][j], i-1, j))
    if (i < len(map)-1):
        neighbours.append(Point(map[i+1][j], i+1, j))
    
    return neighbours


height_map = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        heights_str = list(line.strip('\n'))
        height_int = [int(i) for i in heights_str]
        height_map.append(height_int)

# Going to do a Breath First Search to get area of basin
# First find the low point of each basin
low_points = []
for i, row in enumerate(height_map):
    for j, element in enumerate(row):
        smallest = True
        if (j > 0):
            smallest &= (element < height_map[i][j-1])
        if (j < len(row)-1):
            smallest &= (element < height_map[i][j+1])
        if (i > 0):
            smallest &= (element < height_map[i-1][j])
        if (i < len(height_map)-1):
            smallest &= (element < height_map[i+1][j])
        if (smallest):
            low_points.append(Point(element, i, j))

# For each low point, do a BFS
areas = []
for low_point in low_points:
    search_queue = []
    search_queue.append(low_point)
    visited = set()
    while search_queue:
        current_element = search_queue.pop(0)
        visited.add(current_element)
        for neighbour in get_neighbours(current_element.i, current_element.j, height_map):
            if (neighbour not in visited):
                if (neighbour.val != 9):
                    search_queue.append(neighbour)
    areas.append(len(visited))

areas.sort()
print(math.prod(areas[-3:]))
