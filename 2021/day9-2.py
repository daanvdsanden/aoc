def get_basin(heightmap, visited, x, y):
    visited[x][y] = True
    basin = 1
    if not visited[x-1][y] and heightmap[x-1][y] < 9:
        basin+=get_basin(heightmap, visited, x-1,y)
    if not visited[x+1][y] and heightmap[x+1][y] < 9:
        basin+=get_basin(heightmap, visited, x+1,y)
    if not visited[x][y-1] and heightmap[x][y-1] < 9:
        basin+=get_basin(heightmap, visited, x,y-1)
    if not visited[x][y+1] and heightmap[x][y+1] < 9:
        basin+=get_basin(heightmap, visited, x,y+1)
    return basin


if __name__ =="__main__":
    with(open("day9-input.txt")) as f:
        heightmap = [ [int(x) for x in line.strip()] for line in f.readlines() ]
    
    height = len(heightmap)
    width = len(heightmap[0])
    heightmap.insert( 0, [10]*width )
    heightmap.append( [10]*width )
    heightmap = [ [10] + x + [10] for x in heightmap ]
   

    visited = [[ False for _ in range(width+2) ] for _ in range(height+2)]
    basins = []
    for x in range(1,height+1):
        for y in range(1,width+1):
            surrounding = [
                    heightmap[x-1][y], heightmap[x+1][y],
                    heightmap[x][y-1], heightmap[x][y+1],
            ]
            if all([heightmap[x][y] < i for i in surrounding ]):
                basin_size = get_basin(heightmap, visited, x, y)
                basins.append(basin_size)
    largest = sorted(basins)

    print(largest[-3]*largest[-2]*largest[-1])



