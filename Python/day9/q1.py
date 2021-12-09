def get_neighbours(i, j, env):
    neighbours = []
    for i1 in range(max(0,i-1), min(i+2,len(env))):
        for j1 in range(max(0,j-1), min(j+2, len(env[0]))):
            if env[i1][j1] != env[i][j]:
                neighbours.append(env[i1][j1])
    return neighbours

def Solution(file_content):
    height_map = [list(x.strip()) for x in [line for line in file_content]]

    low_points = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            low_point = True
            for neighbour in get_neighbours(i, j, height_map):
                if int(neighbour) <= int(height_map[i][j]):
                    low_point = False
                    break
            if low_point:
                low_points.append(height_map[i][j])
    # print(low_points)

    result = 0
    for x in low_points:
        result+=int(x)+1
    return result