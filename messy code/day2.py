with open("input_day2.txt", "r+") as mf:
    file_content = mf.readlines()
    depth = 0
    hz_position = 0
    for line in file_content:
        result = line.split()
        if result[0] == "forward":
            hz_position+=float(result[1])
        elif result[0] == "up":
            depth-=float(result[1])
        elif result[0] == "down":
            depth+=float(result[1])
        else:
            print("wtf")
        # print(depth,hz_position)
    print(depth*hz_position)