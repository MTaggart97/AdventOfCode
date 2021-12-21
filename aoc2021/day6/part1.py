from matplotlib import pyplot as plt

fish = []
with open('small_input.txt', 'r', encoding='utf8') as f:
    for line in f:
        fish = [int(n) for n in line.strip("\n").split(",")]

totals = [len(fish)]
day = 0
while day < 80:
    new_fish = []
    for i in range(len(fish)):
        fish[i] = fish[i] - 1
        if fish[i] < 0:
            fish[i] = 6
            new_fish.append(8)
    fish.extend(new_fish)
    totals.append(len(fish))
    day += 1
    
print(len(fish))
plt.plot(totals)
plt.show()