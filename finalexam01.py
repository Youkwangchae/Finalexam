cnt =1
a = 1
b = 2
total = 0

print("i\tm(i)")
while cnt<902:
    c = 1/a*(-1)**b
    total = total + c
    if(cnt%100 ==1):
        print(cnt,"\t",round(4*total,4))
    a=a+2
    cnt = cnt+1
    b=b+1



    
