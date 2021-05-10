f=open("stubasset.txt")
f1=open("24as.txt")
f2=open("stub24asset.txt",'a')

stubasset=set()
as24set=set()
stub24asset=set()

line = f.readline()

while line:
	tmp_list=line.split('\n')
	stubasset.add(int(tmp_list[0]))
	line = f.readline()

line = f1.readline()
while line:
	tmp_list=line.split('\n')
	as24set.add(int(tmp_list[0]))
	line =f1.readline()

if as24set.issubset(stubasset):
	print("yes")
	stub24asset = stubasset.difference(as24set)
else:
	print('no')
	stub24asset = stubasset.intersection(as24set)


stub24aslist = list(stub24asset)
stub24aslist.sort()

print("stub的数量是:",len(stub24aslist))
		
for AS in stub24aslist:
	f2.write(str(AS)+'\n')

f.close()
f1.close()
f2.close()


