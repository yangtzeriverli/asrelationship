import time

time_start=time.time()

f=open("stub24asset.txt")
f1=open("stub24aspplink.txt")
f2=open("stub24asdegree.txt",'a')

stub24asset=set()
pplinkset=set()
stub24asdegree=set()


line = f.readline()

while line:
	tmp_list=line.split('\n')
	stub24asset.add(int(tmp_list[0]))
	line = f.readline()

line = f1.readline()
while line:
	tmp_list=line.split('|')
	pplinkset.add(  (int(tmp_list[0]),int(tmp_list[1]))  )
	line =f1.readline()
print("集合构建完成")
num=0
for enas in stub24asset:
	count=0
	#print("这是enas",enas)
	for link in pplinkset:
		#iprint("这是链路",link)
		if int(enas) == int(link[0]) or int(enas) == int(link[1]):
			count=count+1
			#print("符合条件")
	stub24asdegree.add((enas,count))
	num=num+1
	print("编号是:",num,"计算出来的as的度是:",enas,count)



#if as24set.issubset(stubasset):
#	print("yes")
#	stub24asset = stubasset.difference(as24set)
#else:
#	print('no')
#	stub24asset = stubasset.intersection(as24set)
#实际执行中走的是这个交集的步骤

#stub24aslist = list(stub24asset)
#stub24aslist.sort()

#print("stub的数量是:",len(stub24aslist))
		
for AS in stub24asdegree:
	f2.write(str(AS[0])+'|'+str(AS[1])+'\n')

f.close()
f1.close()
f2.close()

time_end=time.time()
print('time cost',time_end-time_start,'s')
