f=open("asrelweuse.txt")
f1=open("providerasset.txt",'a')

providerasset =set()

line = f.readline()

while line:
	tmp_list=line.split('|')
	if tmp_list[2] == '-1':
		providerasset.add(int(tmp_list[0]))
	line = f.readline()

provideraslist = list(providerasset)
provideraslist.sort()

print("provider的数量是:",len(provideraslist))
		
for AS in provideraslist:
	f1.write(str(AS)+'\n')

f.close()
f1.close()


