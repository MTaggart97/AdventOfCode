from dataclasses import dataclass

@dataclass
class Octopus():
    energy_value: int
    flashed: bool

energy_levels = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        energy_levels.append([Octopus(int(i), False) for i in list(line.strip('\n'))])

def increment_neighbours(i: int, j: int, elements: list):
    if (j > 0):
        elements[i][j-1].energy_value += 1
        if (i > 0):
            elements[i-1][j-1].energy_value += 1
        if (i < len(elements)-1):
            elements[i+1][j-1].energy_value += 1
    if (j < len(elements[i])-1):
        elements[i][j+1].energy_value += 1
        if (i > 0):
            elements[i-1][j+1].energy_value += 1
        if (i < len(elements)-1):
            elements[i+1][j+1].energy_value += 1
    if (i > 0):
        elements[i-1][j].energy_value += 1
    if (i < len(elements)-1):
        elements[i+1][j].energy_value += 1

def finished_flashing(elements: list):
    for row in elements:
        for element in row:
            if (element.energy_value > 9 and not element.flashed):
                return False
    return True

flashes = 0
iterations = 100
for _ in range(iterations):
    # Increment all values by 1
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            energy_levels[i][j].energy_value += 1

    # If greather than 9, increment neighbours
    while not finished_flashing(energy_levels):
        for i in range(len(energy_levels)):
            for j in range(len(energy_levels[i])):
                if (energy_levels[i][j].energy_value > 9 and not energy_levels[i][j].flashed):
                    flashes += 1
                    energy_levels[i][j].flashed = True
                    increment_neighbours(i, j, energy_levels)

    # Set all values larger than 9 to zero
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            if (energy_levels[i][j].energy_value > 9):
                energy_levels[i][j].energy_value = 0
            energy_levels[i][j].flashed = False

print(f'There was {flashes} flashes after {iterations} iterations')