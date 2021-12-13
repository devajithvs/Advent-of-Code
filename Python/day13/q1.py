def print_array(array):
    for i in array:
        print(' '.join(map(str, i)))
    print()

def Solution(file_content):
    coordinates = []
    instructions = []
    for value in file_content:
        value = value.strip()
        coordinate = value.split(",")
        if len(coordinate) >= 2:
            coordinates.append([int(coordinate[0]), int(coordinate[1])])
        elif len(coordinate) == 1 and coordinate[0]:
            instruction = value.split("=")
            instructions.append([instruction[0][-1], int(instruction[1])])
    
    x_pos = []
    y_pos = []
    for point in coordinates:
        x_pos.append(point[0])
        y_pos.append(point[1])
    paper = [ [0]*(max(x_pos)+1) for _ in range(max(y_pos)+1)]
    for point in coordinates:
        j = point[0]
        i = point[1]
        paper[i][j] = 1
    
    # print_array(paper)

    for fold in instructions[:1]:
        paper_x = len(paper[0])
        paper_y = len(paper)
        

        if fold[0] == "y":
            len_y = max(paper_y-fold[1], fold[1])-1
            len_x = paper_x
            new_paper = [ [0]*len_x for _ in range(len_y)]
            for ind_i in reversed(range(0,paper_y)):
                if len_y-ind_i >= 0 and ind_i!=fold[1]:
                    if (len_y-ind_i)%len_y > 0:
                            second_half = len_y+(len_y-ind_i)%len_y
                    else:
                        second_half = 2*len_y
                    for ind_j in range(paper_x):
                        new_paper[ind_i][ind_j] = paper[ind_i][ind_j] + paper[second_half][ind_j]
            paper = new_paper

        elif fold[0] == "x":
            len_x = max(paper_x-fold[1], fold[1])-1
            len_y = paper_y
            new_paper = [ [0]*len_x for _ in range(len_y)]

            for ind_j in reversed(range(0,paper_x)):
                if len_x-ind_j >= 0 and ind_j!=fold[1]:
                    if (len_x-ind_j)%len_x > 0:
                        second_half = len_x+(len_x-ind_j)%len_x
                    else:
                        second_half = 2*len_x
                    for ind_i in range(paper_y):
                        # print(ind_j, len_x, paper_x, second_half)
                        new_paper[ind_i][ind_j] = paper[ind_i][ind_j] + paper[ind_i][second_half]
            paper = new_paper

    counter = 0
    for i in paper:
        for j in i:
            if j:
                counter+=1    
    return counter
