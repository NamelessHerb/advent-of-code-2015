import pandas as pd

lights = pd.DataFrame(0,index=range(1000), columns = range(1000))

with open('Day_6.txt','r') as file_object:
    instructions = file_object.read()

cutted = instructions.splitlines()

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
        sub_light[:] = 1
    elif trigger == "off":
        sub_light[:] = 0
    elif trigger == "toggle":
        sub_light[:] = 1 - sub_light

light_num = lights.sum().sum()

print(light_num)