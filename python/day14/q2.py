def get_min_max(element_counter):
    min = element_counter[list(element_counter.keys())[0]]
    max = element_counter[list(element_counter.keys())[0]]
    for key in element_counter:
        if element_counter[key] > max:
            max = element_counter[key]
        if element_counter[key] < min:
            min = element_counter[key]
    return min, max

def increment_dict(d, key, incr):
    if key in d:
        d[key]+=incr
    else:
        d[key]=incr

def Solution(file_content):
    starting_polymer = file_content[0].strip()
    polymer_rules = {}

    for line in file_content[2:]:
        line = line.strip()
        line = line.split("->")
        polymer_rules[line[0].strip()] = line[1].strip()
    
    element_counter = {}
    for value in starting_polymer:
        increment_dict(element_counter, value, 1)

    polymer = {}
    index = 0
    while index < len(starting_polymer)-1:
        polymer_pair = starting_polymer[index:index+2]
        increment_dict(polymer, polymer_pair, 1)
        index+=1
    
    steps = 40
    for _ in range(1, steps+1):
        new_polymer = {}
        for key in polymer.copy():
            if key in polymer_rules:
                increment_dict(element_counter, polymer_rules[key], polymer[key])

                new_pairs = [key[0]+polymer_rules[key], polymer_rules[key]+key[-1]]
                for new_pair in new_pairs:
                    increment_dict(new_polymer, new_pair, polymer[key])

        polymer = new_polymer
    
    min, max = get_min_max(element_counter)
    return max-min
