positions = {}
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        pos = [int(i) for i in line.strip("\n").replace(" -> ", ",").split(",")]
        if (pos[0] == pos[2]):
            diff = pos[3] - pos[1]
            step = int(diff / abs(diff))
            for i in range(abs(diff) + 1):
                if ((pos[0], pos[1] + i*step) not in positions):
                    positions[(pos[0], pos[1] + i*step)] = 1
                else:
                    positions[(pos[0], pos[1] + i*step)] += 1
        elif (pos[1] == pos[3]):
            diff = pos[2] - pos[0]
            step = int(diff / abs(diff))
            for i in range(abs(diff) + 1):
                if ((pos[0] + i*step, pos[1]) not in positions):
                    positions[(pos[0] + i*step, pos[1])] = 1
                else:
                    positions[(pos[0] + i*step, pos[1])] += 1
        else:
            diff_x = pos[2] - pos[0]
            diff_y = pos[3] - pos[1]
            step_x = int(diff_x / abs(diff_x))
            step_y = int(diff_y / abs(diff_y))
            for i in range(int(abs(diff_x)) + 1):
                if ((pos[0] + i*step_x, pos[1] + i*step_y) not in positions):
                    positions[(pos[0] + i*step_x, pos[1] + i*step_y)] = 1
                else:
                    positions[(pos[0] + i*step_x, pos[1] + i*step_y)] += 1


total = 0
for val in positions.values():
    total += int(val > 1)

print(total)
