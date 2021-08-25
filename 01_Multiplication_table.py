#九九乘法表
 
for i in range(1,10):
    for j in range(1,10):
        print("{}X{}={}".format(j,i,j*i),end = "\t")
    print("\n")
