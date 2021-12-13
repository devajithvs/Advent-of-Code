def find_fuel(crab_positions, value):
    total_fuel = 0
    for j in range(len(crab_positions)):
        total_fuel+=abs(value-crab_positions[j])
    return total_fuel

def Solution(file_content):
    crab_positions = [int(x.strip()) for x in file_content[0].split(",")]
    # sort the list
    crab_positions.sort()

    median_index = len(crab_positions)//2
    median_value = crab_positions[median_index]
    # print(median_value)
    fuel = find_fuel(crab_positions, median_value)
    # print(fuel)
    return fuel

   