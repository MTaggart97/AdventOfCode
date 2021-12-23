hashes = dict()
fold_instructions = []
with open('input.txt', 'r', encoding='utf8') as f:
    read_hashes = True
    for line in f:
        if (line == '\n'):
            read_hashes = False
            continue
        if (read_hashes):
            x, y = [int(i) for i in line.strip('\n').split(',')]
            hashes[(x, y)] = '#'
        else:
            axis, number = line.strip('\n').split('=')
            number = int(number)
            axis = axis[-1]
            fold_instructions.append((axis, number))

for axis, line_number in fold_instructions:
    print(f'Folding along {axis} axis on line {line_number}')
    if axis == 'x':
        for index in list(hashes.keys()):
            if (index[0] == line_number):
                del hashes[index]
            elif (index[0] > line_number):
                delta = index[0] - line_number
                hashes[(line_number - delta, index[1])] = '#'
                hashes.pop(index)
    else:
        for index in list(hashes.keys()):
            if (index[1] == line_number):
                del hashes[index]
            elif (index[1] > line_number):
                delta = index[1] - line_number
                hashes[index[0], line_number - delta] = '#'
                hashes.pop(index)

print(len(hashes))

# Set up matrix to display code
x = max([axis[0] for axis in hashes.keys()])
y = max([axis[1] for axis in hashes.keys()])
row = ['.'*(x+1)]
code = row*(y+1)

for index in hashes:
    s = code[index[1]]
    new_string = s[:index[0]] + '#' + s[index[0] + 1:]
    code[index[1]] = new_string

for line in code:
    print(line)
