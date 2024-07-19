#Om Namah Shivaya
for _ in range(int(input())):
    msg = input()
    msg = msg.replace(" ","")
    if msg =="</>":
        print("Error")
    else:
        front = msg[:2]
        back = msg[len(msg)-1]
        tagsOK = (front=="</" and back==">")
        bodyOK = True
        for i in range(2,len(msg)-1):
            if msg[i] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                bodyOK = False
                break 
        if(tagsOK and bodyOK):
            print("Success")
        else:
            print("Error")
    