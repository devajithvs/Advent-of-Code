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
                return 0
    return stack

def Solution(file_content):
    score_dict = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    complement = {
        "(":")", 
        "[":"]", 
        "{":"}",
        "<":">",
    }

    total_score = []
    for chunk in file_content:
        chunk = chunk.strip("\n")
        remaining_chars = get_first_bad_char(chunk)
        if remaining_chars:
            score = 0
            for remaining_char in reversed(remaining_chars):
                score = score*5 + score_dict[complement[remaining_char]]
            remaining_chars = []
            total_score.append(score)
    
    total_score.sort()
    median_index = len(total_score)//2
    median_value = total_score[median_index]
    return median_value