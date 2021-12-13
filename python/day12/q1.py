from typing import Deque


def Solution(file_content):
    path_dict = {}
    for line in file_content:
        line = line.strip()
        connection = line.split("-")
        if connection[0] in path_dict:
            path_dict[connection[0]].append(connection[1])
        else:
            path_dict[connection[0]] = [connection[1]]
        if connection[1] in path_dict:
            path_dict[connection[1]].append(connection[0])
        else:
            path_dict[connection[1]] = [connection[0]]
    
    return find_paths(path_dict)

def can_visit(path, value):
    
    if value.isupper():
        return True
    if value=="start" or value in path:
        return False
    return True


def find_paths(path_dict):
    q = Deque()
    paths = []

    current_path = []
    current_path.append("start")
    q.append(current_path.copy())

    while q:
        current_path = q.popleft()
        if current_path[-1] == "end":
            paths.append(current_path)
            # print(current_path)
        for neighbour in path_dict[current_path[-1]]:
            if can_visit(current_path, neighbour):
                new_path = current_path.copy()
                new_path.append(neighbour)
                q.append(new_path)
    return len(paths)