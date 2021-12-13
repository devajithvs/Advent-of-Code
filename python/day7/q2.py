def find_fuel(crab_positions, value):
    total_fuel = 0
    for j in range(len(crab_positions)):
        difference = abs(value-crab_positions[j])
        total_fuel+=difference*(difference+1)//2
    return total_fuel
   
def Solution(file_content):
    crab_positions = [int(x.strip()) for x in file_content[0].split(",")]
    # sort the list
    # crab_positions.sort()

    # min_index = 0
    min_fuel = 9223372036854775807 # Largest integer possible, TODO: find a convenient way to find max_int

    max_position = max(crab_positions)
    min_position = min(crab_positions)
    for i in range(min_position, max_position+1):
        fuel = find_fuel(crab_positions, i)
        # print(fuel)
        if fuel < min_fuel:
            # min_index = i
            min_fuel = fuel
    
    # print(min_fuel)
    # print(min_index)
    return min_fuel
