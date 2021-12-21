fish = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        fish = [int(n) for n in line.strip("\n").split(",")]

days = 256

cache = {}
def total_fish_produced(new_f: int, offset: int, days: int = days):
    if (days <= offset+new_f):
        return 0
    if (new_f, offset) in cache:
        return cache[(new_f, offset)]
    new_fish = int((days-new_f-offset-1) / 7)
    for new_f,delta in zip([8]*new_fish, range(offset+new_f+1, days+1, 7)):
        new_fish += total_fish_produced(new_f, delta)
    cache[(new_f, offset)] = new_fish + 1
    return new_fish + 1

day_1_cache = {}

for f in fish:
    if f in day_1_cache:
        continue
    else:
        new_fish = 1 + int((days-f-1) / 7)
        for new_f,offset in zip([8]*new_fish, range(f+1, days+1, 7)):
            new_fish += total_fish_produced(new_f, offset)
        day_1_cache[f] = 1 + new_fish

print(day_1_cache)
ans = 0
for f in fish:
    ans += day_1_cache[f]
print(ans)
