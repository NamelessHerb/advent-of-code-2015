with open('Day_1.txt','r') as file_object:
    floor = file_object.read()

loc = 0

for count in floor:
    if count == '(':
        loc += 1
    else:
        loc -= 1

print(loc)