with open("input2_day1.txt", "r+") as mf:
    file_content = mf.readlines()
    prev_no = float(file_content[0].strip())
    counter = 0

    numbers2 = []
    length = len(file_content)
    for i in range(2, length):
        new_number = float(file_content[i].strip()) + float(file_content[i-1].strip()) + float(file_content[i-2].strip())
        numbers2.append(new_number)
    
    prev_no = numbers2[0]
    for number in numbers2[1:]:
        print(prev_no, number)
        if number > prev_no:
            counter+=1
        prev_no = number
    print(counter)

