# step 5
# s5_print_cypher.py

import sys
    
class_social_file = "class12_13Social.txt"
outdegree0 = set()

# print cypher script for neo4j

entity = ["//Create entities"]
relation = ["//Create relations between entities"]
relation.append("\nMATCH (a:Class),(b:Class)\n WHERE ")
rel_detail = []   
with open(class_social_file, 'r', encoding=sys.getfilesystemencoding()) as f:
    for ln in f:
        ln = ln.rstrip()    # remove '\n'
        ln = ln.split(":")
        u = int(ln[0].rstrip())
        entity.append(f"CREATE (s{u}:Class{{name:'{u}'}})")
        
        vv = ln[1].split()
        if vv[0] == '-1':     # no acquaintance. outdegree is 0.
        #if len(vv) == 0:
            outdegree0.add(u)
        else:            
            rel_detail.append(f"a.name='{u}' AND b.name in {vv}")  
                
relation.append('\nOR '.join(rel_detail))
relation.append("\nCREATE (a)-[r:know]->(b)")
relation.append("\nRETURN type(r)")

# python3 print_cypher.py > 1213output.log
print('\n'.join(entity))
print()
print(*relation)


# in neo4j Sandbox
# https://stackoverflow.com/questions/23310114/how-to-reset-clear-delete-neo4j-database
# delete all nodes with relationships
#   match (a) -[r] -> () delete a, r
# delete nodes that have no relationships
#   match (a) delete a

# run 1213output.log
