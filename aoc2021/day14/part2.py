template = dict()
instructions = dict()

with open('input.txt', 'r', encoding='utf8') as f:
    read_instructions = False
    for line in f:
        if (line == '\n'):
            read_instructions = True
            continue
        if (read_instructions):
            sequence, insertion = line.strip('\n').split(' -> ')
            instructions[sequence] = [sequence[0] + insertion, insertion + sequence[1]]
        else:
            temp = list(line.strip('\n'))
            for i in range(len(temp) - 1):
                key = temp[i] + temp[i+1]
                if key in template:
                    template[temp[i] + temp[i+1]] += 1
                else:        
                    template[temp[i] + temp[i+1]] = 1
            # Needs to be kept as we will lose track of it in the following process
            last_val = temp[-1]

step = 40
for i in range(step):
    insertions = dict()
    for pair, value in template.items():
        to_insert = instructions[pair]
        for new_pair in to_insert:
            if new_pair in insertions:
                insertions[new_pair] += value
            else:
                insertions[new_pair] = value
    template = insertions.copy()

frequencies = dict()
for k, v in template.items():
    if k[0] in frequencies:
        frequencies[k[0]] += v
    else:
        frequencies[k[0]] = v

frequencies[last_val] += 1

print(frequencies)
print(max(frequencies.values()) - min(frequencies.values()))
