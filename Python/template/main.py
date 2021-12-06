import q1, q2
# Question 1
with open("test_input1.txt", "r+") as mf:
    file_content = mf.readlines()
    solution = q1.Solution(file_content)
    print(solution)

# with open("input1.txt", "r+") as mf:
#     file_content = mf.readlines()
#     solution = q1.Solution(file_content)
#     print(solution)

# Question 2
with open("test_input2.txt", "r+") as mf:
    file_content = mf.readlines()
    solution = q2.Solution(file_content)
    print(solution)

# with open("input2.txt", "r+") as mf:
#     file_content = mf.readlines()
#     solution = q2.Solution(file_content)
#     print(solution)