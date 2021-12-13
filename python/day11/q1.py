def print_array(array):
    for i in array:
        print('\t'.join(map(str, i)))
    print()

def increment_neighbours(oct_energy, row_index,column_index, flashed):
    flashed[row_index][column_index] = 1
    for i,j in neighbours(oct_energy,row_index,column_index):
        if oct_energy[i][j] != 10:
            oct_energy[i][j]+=1
            if oct_energy[i][j] == 10:
                if not flashed[i][j]:
                    increment_neighbours(oct_energy, i, j, flashed)
                pass
    

def neighbours(array, i, j):
    neighbours = []
    for i1 in range(max(0,i-1), min(i+2,len(array))):
        for j1 in range(max(0,j-1), min(j+2, len(array[0]))):
            if (i1,j1)!=(i,j):
                neighbours.append((i1,j1))
    return neighbours

def Solution(file_content):
    oct_energy = []
    for line in file_content:
        oct_energy_column = [int(x.strip()) for x in line.strip()]
        oct_energy.append(oct_energy_column)
    # print_array(oct_energy)

    days = 100
    flash_counter = 0
    for day in range(1,days+1):
        flashed = [[0]*len(oct_energy[0]) for _ in range(len(oct_energy))]
        for row_index in range(len(oct_energy)):
            for column_index in range(len(oct_energy[0])):
                oct_energy[row_index][column_index]+=1
        
        for row_index in range(len(oct_energy)):
            for column_index in range(len(oct_energy[0])):
                if oct_energy[row_index][column_index] == 10:
                    if not flashed[row_index][column_index]:
                        increment_neighbours(oct_energy, row_index, column_index, flashed)

        for row_index in range(len(oct_energy)):
            for column_index in range(len(oct_energy[0])):
                if oct_energy[row_index][column_index] == 10:
                    oct_energy[row_index][column_index] = 0
                    flash_counter+=1
        
        # print("Day -", day)
        # print_array(oct_energy)

    
    # print_array(oct_energy)
    # print(flash_counter)
    return flash_counter