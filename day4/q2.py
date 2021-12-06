def winCheck(bingo):
    for i in range(len(bingo)):
        winner = True
        for j in range(len(bingo[i])):
            if(bingo[i][j] != -1):
                winner=False
                break

        if winner:
            return True

        # vertical rows
        for j in range(len(bingo[0])):
            winner = True
        for i in range(len(bingo)):
            if(bingo[i][j] != -1):
                winner=False
                break

        if winner:
            return True

    return False

def get_result(winBoard, winNo):
    sum = 0
    for element in winBoard:
        for el2 in element:
            if el2 != -1:
                sum+= el2
    # print(sum, winNo)
    return sum*winNo

def Solution(file_content):
    bingo_numbers = file_content[0].split(",")
    bingo_numbers = [int(x) for x in bingo_numbers]
    
    bingo_boards = []
    bingo_board = []
    for index, line in enumerate(file_content[1:]):
        
        if line.strip() != "":
            rows = line.split(" ")
            row = []
            if rows:
                for x in rows:
                    if x.strip() != "":
                        row.append(int(x.strip()))
                bingo_board.append(row)
                row = []
        if line.strip() == "" or index >= len(file_content)-2 :
            if bingo_board:
                bingo_boards.append(bingo_board)
                bingo_board = []
                continue
    winBoard = []
    for index,bingo_board in enumerate(bingo_boards):
        bingo_boards[index] = [list(i) for i in zip(*bingo_board)]
    
    win_status = [0]*len(bingo_boards)
    for number in bingo_numbers:
        for n in range(len(bingo_boards)):
            for i in range(len(bingo_boards[0])):
                for j in range(len(bingo_boards[0][0])):
                    if bingo_boards[n][i][j] == number:
                        bingo_boards[n][i][j] = -1
            if winCheck(bingo_boards[n]):
                winElement = number
                winBoard = bingo_boards[n]
                win_status[n] = 1
                product = 1
                for value in win_status:
                    product*=value
                if product == 1:
                    return get_result(winBoard, winElement)