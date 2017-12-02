N1=int(input('数字1>>:'))
N2=int(input('数字2>>:'))
N3=int(input('数字3>>:'))
Min_num=0
#注意缩进级别
if N1<N2:
   Min_num=N1
   if Min_num <N3:
    print("Min_num is ",Min_num)
   else :
    print("Min_num is",N3)
else :
   Min_num=N2
   if Min_num < N3:
    print("Min_num is ",Min_num)
   else :
    print("Min_num is",N3)