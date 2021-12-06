def find_common(i, A):
    counter0 = 0
    counter1 = 0
    for line in A:
        result = int(line[i].strip())
        if result == 0:
            counter0+=1
        elif result == 1:
            counter1+=1
    if counter0 > counter1:
        return 0
    elif counter0 < counter1:
        return 1
    else:
        return -1

with open("input2_day3.txt", "r+") as mf:
    file_content = mf.readlines()
    oxy = ""
    carbon = ""
    array0 = []
    array1 = []
    counter = 0
    A = [x.strip() for x in file_content[:]]
    B = A[:]
    for i in range(len(file_content[0])):
    # for i in range(1):
        # oxygen
        if len(A) <= 1:
            break
        common_elem = find_common(i, A)
        if common_elem == -1:
            common_elem = 1
        j = 0
        while j<len(A):
            line = A[j]
            result = int(line[i].strip())
            if result != common_elem:
                A.remove(line)
            else:
                j+=1
        oxy = A[0]
        
    for i in range(len(file_content[0])):
        # carbon
        if len(B) <= 1:
            break
        common_elem = find_common(i, B)
        if common_elem == -1:
            common_elem = 1
        j = 0
        while j<len(B):
            line = B[j]
            result = int(line[i].strip())
            if result == common_elem:
                B.remove(line)
            else:
                j+=1
        carbon = B[0]
    oxy1 = int(str(oxy),2)
    carbon1 = int(str(carbon),2)
    print(oxy1,carbon1)
    print(oxy1*carbon1)



