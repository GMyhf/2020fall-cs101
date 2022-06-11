# step 4
# s4_KosarajuAlgorithm.py
# skip this step if we do not need SCCs.

# https://www.geeksforgeeks.org/strongly-connected-components/
# Python implementation of Kosaraju's algorithm to print all SCCs 

import sys
from collections import defaultdict 

#This class represents a directed graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A function used by DFS 
	def DFSUtil(self,v,visited): 
		# Mark the current node as visited and print it 
		visited[v]= True
		print (v, end=" ") 
		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.DFSUtil(i,visited) 

	def fillOrder(self,v,visited, stack): 
		# Mark the current node as visited 
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 
		stack = stack.append(v) 
	
	# Function that returns reverse (or transpose) of this graph 
	def getTranspose(self): 
		g = Graph(self.V) 

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph: 
			for j in self.graph[i]: 
				g.addEdge(j,i) 
		return g 

	# The main function that finds and prints all strongly 
	# connected components 
	def printSCCs(self): 
		
		stack = [] 
		# Mark all the vertices as not visited (For first DFS) 
		visited =[False]*(self.V) 
		# Fill vertices in stack according to their finishing 
		# times 
		for i in range(self.V): 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 

		# Create a reversed graph 
		gr = self.getTranspose() 
		
		# Mark all the vertices as not visited (For second DFS) 
		visited =[False]*(self.V) 

		# Now process all vertices in order defined by Stack 
		while stack: 
			i = stack.pop() 
			if visited[i]==False: 
				gr.DFSUtil(i, visited) 
				print() 

# Create a graph given in the above diagram 
class_social_file = "class12_13Social.txt"
outdegree0 = set()
g = Graph(200)      # there are 116 lines in class12_13Social.txt

with open(class_social_file, 'r', encoding=sys.getfilesystemencoding()) as f:
    for ln in f:
        ln = ln.rstrip()    # remove '\n'
        ln = ln.split(":")
        u = int(ln[0].rstrip())
        vv = [int(x) for x in ln[1].split()]
        if vv[0] == -1:     # no acquaintance. outdegree is 0.
        #if len(vv) == 0:
            outdegree0.add(u)
        else:            
            for v in vv:
                g.addEdge(u, v)


'''
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
'''

print ("Following are strongly connected components in given graph") 
g.printSCCs() 
