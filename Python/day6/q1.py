def Solution(file_content):
    lantern_numbers = [int(x.strip()) for x in file_content[0].split(",")]
    lantern_dict = {}
    for i in range(9):
        lantern_dict[i] = 0
    for x in lantern_numbers:
        lantern_dict[x]+=1
    
    days = 80
    for day in range(1,days+1):
        new_lantern_dict = lantern_dict.copy()
        for key in lantern_dict:
            if key > 0:
                new_lantern_dict[key-1] = lantern_dict[key]
        new_lantern_dict[6] += lantern_dict[0]
        new_lantern_dict[8] = lantern_dict[0]

        lantern_dict = new_lantern_dict
    total = sum(lantern_dict.values())
    return total