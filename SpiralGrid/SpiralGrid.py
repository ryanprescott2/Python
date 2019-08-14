""" Spiral Problem
Write a function that takes in a grid of numbers (as a list of lists), and outputs them as
a list in spiral order -- starting from the top left, in clockwise direction.
"""
# Works for any size rectangular grid

grid1 = [
    [1, 2, 3, 4, 5, 6],
    [16, 17, 18, 19, 20, 7],
    [15, 24, 23, 22, 21, 8],
    [14, 13, 12, 11, 10, 9]
] # this grid specifically will be 1 to 24 in order


height = len(grid1)
length = len(grid1[0])

columns = [[grid1[i][x] for i in range(0, height)] for x in range(0, length)]
# print columns

master_list = []

def forward(grid, row):
    global master_list
    global grid1
    for index, val in enumerate(grid1[0]):
        master_list.append(val)
    del grid1[row]
    # print grid1
    # print master_list


def down(grid):
    # print length
    global master_list
    for i in range(height):
        master_list.append(grid[i][length - 1])
    # print master_list
    for i in grid1:
        del i[length - 1]
    # print grid1


def backward(grid, row):
    global master_list
    for i in range(length - 1, -1, -1):
        master_list.append(grid1[row][i])
    # print master_list
    del grid[row]
    # print grid


def up(grid):
    global master_list
    for i in range(height - 1, -1, -1):
        master_list.append(grid[i][0])
    # print master_list
    for i in grid1:
        del i[0]
    # print grid


def calculate_grid_size(grid):
    global length
    global height
    try:
        length = len(grid[0])
    except IndexError:
        print master_list
        raise SystemExit
    height = len(grid)


def print_spiral(grid):
    while True:
        forward(grid, 0)
        calculate_grid_size(grid)
        down(grid)
        calculate_grid_size(grid)
        backward(grid, height - 1)
        calculate_grid_size(grid)
        up(grid)
        calculate_grid_size(grid)


if __name__ == "__main__":
    print_spiral(grid1)
