#Om Namah Shivaya
for _ in range(int(input())):
    size,num = map(int,input().split())
    ls = list(map(int,input().split()))
    oddscount = 0
    for i in ls:
        if i%2!=0:
            oddscount+=1 
    if(oddscount==size):
        print(0)
    elif(oddscount==0 and num%2==0):
        print(-1)
    else:
        if(num%2==0):
            print(size-oddscount)
        else:
            x = size-oddscount 
            if x%2==0:
                print(x//2)
            else:
                print((x//2)+1)