class TicTacToe:

    def __init__(self):
        self.board = self.make_board()     

    def make_board(self):
        return [0 for _ in range(9)]

    def board(self):
        return self.board

    def set_board(self,location,xORo):
        self.board[location]=xORo

    def show_options(self):             #show user what the numbers are
        [print() for _ in range(20)]
        for num in range(9,0,-3):
            print('          ',num-2,'|',num-1,'|',num)
            if num>3:
                print('           ---------')
        print("\nWhich number would you like?")
        [print() for _ in range(5)] 

    def show_board(self):               #show game board with positions on it
        [print() for _ in range(20)]
        self.show_options() 
        print("          GAME BOARD\n")
        
        play=[]                         #replace the 1s and 0s with XandO
        for x in range(9):
            if self.board[x]==0:play.append(' ')
            elif self.board[x]==1:play.append('X')
            else:play.append('O')
        

        for num in range(8,0,-3):       #Display
            print('          ',play[num-2],'|',play[num-1],'|',play[num])
            if num>3:
                print('           ---------')
        [print() for _ in range(5)]  

    def check_for_win(self):                    #check for winner
        winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))   #possible win combinations
        player=(1,4)

        for who in player:      #run through twice as 1 then 4
          for item in winners:    #all the winning combos
            if who==self.board[item[0]] and who==self.board[item[1]]and who==self.board[item[2]]:
                if who==1:return'X'
                else:return'O'
        for item in self.board:
            if item==0:
                return
        return 'tie'
       
    def who_first(self):
        self.show_board()
        ans=input("Who would you like to go first, Player, Computer or Quit - P, C or Q: ")
        ans=ans.upper()
        return ans

    def player_go(self):
        while True:
            try:
                pgo=int(input("What number would you like (1-9)"))
                if self.board[pgo-1]!=0:
                    exception #no space available
                return pgo
            except:
                self.show_board()
                print("try again")
                continue 

    def comp_go(self):
        move=0
        best_score=-100000
        score=-100000
        for x in range(9):
            if self.board[x]==0:
                self.board[x]=1
                score=self.miniMax(0,False)
                if score > best_score:
                     best_score=score
                     move=x               
                self.board[x]=0
        return move
    
    def noZeros(self):
        res=0
        for item in self.board:
            if item==0:     res+=1
        return res

    def miniMax(self,depth,isMaximizing):

        ans=self.check_for_win()
        if ans:                         #check for win
            if ans=='X':    return 1*(self.noZeros()+1)
            if ans=='O':    return -1*(self.noZeros()+1)
            if ans=='tie':  return 0*(self.noZeros()+1)

        if isMaximizing:
            best_score=-100000
            score=-100000
            for x in range(9):
                if self.board[x]==0:
                    self.board[x]=1
                    score=self.miniMax(depth+1,False)
                    self.board[x]=0
                    best_score=max(score,best_score)
            return best_score

        else:
            best_score=100000
            score=100000
            for x in range(9):
                if self.board[x]==0:
                    self.board[x]=4
                    score=self.miniMax(depth+1,True)
                    self.board[x]=0
                    best_score=min(score,best_score)
            return best_score

    def main(self):
        
        self.show_board()
        ans=self.who_first()
        if ans=='C':
            self.set_board(8,1) #i set this to save time because on turn 1 if left to the computer it will look at 456777 positions and then put this one
            self.show_board()
        if ans=='Q':return'Q' 

        while True:             #while true alternat turns (until a win or tie)
            if self.check_for_win():
                input("Game Over, press return")
                break 
            self.set_board((self.player_go()-1),4)
            self.show_board()

            if self.check_for_win():
                input("Game Over, press return")
                break
            self.set_board(self.comp_go(),1)
            self.show_board()

if __name__=='__main__':
    while True:
        game=TicTacToe()
        if game.main()=='Q':break