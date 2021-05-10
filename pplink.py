fr = open("asrelweuse.txt")
fw = open("pplink.txt",'a')

line = fr.readline()
num = 0
tmp_list =[]

while line:
	tmp_list = line.split('|')
	if tmp_list[2] == '0':
		fw.write(line)
	line = fr.readline()
fr.close()
fw.close()
