import collections
import heapq
import pprint
import sys

def get_neighbours(heights,location):
    Node = collections.namedtuple('Node', ['x','y'])
    max_x = len(heights[0])
    max_y = len(heights)
    if location.x > 0:
        yield (Node(location.x-1,location.y),heights[location.y][location.x-1])
    if location.y > 0:
        yield (Node(location.x,location.y-1),heights[location.y-1][location.x])
    if location.x < max_x - 1:
        yield (Node(location.x+1,location.y),heights[location.y][location.x+1])
    if location.y < max_y - 1:
        yield (Node(location.x,location.y+1),heights[location.y+1][location.x])

def increase_heights(heights):
    temp = []
    for line in heights:
        temp_line=[]
        for height in line:
            temp_line.append(height + 1 if height < 9 else 1)
        temp.append(temp_line)
    return temp

if __name__=="__main__":
    with(open("day15-input.txt")) as f:
        lines = f.readlines()
    pp = pprint.PrettyPrinter(width=200)
    temp_heights = [[]]
    for line in lines:
        temp_heights[0].append(list(map(int,list(line.strip()))))
        
    Node = collections.namedtuple('Node', ['x','y'])
    
    for i in range(1,10):
        temp_heights.append(increase_heights(temp_heights[i-1]))
    heights=[]
    for x in range(5):
        for l in range(len(temp_heights[0])):
            line = []
            for y in range(x,x+5):
                line.extend(temp_heights[y][l])
            heights.append(line)    

    max_x = len(heights[0])
    max_y = len(heights)
    risks = {Node(x,y): sys.maxsize for x in range(max_x) for y in range(max_y)}
    risks[Node(0,0)]=0
    pq = [(0, Node(0,0))]
    
    while len(pq) > 0:
        current_risk, current_node = heapq.heappop(pq)

        if current_risk > risks[current_node]:
            continue

        for neighbor, risk in get_neighbours(heights,current_node):
            new_risk = current_risk + risk
            if new_risk < risks[neighbor]:
                risks[neighbor]=new_risk
                heapq.heappush(pq, (new_risk, neighbor))

    pprint.pprint(risks[Node(max_x-1,max_y-1)])

