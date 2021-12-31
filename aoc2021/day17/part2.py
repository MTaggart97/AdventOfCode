import math
import itertools

target_area = []

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        x_coords, y_coords = line.strip('\n').split(', ')
        x_coords = [int(i) for i in x_coords.strip('x=').split('..')]
        y_coords = [int(i) for i in y_coords.strip('y=').split('..')]
        target_area.append(x_coords)
        target_area.append(y_coords)

x_steps = dict()
y_steps = dict()

# First find the max y velocity that will land in the target
# This will be used to get the maximum number of steps to check
# for a starting point to hit the target, can't use x as the number
# of steps it can take is infinte (as it hit's a brick wall)
y_vel = 1
max_y_vel = y_vel
attempts = 10_000   # Miss 10_000 times before counting as failure
missed_count = 0
while True:
    steps = math.ceil((y_vel + (y_vel**2 - 2*target_area[1][0])**0.5))
    temp_y_vel = y_vel
    height = (y_vel*(y_vel+1)) / 2
    height -= ((steps-1-y_vel)*(steps-y_vel)) / 2
    missed = target_area[1][0] > height or height > target_area[1][1]
    if (missed):
        missed_count += 1
        if (missed_count == attempts):
            break
    else:
        max_y_vel = y_vel
    y_vel += 1

# Maximum number of steps found using s(t) = C + y_vel*t - 0.5t^2
max_steps = math.ceil((max_y_vel + (max_y_vel**2 - 2*target_area[1][0])**0.5))
print(max_steps)

# Can find the minimum x velocity that will reach the target using
# the -b formula (on S(n) = n*n+1 / 2)
x_vel = target_area[0][1]
min_x_vel = math.ceil((-1 + (1 + 8*target_area[0][0])**0.5) / 2)
while x_vel >= min_x_vel:
    steps = 0
    # Maximum number of steps found using s(t) = C + x_vel*t - 0.5t^2
    # max_steps = math.ceil((x_vel + (x_vel**2 - 2*target_area[0][0])**0.5))
    dist = 0
    velocity = x_vel
    while steps < max_steps:
        steps += 1
        dist += velocity
        if (target_area[0][0] <= dist and dist <= target_area[0][1]):
            if steps in x_steps:
                x_steps[steps].append(x_vel)
            else:
                x_steps[steps] = [x_vel]
        velocity = max(0, velocity-1)
    x_vel -= 1

print(x_steps)

# Can do the same to find the y-values
# Start at the maximum y velocity and work down towards
# the minimum y-coordindate in the target area
y_vel = max_y_vel
min_y_vel = target_area[1][0]
while y_vel >= min_y_vel:
    steps = 0
    # Maximum number of steps found using s(t) = C + y_vel*t - 0.5t^2
    # max_steps = math.ceil((y_vel + (y_vel**2 - 2*target_area[1][0])**0.5))
    dist = 0
    velocity = y_vel
    while steps < max_steps:
        steps += 1
        dist += velocity
        if (target_area[1][0] <= dist and dist <= target_area[1][1]):
            if steps in y_steps:
                y_steps[steps].append(y_vel)
            else:
                y_steps[steps] = [y_vel]
        velocity -= 1
    y_vel -= 1

print(y_steps)

all_pairs = []
for key, value in x_steps.items():
    if key in y_steps:
        all_pairs.extend(itertools.product(value, y_steps[key]))

print(len(set(all_pairs)))
