with open("input_day3.txt", "r+") as mf:
    file_content = mf.readlines()
    gamma = ""
    epsilon = ""
    for i in range(12):
        counter0 = 0
        counter1 = 0
        for line in file_content:
            result = int(line[i])
            if result == 0:
                counter0+=1
            elif result == 1:
                counter1+=1
        if counter0 >= counter1:
            gamma+="0"
            epsilon+="1"
        else:
            epsilon+="0"
            gamma+="1"
        gamma1 = int(gamma)
        epsilon1 = int(epsilon)
        print(gamma1,epsilon1)



