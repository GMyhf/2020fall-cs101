# step 2
# s2_dict_stu_id.py

import sys
import pandas as pd
from collections import defaultdict 

class12 = '20201218_12class_xkmd.xls'
class13 = '20201218_13class_xkmd.xls'

df = pd.read_excel(class12, usecols=[0, 1, 8])
data12 = df.values

print("There are {} students in class 12.".format(len(data12)))
df = pd.read_excel(class13, usecols=[0, 1, 8])
data13 = df.values
print("There are {} students in class 13.".format(len(data13)))

dict_stu_id = defaultdict(list)
cnt = XX    # anonymous processing 
for i in range(len(data12)):
    if data12[i][2] == 'y':
        cnt += 1
        continue
    
    dict_stu_id[data12[i][0]] = [data12[i][1], cnt]
    cnt += 1

for i in range(len(data13)):
    dict_stu_id[data13[i][0]] = [data13[i][1], cnt]
    cnt += 1

with open('stu_name_id.csv', 'w', encoding=sys.getfilesystemencoding()) as f:
    for key in dict_stu_id.keys():
        f.write("{},{},{}\n".format(key, *(dict_stu_id[key])))
