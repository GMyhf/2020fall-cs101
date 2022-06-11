# step 3
# s3_generate_class12_13Social.py

import sys
from collections import defaultdict 

def readGraph(f):
    g = defaultdict(list)
    with open(f, 'rt', encoding=sys.getfilesystemencoding()) as f:
        for ln in f:
            ln = ln.rstrip()    # remove '\n'
            ln = ln.split(":")
            u = ln[0].rstrip()
            u = dict_id[u]
            vv = ln[1].split()
            if len(vv) == 0:
                g[u].append(-1)     # no acquaintance. outdegree is 0.
            else:
                for v in vv:
                    v = dict_id[v]
                    g[u].append(v)

        return g
    
def readStuId(f):
    dict_stu_id = defaultdict(int)
    with open(f, 'r', encoding=sys.getfilesystemencoding()) as f:
        for ln in f:
            ln = ln.rstrip()    # remove '\n'
            ln = ln.split(",")
            dict_stu_id[ln[0]] = ln[-1]
    
    return dict_stu_id


dict_id = readStuId("stu_name_id.csv")
graph = readGraph("class12_13Social.raw.txt")        

with open('class12_13Social.txt', 'w', encoding=sys.getfilesystemencoding()) as f:
    for key in graph.keys():
        f.write("{} :".format(key))
        for i in graph[key]:
            f.write(" {}".format(i))
        f.write("\n")
f.close()
