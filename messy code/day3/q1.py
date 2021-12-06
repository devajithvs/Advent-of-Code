def Solution(file_content):
    gamma = ""
    epsilon = ""
    for i in range(12):
        counter0 = 0
        counter1 = 0
        for line in file_content:
            if line[i].strip() != "":
                result = int(line[i].strip())
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
        gamma1 = int(str(gamma),2)
        epsilon1 = int(str(epsilon),2)
        print(gamma1,epsilon1)