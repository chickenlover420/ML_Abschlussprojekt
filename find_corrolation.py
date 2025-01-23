with open('corrolation.csv', 'r') as file:
    lines = file.readlines()

line_one = lines[0]
line_list = line_one.strip().split(' ')
for element in line_list:
    if len(element) == 0:
        line_list.remove(element)
print(line_list)                            #??????????????

































#Alle Zahlen in Floats umwandeln
for i in range(len(lines)):
    lines[i] = lines[i].strip().split(' ')
    try:
        for x in range(len(lines[i])):
            lines[i][x] = float(lines[i][x])
    except ValueError:
        continue

#Alle Strings aus liste löschen
    for x in lines[i]:
        if isinstance(x, str):
            lines[i].remove(x)
