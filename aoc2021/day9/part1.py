height_map = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        heights_str = list(line.strip('\n'))
        height_int = [int(i) for i in heights_str]
        height_map.append(height_int)

risk_levels = []
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
            risk_levels.append(element+1)

print(sum(risk_levels))
