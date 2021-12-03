import operator

def read_input(filename):
    with open(filename) as f:
        readings = f.readlines()
    return list(map(str.strip,readings))

def return_reading(readings, position, compare):
    if len(readings) == 1:
        return int(readings[0],2)

    temp_reading = 0

    for reading in readings:
        temp_reading += int(reading[position])
    
    filtered = '1' if compare(temp_reading,len(readings)/2) else '0' 

    return return_reading([x for x in readings if x[position]==filtered ] ,position+1, compare)


if __name__ == "__main__":
    readings = read_input("day3-input.txt")
    
    print(return_reading(readings,0,operator.ge) * return_reading(readings,0,operator.lt))

