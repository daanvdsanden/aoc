if __name__ =="__main__":
    with(open("day9-input.txt")) as f:
        heightmap = [ [int(x) for x in line.strip()] for line in f.readlines() ]
    
    height = len(heightmap)
    width = len(heightmap[0])
    heightmap.insert( 0, [10]*width )
    heightmap.append( [10]*width )
    heightmap = [ [10] + x + [10] for x in heightmap ]
    
    points = []
    for x in range(1,height+1):
        for y in range(1,width+1):
            surrounding = [
                    heightmap[x-1][y], heightmap[x+1][y],
                    heightmap[x][y-1], heightmap[x][y+1],
            ]
            if all([heightmap[x][y] < i for i in surrounding ]):
                points.append(heightmap[x][y])

    print(sum(points)+len(points))



