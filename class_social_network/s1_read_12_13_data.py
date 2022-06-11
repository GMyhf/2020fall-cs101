# step 1
# s1_read_12_13_data.py

import sys
import pandas as pd
from collections import defaultdict 

# https://www.codespeedy.com/breadth-first-search-algorithm-in-python/
def bfs(graph, initial):    
    visited = []    
    queue = [initial]
 
    while queue:        
        node = queue.pop(0)
        if node not in visited:            
            visited.append(node)
            
            if node not in graph:
                continue
            
            neighbours = graph[node] 
            
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

# https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python
# https://www.codespeedy.com/depth-first-search-algorithm-in-python/
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        if node not in graph:
                return visited
            
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


## process data

# filename = '101648953_0_poll_68_68.xlsx'
# There are 67 students
# bfs: the lenghth of the longest path is 52
# dfs: the lenghth of the longest path is 52
# filename = '101648953_0_poll_104_104.xlsx'
# There are 103 students
# bfs: the lenghth of the longest path is 76
# dfs: the lenghth of the longest path is 76
# filename = '101648953_0_poll_118_118.xlsx'
# There are 116 students
# bfs: the lenghth of the longest path is 79
# dfs: the lenghth of the longest path is 79
filename = '101648953_0_poll_119_119.xlsx'
# There are 117 students
# bfs: the lenghth of the longest path is 79
# dfs: the lenghth of the longest path is 79

df = pd.read_excel(filename, usecols=[6, 7, 8, 10, 12, 14])
                   #, encoding=sys.getfilesystemencoding())
data = df.values
print("There are {} students.".format(len(data)))

## create graph
graph = {}
isolated_vertex = defaultdict(str)
  

for i in range(len(data)):
    if data[i][0] not in graph:
        neighbours = data[i][2:]
        neis = filter(lambda x: x != '(Пе)', neighbours) 
        neis = list(map(int, neis))
        if len(neis) == 0:
            isolated_vertex[data[i][0]] = data[i][1]
            graph[data[i][0]] = []
        else:
            graph[data[i][0]] = neis

with open('class12_13Social.raw.txt', 'w', encoding=sys.getfilesystemencoding()) as f:
    for key in graph.keys():
        f.write("{} :".format(key))
        for i in graph[key]:
            f.write(" {}".format(i))
        f.write("\n")
f.close()

ids = sorted(graph)

## bfs travel
maxp = 0
for i in ids:
    bfs_path = bfs(graph, i)
    maxp = max(maxp, len(bfs_path))
    #print(len(bfs_path), bfs_path)

#print("bfs: the lenghth of the longest path is {}".format(maxp))


## dfs travel
maxp = 0
for i in ids[::-1]:
    dfs_path = dfs(graph, i, [])
    maxp = max(maxp, len(dfs_path))
    #print(len(dfs_path), dfs_path)
    
print("dfs: the lenghth of the longest path is {}".format(maxp))
