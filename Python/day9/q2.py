def get_neighbours(i, j, env):
    neighbours = []
    for i1 in range(max(0,i-1), min(i+2,len(env))):
        for j1 in range(max(0,j-1), min(j+2, len(env[0]))):
            if i - i1 != j -j1:
                neighbours.append([i1, j1])
    return neighbours

def Solution(file_content):
    height_map = [list(x.strip()) for x in [line for line in file_content]]

    low_points = []
    low_points2 = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            low_point = True
            for neighbour in get_neighbours(i, j, height_map):
                if int(height_map[neighbour[0]][neighbour[1]]) <= int(height_map[i][j]):
                    low_point = False
                    break
            if low_point:
                low_points.append((i,j))
                low_points2.append(height_map[i][j])
    # print(low_points2)

    counter = []
    for point in low_points:
        i, j = point[0], point[1]
        counter.append(get_basin_size(i,j,height_map))
    counter.sort()
    # print(counter[-3:])

    product = 1
    for element in counter[-3:]:
        product*=element
    return product


def get_basin_size(i,j,height_map):
    queue = []
    queue.append((i,j))
    visited = [(i,j)]

    size = 1
    while queue:
        current_point = queue.pop(0)
        dead_end = False
        for neighbour in get_neighbours(current_point[0], current_point[1], height_map):
            neighbour_value = height_map[neighbour[0]][neighbour[1]]
            current_value = height_map[current_point[0]][current_point[1]]
            if neighbour not in visited and int(neighbour_value) > int(current_value) and int(neighbour_value)!=9:
                queue.append(neighbour)
                visited.append(neighbour)
                size+=1
                # print(neighbour_value, current_value, size)
    return size