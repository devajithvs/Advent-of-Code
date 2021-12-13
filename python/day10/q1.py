def get_first_bad_char(chunk):
    stack = []
    complement = {
        "(":")", 
        "[":"]", 
        "{":"}",
        "<":">",
    }
    for char in chunk:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            final_char = complement[stack.pop()]
            if final_char != char:
                return char
    return -1

def Solution(file_content):
    penalty_dict = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    penalty = 0
    for chunk in file_content:
        chunk = chunk.strip("\n")
        print(chunk)
        bad_char = get_first_bad_char(chunk)
        print(bad_char)
        if bad_char != -1:
            penalty += penalty_dict[bad_char]
    
    print(penalty)
    return penalty