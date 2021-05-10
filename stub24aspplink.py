f=open("stub24asset.txt")
f1=open("pplink.txt")
f2=open("stub24aspplink.txt",'a')


stub24asset=set()

line = f.readline()

while line:
	tmp_list=line.split('\n')
	stub24asset.add(int(tmp_list[0]))
	line = f.readline()


line = f1.readline()
while line:
	tmp_list=line.split('|')
	if int(tmp_list[0]) in stub24asset and int(tmp_list[1]) in stub24asset:
		f2.write(line)
	line =f1.readline()



		

f.close()
f1.close()
f2.close()


