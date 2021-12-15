from typing import Deque

def Solution(file_content):
    path_matrix = []
    for row in file_content:
        row = list(row.strip())
        row = [int(x) for x in row]
        path_matrix.append(row)
    
    # print_array(path_matrix)
    risk = get_min_risk(path_matrix)
    return risk

def print_array(array):
    for i in array:
        print('\t'.join(map(str, i)))
    print()
    
def neighbours(point, array):
    directions = [
        [point[0] + 1, point[1]],
        [point[0] - 1, point[1]],
        [point[0], point[1] + 1],
        [point[0], point[1] - 1],
    ]
    neighbours = []
    elements = []
    for i, j in directions:
        if i >= 0 and j>= 0:
            try:
                element = array[i][j]
                elements.append(element)
                neighbours.append((i,j))
            except:
                pass
    return neighbours


def get_min_risk(array):
    q = Deque()
    current_point = (0,0)
    q.append(current_point)
    risk = [[2**64]*len(array[0]) for _ in array]
    lowest_risk = 2**64
    risk[0][0] = 0
    while q:
        current_point = q.popleft()
        if current_point == (len(array)-1, len(array[0])-1):
            lowest_risk = min(risk[-1][-1], lowest_risk)
            continue
        for neighbour in neighbours(current_point, array):
            if risk[neighbour[0]][neighbour[1]] > risk[current_point[0]][current_point[1]]+array[neighbour[0]][neighbour[1]]:
                risk[neighbour[0]][neighbour[1]] = risk[current_point[0]][current_point[1]]+array[neighbour[0]][neighbour[1]]
                q.append(neighbour)
    return lowest_risk
        