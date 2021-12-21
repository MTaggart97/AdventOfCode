import copy

report = []
width = 0
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        width = max(width, len(line.strip("\n")))
        report.append(int(line.strip("\n"), 2))

report_copy = copy.deepcopy(report)

def filter_max(numbers: list, index: int):
    if len(numbers) == 1 or index == 0:
        return numbers
    count = 0
    for num in numbers:
        count += int((num >> index-1) & 0b1)

    drop_prefix = int(2*count >= int(len(numbers)))

    return filter_max([n for n in numbers if drop_prefix == int((n >> index-1) & 0b1)], index-1)

def filter_min(numbers: list, index: int):
    if len(numbers) == 1 or index == 0:
        return numbers
    count = 0
    for num in numbers:
        count += int((num >> index-1) & 0b1)

    drop_prefix = int(2*count < int(len(numbers)))

    return filter_min([n for n in numbers if drop_prefix == int((n >> index-1) & 0b1)], index-1)

print(filter_max(report, width)[0] * filter_min(report_copy, width)[0])
