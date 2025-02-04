import pandas as pd
import numpy as np


lights = pd.DataFrame(0,index=range(1000), columns = range(1000))

with open('Day_6.txt','r') as file_object:
    instructions = file_object.read()

cutted = instructions.splitlines()
#首先把input分成不同行，然后对每一个行进行单独处理

for itr in cutted:
    parts = itr.split()
    if parts[0] == 'turn':
        trigger = parts[1]
        start = list(map(int,parts[2].split(",")))
        end = list(map(int,parts[4].split(",")))
    else:
        trigger = 'toggle'
        start = list(map(int,parts[1].split(",")))
        end = list(map(int,parts[3].split(",")))

    sub_light = lights.loc[start[0]:end[0],start[1]:end[1]]

    if trigger == "on":
        sub_light[:] +=1
    elif trigger == "off":
        sub_light[:] = np.maximum(0,sub_light-1)
        #maximum需要np来让sublight可以直接参与运算
    elif trigger == "toggle":
        sub_light[:] += 2



light_num = lights.sum().sum()
#一个sum等于所有列各自相加，单独输出每一列各自的和，两个sum等于全体求和
#I know these comments look like AI generated, but they are just my personal note :)

print(light_num)


