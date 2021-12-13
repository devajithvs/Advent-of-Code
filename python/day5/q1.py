def get_all_points(start, end):
    points = []
    if start[0] == end[0] or start[1]==end[1]:
        if end[0] > start[0]:
            for x in range (start[0], end[0]+1):
                if end[1] > start[1]:
                    for y in range(start[1], end[1]+1):
                        points.append((x,y))
                else:
                    for y in range(end[1], start[1]+1):
                        points.append((x,y))
        else:
            for x in range (end[0], start[0]+1):
                if end[1] > start[1]:
                    for y in range(start[1], end[1]+1):
                        points.append((x,y))
                else:
                    for y in range(end[1], start[1]+1):
                        points.append((x,y))
    return points


def Solution(file_content):
    points = []
    danger_point = {}
    for index, line in enumerate(file_content):
        point = line.split("->")
        if point:
            start = [int(x.strip()) for x in point[0].split(",")]
            end = [int(x.strip()) for x in point[1].split(",")]
            points.append([start, end])
            # print(start,end)
            for p in get_all_points(start,end):
                if p in danger_point:
                    danger_point[p]+=1
                else:
                    danger_point[p]=1
    point_overlap = 0
    # print(danger_point)
    for a in danger_point:
        if danger_point[a] >= 2:
            point_overlap+=1
    # print(point_overlap)
    x_pos = []
    y_pos = []
    for point in points:
        start = point[0]
        end = point[1]
        x_pos.append(start[0])
        x_pos.append(end[0])
        y_pos.append(start[1])
        y_pos.append(end[1])

    result = [ [0]*(max(y_pos)+1) for i in range(max(x_pos)+1)]
    # print(len(result), len(result[0]))

    # # for y in range(len(result)):
    # #     for x in range(len(result[0])):
    return point_overlap
