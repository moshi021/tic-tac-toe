import time 

def main():
    
    import time
class Board:
    def __init__(self):
        self.cells=["" for i in range(9)]  
        
        
        
    def display_board(self):
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("------------")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("------------")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print("------------")
        
    
    def update_board(self,cell_no, player):
        if cell_no>0 and cell_no<10 and self.cells[cell_no-1]=='':
            self.cells[cell_no-1]=player
        else:
            print("INVALID ")
            return False
        
        return True

    
    def winner(self, player):
        combinations=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for combination in combinations:
            result=True
            for cell in combination:
                if self.cells[cell]!=player:
                    result=False
            if result==True:
                return True
        return False
                
       
    def reset(self):
        self.cells=["" for i in range(9)]
     
    
    def tie(self):
        count=0
        for i in self.cells:
            if i!="":
                count+=1
        if count==9:
            return True
        return False
                    
            
board=Board()            
            
def refresh_screen():
    print("Tic Tac Toe")
    time.sleep(0.05)
    board.display_board()
    


    
while True:
    refresh_screen()

    player1_input=int(input("Player 1, Please choose a cell between 1-9: "))

    
    while not  board.update_board(player1_input, 'X') :
        player1_input=int(input("Player 1, Please choose a cell between 1-9: "))
    
   
    #check_x_wins
    if board.winner('X'):
        refresh_screen()
        print("player1 wins")
        play_again=str(input("Wanna play again? Y/N : "))
        if play_again.upper()=="Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break
    
    
    #check_tie
    if board.tie():
        print("Its a tie")
        play_again=str(input("Wanna play again? Y/N : "))
        if play_again.upper()=="Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break
            
    refresh_screen()
    
    player2_input=int(input('Player 2, Please choose a cell between 1-9: '))
    while not  board.update_board(player2_input, 'O') :
        player2_input=int(input("Player 2, Please choose a cell between 1-9: "))
        
    #check_0_wins
    if board.winner("O"):
        refresh_screen()
        print('player2 wins')
        play_again=str(input("Wanna play again? Y/N : "))
        if play_again.upper()=="Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break
         
    
    
      
     #check_tie   
    if board.tie():

        print("Its a tie")
        play_again=str(input("Wanna play again? Y/N : "))
        if play_again.upper()=="Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break
        
        

if __name__ == "__main__":
    main()