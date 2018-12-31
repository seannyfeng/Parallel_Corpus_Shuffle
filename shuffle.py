from random import shuffle
import datetime
import os
print(datetime.datetime.now())
print("start")
tgt_in = "trainZH.txt"
tgt_out = "trainZH.s.txt"
src_in = "trainEN.txt"
src_out = "trainEN.s.txt"
lines=[]
with open (src_in) as f:
	line_count = 0
	for line in f:
		line_count += 1
		lines.append(line)
print(datetime.datetime.now())
print("finish reading")		
line_numbers = list(range(0,line_count))
print(datetime.datetime.now())
print("created list")
shuffle(line_numbers)
print(datetime.datetime.now())
print("shuffled list")
ft_out= open(src_out,"a+")
for i in range(len(line_numbers)):
	ln=line_numbers[i]
	ft_out.write(lines[ln])
ft_out.close()
lines=[]
with open (tgt_in) as f:
	line_count = 0
	for line in f:
		line_count += 1
		lines.append(line)
ft_out= open(tgt_out,"a+")
for i in range(len(line_numbers)):
	ln=line_numbers[i]
	ft_out.write(lines[ln])
ft_out.close()				
print(datetime.datetime.now())
print("finished")
