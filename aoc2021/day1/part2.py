import itertools

depths = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        depths.append(int(line))

def sliding_window(iterable, n=2):
    iterables = itertools.tee(iterable, n)
    
    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)
    
    return zip(*iterables)

count = 0
prev_sum = float('inf')
windows = sliding_window(depths, 3)
for window in windows:
    s1 = window[0] + window[1] + window[2]
    count += int(prev_sum < s1)
    prev_sum = s1

print(count)
