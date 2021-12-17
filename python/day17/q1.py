def Solution(file_content):
    input = file_content[0].split(":")[-1].split(",")
    x_coord = [int(x) for x in input[0].split("=")[-1].split("..")]
    y_coord = [int(y) for y in input[-1].split("=")[-1].split("..")]

    for vel in range(min(y_coord), -min(y_coord)-1):
        if check_in_y_range(y_coord, vel):
            initial_y = vel
    
    current_y = initial_y
    
    return get_max_y(current_y)

def get_max_y(y_vel):
    y_pos = 0
    y_prev=y_pos-1
    while y_pos - y_prev > 0:
        y_prev = y_pos
        y_pos+=y_vel
        y_vel-=1
    if y_pos == 0:
        return 0
    return y_prev

def check_in_y_range(y_target, y_vel):
    step = 0
    current_point = 0
    while current_point >= y_target[0]:
        if current_point <= y_target[1]:
            return step 
        step+=1
        current_point+=y_vel
        y_vel-=1
        
    return False