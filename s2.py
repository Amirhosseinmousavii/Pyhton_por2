import random
name=input("input username:")
password=input("input password:")
li=["shir","khat"]
if name=="amirhossein" and password=="14002310":
        computer1_point=computer2_point=0
        turn=1
        while True:
            print(f"points computer1 : {computer1_point} , computer2 : {computer2_point}")
            if computer1_point==5:
                print("computer1 win")
                break
            if computer2_point==5:
                print("computer2 win")
                break
            player1=random.randint(0,1)
            player2=random.randint(0,1)
            if turn==1:
                print(f"guess  computer1 : {li[player1]} > select computer2 : {li[player2]}")
            if turn==2:
                print(f"guess  computer2 : {li[player2]} > select computer1 : {li[player1]}")
            if turn==1 and player1==player2:
                computer1_point+=1
                turn=2
                continue
            else:
                computer2_point+=1
                turn=2
                continue
            if turn==2 and player1==player2:
                computer2_point+=1
                turn=1
                continue
            else:
                computer1_point+=1
                turn=1





