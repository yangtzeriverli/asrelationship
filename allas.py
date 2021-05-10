fr = open("asrelweuse.txt")
fw = open("allas.txt",'a')

allasset = set()

line = fr.readline()

tmp_list =[]


while line:
	tmp_list = line.split('|')
	allasset.add(int(tmp_list[0]))	
	allasset.add(int(tmp_list[1]))
	line = fr.readline()



allaslist = list(allasset)
allaslist.sort()

print("AS数量是:",len(allaslist))

for AS in allaslist:
	fw.write(str(AS)+'\n')


fr.close()
fw.close()
