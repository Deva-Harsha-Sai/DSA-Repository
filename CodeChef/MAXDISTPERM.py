for _ in range(int(input())):
    num = int(input())
    ls1 = [x for x in range(1,num+1)]
    ls2 = []
    for i in ls1:
        ls2.append(i)
    steps = (len(ls1))//2 
    while steps>0:
        x = ls2.pop()
        ls2.insert(0,x)
        steps-=1
        
    for i in ls1:
        print(i,end=" ")
    print()
    for i in ls2:
        print(i,end=" ")
    print()