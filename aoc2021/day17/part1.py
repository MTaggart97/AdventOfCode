import math

target_area = []

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        x_coords, y_coords = line.strip('\n').split(', ')
        x_coords = [int(i) for i in x_coords.strip('x=').split('..')]
        y_coords = [int(i) for i in y_coords.strip('y=').split('..')]
        target_area.append(x_coords)
        target_area.append(y_coords)

print(target_area)

# Use -b formula to get minimum starting x velocity
# that will intersect with the target area
# NOTE: This only looks in the positive x direction
x_vel = (-1 + (1 + 8*target_area[0][0])**0.5) / 2
x_vel = math.ceil(x_vel)

# Can do the something similar to find the number of steps needed for
# the target to be reached in the y-axis
y_vel = 1
curr_best_velocity = y_vel
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
        curr_best_velocity = y_vel
    y_vel += 1

print(x_vel, curr_best_velocity)
print((curr_best_velocity*(curr_best_velocity+1)) / 2)