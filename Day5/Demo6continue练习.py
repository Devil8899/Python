#_author: liuz
#date: 2017/12/2
exit_flag=False

for i in range(10):
    if i<5:
        continue
    print(i)
    for j in range(10):
        print("level2",j)
        if j==6:
            exit_flag=False
            break
    if exit_flag:
        break