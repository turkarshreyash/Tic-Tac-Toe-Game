import os
from random import randint
play= 'YES'
print("---------------TIC TAC TOE----------------")
while(play.lower() == 'yes'):
    p1 = input("Enter Name for Player : ")
    p2 = input("Enter Name for Player : ")
    turn1 = randint(0,1)
    if turn1 :
        player1 = p1
        player2 = p2
    else :
        player1 = p2
        player2= p1
    print(f"TOSS! {player1} has won the Toss and would play fisrt :")
    board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    
    def printb():
        os.system( 'cls' )
        print("---------------TIC TAC TOE----------------")
        for i in range(7,0,-3):
            print(f"\t\t\t{board[i]}|{board[i+1]}|{board[i+2]}")
            if i is 7 or i is 4:
                print("\t\t\t-|-|-")
    def win(player):
            hori = (player == board[1]  == board[2] == board[3] or player == board[4]  == board[5] == board[6] or player == board[7]  == board[8] == board[9])
            verti = (player == board[1]  == board[4] == board[7] or player == board[2]  == board[5] == board[8] or player == board[3]  == board[6] == board[9])
            cross = (player == board[1]  == board[5] == board[9] or player == board[3]  == board[5] == board[7])
            return hori or verti or cross
    while(True):
        X = int(input(f"{player1} Choose Position : "))
        while not X in range(1,10,1) or not board[X]==' ':
            X = int(input(f"That's Unfair {player1} Choose Position Again : "))
        board[X] ='X'
        printb()
        if win('X'):
            print(f"{player1} Wins!!")
            break
        if not ' ' in board.values():
            print(f"TIE BETWEEN {player1} and {player2}")
            break
        O = int(input(f"{player2} Choose Position : "))
        while not O in range(1,10,1) or not board[O] == ' ':
            O = int(input(f"That's Unfair {player2} Choose Position Again : "))
        board[O] ='O'
        printb()
        if win('O'):
            print(f"{player2} Wins!!")
            break
    play = input("Yes to Play again!\nNo To Quite!\n")
        
