def Solution(file_content):
    input = file_content[0].split(":")[-1].split(",")
    x_coord = [int(x) for x in input[0].split("=")[-1].split("..")]
    y_coord = [int(y) for y in input[-1].split("=")[-1].split("..")]

    y_elem = []
    x_elem = []
    # This only works if final position is negative, did not think about positive positions
    for vel in range(min(y_coord), -min(y_coord)):
        if check_in_y_range(y_coord, vel):
            y_elem.append(vel)

    min_x = int((2*x_coord[0]-1)**(0.5))
    for vel in range(min_x, max(x_coord)+1):
        if check_in_x_range(x_coord, vel):
            x_elem.append(vel)
    
    counter = 0
    for x in x_elem:
        for y in y_elem:
            velocity = [x, y]
            if check_in_both_range(velocity, x_coord, y_coord):
                counter+=1
    return counter

def check_in_x_range(x_target, x_vel):
    step = 0
    current_point = 0
    while current_point <= x_target[0]:
        step+=1
        current_point+=x_vel
        if current_point <= x_target[1] and current_point >= x_target[0]:
            return step
        if x_vel>0:
            x_vel-=1
        if x_vel == 0:
            return False
        
    return False

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

def check_in_both_range(velocity, x_range, y_range):
    current_position = [0,0]
    current_velocity = velocity[:]

    while True:
        current_position[0]+=current_velocity[0]
        current_position[1]+=current_velocity[1]
        
        if x_range[0] <= current_position[0] <= x_range[1] and y_range[0] <= current_position[1] <= y_range[1]:
            return True
        
        if current_position[0] > x_range[1] or current_position[1] < y_range[0]:
            return False

        if current_velocity[0] > 0:
            current_velocity[0]-=1
        
        current_velocity[1]-=1