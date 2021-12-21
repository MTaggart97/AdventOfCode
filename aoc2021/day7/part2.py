import math

numbers = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        numbers = [int(n) for n in line.strip("\n").split(",")]

min_x = 0
min_val = math.inf
start = min(numbers)
end = max(numbers)
for x in range(start, end+1):
    total = 0
    for n in numbers:
        total += int((abs(n - x) * (abs(n - x) +1))/2)
    if total < min_val:
        min_val = total
        min_x = x

print(min_x, min_val)
