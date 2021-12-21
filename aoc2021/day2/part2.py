position = [0, 0, 0]
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        direction = line.split(" ")
        if (direction[0] == "forward"):
            position[0] += int(direction[1])
            position[1] += int(direction[1]) * position[2]
        elif (direction[0] == "backward"):
            position[0] -= int(direction[1])
            position[1] -= int(direction[1]) * position[2]
        elif (direction[0] == "up"):
            position[2] -= int(direction[1])
        elif (direction[0] == "down"):
            position[2] += int(direction[1])

print(position)
print(position[0] * position[1])
