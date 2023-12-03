import os
import re

filename = os.path.join(os.path.dirname(os.getcwd()), 'day2/puzzle_input.txt')

with open(filename, 'r') as f:
    samples = f.read().split('\n')
    sum_ids = 0

    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

sum_max_cubes = 0
for string in samples:
    game_id, games_list = string.split(':')
    games = [[test.strip() for test in tmp.split(',')] for tmp in games_list.split(';')]
    correct = True
    max_red_cubes = 0
    max_green_cubes = 0
    max_blue_cubes = 0

    for game in games:
        for play in game:
            for color in ['green', 'blue', 'red']:
                pattern = re.compile(rf'(\d+ {color})')
                for elem in pattern.findall(play):
                    if int(elem.split(' ')[0]) > globals()[f"{color}_cubes"]:
                        correct = False
                    if int(elem.split(' ')[0]) > globals()[f"max_{color}_cubes"]:
                        globals()[f"max_{color}_cubes"] = int(elem.split(' ')[0])
    sum_max_cubes += (max_red_cubes * max_green_cubes * max_blue_cubes)
    if correct:
        sum_ids += int(game_id.split(' ')[1])
print(sum_ids)
print(sum_max_cubes)

# Part 2


