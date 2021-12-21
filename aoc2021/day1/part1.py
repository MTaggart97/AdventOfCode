depths = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        depths.append(int(line))

count = 0
for i in range(len(depths)-1):
    if depths[i] < depths[i+1]:
        count += 1

print(count)
