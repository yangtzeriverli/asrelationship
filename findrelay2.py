def IsKconnected(element,R_can):
#	print("IsKconnected is invoked")
	count=0
	if len(R_can) == 0:
		return True
	else:
		#就是要看这个element加入到R_can中后是否依旧是k连接的
		for r in R_can:
			tmp1=(int(element),int(r))
			tmp2=(int(r),int(element))
			if tmp1 in pplinkset or tmp2 in pplinkset:
				count=count+1
				print("+1")
		if count < k:
			return False
		else:
			print("true")
			return True
		


f=open("stub24asset2.txt")
f1=open("stub24aspplink2.txt")
#f2=open("stub24aspplink.txt",'a')

N=2
k=1

stub24asset=set()
pplinkset=set()

R_can=set()
Rs=set()
R_scens=set()


line = f.readline()

while line:
	tmp_list=line.split('\n')
	stub24asset.add(int(tmp_list[0]))
	line = f.readline()
#此时得到了全部的候选AS--就是R

print(stub24asset)

line = f1.readline()
while line:
	tmp_list=line.split('|')
	pplinkset.add((int(tmp_list[0]),int(tmp_list[1])))
	line = f1.readline()

print("The num of link is:",len(pplinkset))
print(pplinkset)
	
#这里只要找到一个满足条件的cluster就会退出程序
while len(R_can) <= N:
	print("外循环是",R_can)
	for element in stub24asset.difference(R_can):
		print("差集是",stub24asset.difference(R_can))
		print(element)
		if IsKconnected(element,R_can):
			R_can.add(int(element))
			print("加入的元素是:",element)
			print("内循环是：",R_can)
	stub24asset=stub24asset.difference(R_can)
	R_can.clear()
	#R_can.add(findn)


#line = f1.readline()
#while line:
#	tmp_list=line.split('|')
#	if int(tmp_list[0]) in stub24asset and int(tmp_list[1]) in stub24asset:
#		f2.write(line)
#	line =f1.readline()



		

f.close()
f1.close()
#f2.close()


