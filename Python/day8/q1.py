def Solution(file_content):
    unique_digits = 0
    for line in file_content:
        output = line.split(" | ")
        unique_pattern = [x.strip() for x in output[0].split(" ")]
        four_digit_code = [x.strip() for x in output[1].split(" ")]

        for i in four_digit_code:
            if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                unique_digits+=1
    
    return unique_digits