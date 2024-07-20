#Om namah shivaya
for _ in range(int(input())):
    games,time,rest = map(int,input().split())
    total_time = 0
    counter = 0
    while(games>0):
        total_time+=time 
        counter+=1 
        games-=1
        if counter==3 and games>0:
            counter = 0
            total_time+=rest
    print(total_time)