import random
name=input("input username:")
password=input("input password:")
li=["sang","kaqaz","qeychi"]
def game(s1,s2):
    if s1=="sang" and s2=="qeychi":
        return 1
    if s1=="sang" and s2=="sang":
        return 0
    if s1=="sang" and s2=="kaqaz":
        return -1
    if s1=="kaqaz" and s2=="qeychi":
        return -1
    if s1=="kaqaz" and s2=="sang":
        return 1
    if s1=="kaqaz" and s2=="kaqaz":
        return 0
    if s1=="qeychi" and s2=="qeychi":
        return 0
    if s1=="qeychi" and s2=="sang":
        return -1
    if s1=="qeychi" and s2=="kaqaz":
        return 1
if name=="amirhossein" and password=="14002310":
    select=int(input("1-computer\n2-another player\n"))
    if select==1:
        your_point=computer_point=0
        while True:
            print(f"points you : {your_point} , computer : {computer_point}")
            if your_point==5:
                print("you win")
                break
            if computer_point==5:
                print("you lose and computer win")
                break
            player1=int(input("1-sang\n2-kaqaz\n2-qeychi\n"))
            player1-=1
            player2=random.randint(0,2)
            g=game(li[player1],li[player2])
            print(f"selection  you : {li[player1]} , computer : {li[player2]}")
            if g==1:
                your_point+=1
            elif g==-1:
                computer_point+=1
    if select==2:
        your_point=another_point=0
        while True:
            print(f"points you : {your_point} , another_point : {another_point}")
            if your_point==5:
                print("you win")
                break
            if another_point==5:
                print("you lose and another win")
                break
            player1=int(input("you turn\n1-sang\n2-kaqaz\n2-qeychi\n"))
            player1-=1
            player2=int(input("another player turn\n1-sang\n2-kaqaz\n2-qeychi\n"))
            player2-=1
            g=game(li[player1],li[player2])
            print(f"selection  you : {li[player1]} , another : {li[player2]}")
            if g==1:
                your_point+=1
            elif g==-1:
                another_point+=1



