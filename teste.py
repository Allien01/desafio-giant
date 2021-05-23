import re
def sale
fhandle = open('text.txt')
invalid_input = 0
count = dict()
wrong_input = []
for line in fhandle:
    line = line.strip()
    if line.startswith("SIDE:"):
        pos = line.find(":")
        sale_pos = line.find(";", pos)
        fst_value = line[pos+1:sale_pos]