import os
import time

def inside_range(index, n):
    return index - 1 >= 0 and index + 1 <= n - 1


def neighbors(grid, i, j) :
    n = len(grid)
    m = len(grid[0])
    if i == 0 and j == 0:
        return [grid[i + 1][j], grid[i][j + 1], grid[i + 1][j + 1]]
    elif i == 0 and j == m - 1:
        return [grid[i + 1][j], grid[i][j - 1], grid[i + 1][j - 1]]
    elif i == n - 1 and j == m - 1:
        return [grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]]
    elif i == n - 1 and j == 0:
        return [grid[i - 1][j], grid[i - 1][j + 1], grid[i][j + 1]]
    elif i == 0 and inside_range(j, m):
        return [grid[i][j - 1], grid[i][j + 1], grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]]
    elif inside_range(i, n) and j == m - 1:
        return [grid[i - 1][j - 1], grid[i - 1][j], grid[i][j - 1], grid[i + 1][j - 1], grid[i + 1][j]]
    elif i == n - 1 and inside_range(j, m):
        return [grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1], grid[i][j + 1]]
    elif inside_range(i, n) and j == 0:
        return [grid[i - 1][j], grid[i + 1][j], grid[i - 1][j + 1], grid[i][j + 1], grid[i + 1][j + 1]]
    elif inside_range(i, n) and inside_range(j, m):
        return [grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1], grid[i][j + 1], grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]]


def rules(neighbors_state, cell):
    if neighbors_state == 3 and cell == 0:
        return 1
    if (neighbors_state < 2 or neighbors_state > 3) and cell == 1:
        return 0;
    if (neighbors_state == 2 or neighbors_state == 3) and  cell == 1:
        return 1
    return cell


grid = [[0 ,1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]]


def display(grid):
    for _row in grid:
        for _cell in _row:
            print(_cell, "\t", end='')
        print("\n")
    print("#############################")
    time.sleep(2)




for _ in range(0, 20):
    os.system("cls")
    grid2= [[0 ,0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    i = 0
    for row in grid:
        j = 0
        for cell in row:
            grid2[i][j] = rules(sum(neighbors(grid, i, j)), grid[i][j])
            j += 1
        i += 1
    display(grid2)
    grid = grid2




