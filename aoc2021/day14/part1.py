template = []
instructions = dict()

with open('small_input.txt', 'r', encoding='utf8') as f:
    read_instructions = False
    for line in f:
        if (line == '\n'):
            read_instructions = True
            continue
        if (read_instructions):
            sequence, insertion = line.strip('\n').split(' -> ')
            instructions[sequence] = insertion
        else:
            template = list(line.strip('\n'))

print(f'Template is {template}')
print(instructions)

step = 10
for i in range(step):
    insertions = dict()
    for j in range(len(template) - 1):
        seq = template[j] + template[j+1]
        insertions[2*j+1] = instructions[seq]
    for index, character in insertions.items():
        template.insert(index, character)

frequencies = {i:template.count(i) for i in set(template)}
print(max(frequencies.values()) - min(frequencies.values()))