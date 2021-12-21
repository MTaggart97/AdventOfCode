unique_segments = 0
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        output = line.strip('\n').split('|')[1]
        output_segments = output.split(' ')
        unique_segments += sum(1 for seg in output_segments if len(seg) in [2, 4, 3, 7])

print(unique_segments)
