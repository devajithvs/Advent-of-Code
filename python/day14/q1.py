def get_min_max(element_counter):
    min = element_counter[list(element_counter.keys())[0]]
    max = element_counter[list(element_counter.keys())[0]]
    for key in element_counter:
        if element_counter[key] > max:
            max = element_counter[key]
        if element_counter[key] < min:
            min = element_counter[key]
    return min, max

def Solution(file_content):
    starting_polymer = file_content[0].strip()
    polymer_rules = {}

    for line in file_content[2:]:
        line = line.strip()
        line = line.split("->")
        polymer_rules[line[0].strip()] = line[1].strip()
    
    polymer = starting_polymer[:]
    steps = 10
    for step in range(1, steps+1):
        index = 0
        while index < len(polymer)-1:
            if polymer[index:index+2] in polymer_rules:
                new_polymer = polymer[:index+1] + polymer_rules[polymer[index:index+2]] + polymer[index+1:]
                index+=1
            polymer = new_polymer
            index+=1
    
    element_counter = {}

    for value in polymer:
        if value in element_counter:
            element_counter[value]+=1
        else:
            element_counter[value] = 1
    
    min, max = get_min_max(element_counter)
    return max-min

