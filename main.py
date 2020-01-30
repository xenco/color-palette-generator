from PIL import Image, ImageDraw
import numpy as np
import random


def modify_color(lighten, color, percent):
    color = [c for c in color[:-1]]
    color = np.array(color)
    mod = np.array([255, 255, 255] if lighten else [0, 0, 0])
    vector = mod - color
    return tuple(int(i) for i in tuple(color + vector * percent)) + (255,)


base_colors = [
    (0, 0, 0, 255),
    (255, 0, 0, 255),
    (0, 255, 0, 255),
    (0, 0, 255, 255),
    (0, 255, 255, 255),
    (255, 0, 255, 255),
    (255, 255, 0, 255),
    (255, 255, 255, 255),
    (255, 220, 200, 255),
]

num_shades = 6
cell_size = 16

grid = [[base_colors[y] if x == 0 else 0 for x in range(num_shades)] for y in range(len(base_colors))]
for y in range(len(grid)):
    last_color = grid[y][0]
    modifier = True
    for x in range(1, len(grid[y]) - 1):
        if x == num_shades / 2:
            last_color = grid[y][0]
            modifier = False
        grid[y][x] = modify_color(modifier, last_color, 0.2)
        last_color = grid[y][x]

canvas = (cell_size * num_shades - cell_size, cell_size * len(base_colors))

im = Image.new('RGBA', canvas, (255, 255, 255, 255))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        ImageDraw.Draw(im).rectangle([
            cell_size * x,
            cell_size * y,
            cell_size * x + cell_size,
            cell_size * y + cell_size
        ], fill=grid[y][x])

im.save('example.png')
