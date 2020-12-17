import sys
import numpy as np
import heapq

adj = []
start = ()
goal = ()

def heuristic(a, b):
    return abs(a[1] - a[0]) + (b[1] - b[0])


def starapproach(array, start, goal):
    neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []

            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data
        close_set.add(current)
        cc = 0

        for i, j in neigh:

            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + \
                heuristic(current, neighbor) + cc

            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + \
                    heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
            cc += 1

    return False

#making a 2d array to store
def make2dList(rows, cols):
    a = []
    for row in range(rows):
        a += [[0]*cols]
    return a


if _name_ == "_main_":
    sys.stdin = open("input.txt", "r")
    r = 3
    arr = []
    a = []
    matrix = []
    rows = 0
    cols = 0
    for i in range(0, r):
            # taking input
        st = str(input())
        cols = len(st)
        arr.append(st)
    for i in range(0, r):
        rows += 1
        matrix.append(arr[i])
    a = make2dList(rows, cols)
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == '#':
                a[i][j] = 1
            if matrix[i][j] == 's':
                start = i, j
            if matrix[i][j] == 't':
                goal = i, j
    adj = np.array(a)
    route = starapproach(adj, start, goal)
    route = route + [start]
    route = route[::-1]
    for i in route:
        if i == start:
            print(i, "->Source")
        elif i == goal:
            print(i, "->Target")
        else:
            print(i)
