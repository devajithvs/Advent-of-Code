def Solution(file_content):
    sum_of_digits = 0
    for line in file_content:
        output = line.split(" | ")
        unique_pattern = [x.strip() for x in output[0].split(" ")]
        four_digit_code = [x.strip() for x in output[1].split(" ")]

        digit_dict = {}
        for i in unique_pattern:
            if len(i) == 2:
                digit_dict[1] = i
            elif len(i) == 3:
                digit_dict[7] = i
            elif len(i) == 4:
                digit_dict[4] = i
            elif len(i) == 7:
                digit_dict[8] = i
        unique_pattern.remove(digit_dict[1])
        unique_pattern.remove(digit_dict[4])
        unique_pattern.remove(digit_dict[7])
        unique_pattern.remove(digit_dict[8])
        for i in unique_pattern:
            if len(i) == 5:
                if set(digit_dict[1]) <= set(i):
                    digit_dict[3] = i
            if len(i) == 6:
                if set(digit_dict[4]) <= set(i):
                    digit_dict[9] = i
        unique_pattern.remove(digit_dict[3])
        unique_pattern.remove(digit_dict[9])
        for i in unique_pattern:
            if len(i) == 6:
                if set(digit_dict[1]) <= set(i):
                    digit_dict[0] = i
        unique_pattern.remove(digit_dict[0])
        for i in unique_pattern:
            if len(i) == 6:
                digit_dict[6] = i
        unique_pattern.remove(digit_dict[6])
        for i in unique_pattern:
            if len(set((digit_dict[6])) - set(i)) == 1:
                digit_dict[5] = i
        unique_pattern.remove(digit_dict[5])
        digit_dict[2] = unique_pattern[0]
        
        actual_code = ""
        for digit  in four_digit_code:
            for key in digit_dict:
                if set(digit) == set(digit_dict[key]):
                    actual_code+=str(key)
                    break
        # print(int(actual_code))
        sum_of_digits += int(actual_code)

    return sum_of_digits