f=open("allas.txt")
f1=open("providerasset.txt")
f2=open("stubasset.txt",'a')

allasset=set()
providerasset =set()
stubasset=set()

line = f.readline()

while line:
	tmp_list=line.split('\n')
	allasset.add(int(tmp_list[0]))
	line = f.readline()

line = f1.readline()
while line:
	tmp_list=line.split('\n')
	providerasset.add(int(tmp_list[0]))
	line =f1.readline()

if providerasset.issubset(allasset):
	print("yes")
	stubasset = allasset.difference(providerasset)
else:
	print('no')



stubaslist = list(stubasset)
stubaslist.sort()

print("stub的数量是:",len(stubaslist))
		
for AS in stubaslist:
	f2.write(str(AS)+'\n')

f.close()
f1.close()
f2.close()


