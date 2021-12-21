counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num_of_lines = 0
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        num_of_lines += 1
        for i, c in zip(range(len(line.strip("\n"))), line.strip("\n")):
            counts[i] += int(c)

gamma = 0
eplison = 0
for i, c in zip(reversed(range(len(counts))), counts):
    if (c > int(num_of_lines/2)):
        gamma += 2**i
    else:
        eplison += 2**i
    
print(gamma * eplison)
