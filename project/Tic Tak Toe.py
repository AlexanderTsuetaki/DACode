#tictactoe.py
#A one-player game of tic-tac-toe
#Due 02-14-2016
__author__="Alexander Tsuetaki"
import random
import sys
class TicTacToe:
    grid = None
    userPick = None
    playerturn= False

    def __init__(self):
        #makes a grid and a copy of the grid that will always be the same
        self.grid= [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.copy = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ' ]]
        #gets the player to give what tile they want to be
        print ('*** Welcome to tic tac toe ***')
        print ('computer v.s.player version')
        print ('when making it a move print it in the form of row col make sure there is a spave between row and col')
        playerTile = raw_input('would you like to be X or O')
        playerTile = playerTile.upper()
        #gets the computer Tile
        if playerTile=='O':
            compTile='X'
        else:
            compTile='O'
        #sees who goes first
        rand = random.randrange(0,2)
        if rand == 0:
            playerturn = True
        else:
            playerturn= False
        #returns all the variables that i will need for later
        self.playerTile = playerTile
        self.compTile = compTile
        self.playerturn = playerturn

    #TODO:
    # Scan grid and determine if all indices are filled
    # with X or O. Return True if so, False otherwise
    def board_is_full(self):
        counter=0
        for a in range(0,3):
            for b in range(0,3):
                if self.grid[a][b] == "X" or self.grid[a][b] == "O":
                    counter+=1
        if counter == 9:
            return True
        else:
            return False

    #TODO:
    # Determine if a row, col position in grid is open
    # If yes, return True. False otherwise.
    def is_open_space(self, grid, row, col):
         if grid[row][col] == " ":
            return True
         else:
            return False
    #gets the users move
    def get_user_move(self):
        user_input = raw_input("input your coordinates in a row col format")
        user_input = user_input.split(" ")
        #splits and changes the users input into intigers that can be used
        #sees if data is good
        try:
            user_input[0] = int(user_input[0])
            user_input[1] = int(user_input[1])
        except:
            print ("you have bad data")
        #sees if it can play in a spot and if not makes the user try again
        if self.is_open_space(self.grid,user_input[0],user_input[1]):
            self.grid[user_input[0]][user_input[1]] = self.playerTile
        else:
            self.get_user_move()

    # Determine computer move (this is the AI)
    def get_comp_move(self):
        counter=0
        #see if can win
        self.get_board_copy()
        for i in range(0,3):
            for j in range(0,3):
                self.get_board_copy()
                if self.is_open_space(self.copy, i, j):
                    self.copy[i][j] = self.compTile
                    if self.game_won(self.copy):
                        self.grid[i][j] = self.compTile
                        print "Computer moved to "+str(i)+" "+str(j)
                        return i,j
        #sees if it can block player
        self.get_board_copy()
        for i in range(0,3):
            for j in range(0,3):
                self.get_board_copy()
                if self.is_open_space(self.copy, i, j):
                    self.copy[i][j] = self.playerTile
                    if self.game_won(self.copy):
                        self.grid[i][j] = self.compTile
                        print "Computer moved to "+str(i)+" "+str(j)
                        return i, j
        #sees if can play in a corner then picks a random corner
        for i in range(0,4):
            move = ["0 0","2 2","0 2","2 0"]
            temp = random.randint(0,3)
            temp1 = move[temp]
            temp2 = temp1.split(" ")
            if self.is_open_space(self.grid, int(temp2[0]), int(temp2[1])):
                self.grid[int(temp2[0])][int(temp2[1])] = self.compTile
                print "Computer moved to "+temp2[0]+" "+temp2[1]
                return temp1
            else:
                del(move[temp])
        #sees if can play in the center
        for i in range(1,2):
            if self.is_open_space(self.grid, i, i):
                self.grid[1][1] = self.compTile
                print "Computer moved to 1 1"
                return i
        #sees if  an play in a side
        for i in range(0,4):
            move = ["1 0","0 1","2 1","1 2"]
            temp=random.randint(0,4)
            temp1=move[temp]
            temp2=temp1.split(' ')
            if self.is_open_space(self.grid, int(temp2[0]), int(temp2[1])):
                self.grid[int(temp2[0])][int(temp2[1])] = self.compTile
                print "Computer moved to "+temp2[0]+" "+temp2[1]
                return temp1
            else:
                del(move[temp])
            #see if can lose
    def get_board_copy(self):
   # Make a duplicate of the board list and return it the duplicate.
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.copy[i][j] = self.grid[i][j]

    # Has a player won the game (i.e. 3-in-a-row?)
    # If yes, return True, otherwise return False
    def game_won(self,grid):
        for i in range(0,3):
            if grid[i][i] != " ":
                if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2]:
                    return True
                if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i]:
                    return True
        for i in range(0,1):
            if grid[i+1][i+1] != " ":
                if grid[i][i] == grid[i+1][i+1] and grid[i+1][i+1] == grid[i+2][i+2]:
                    return True
                if grid[i+2][i] == grid[i+1][i+1] and grid[i+1][i+1] == grid[i][i+2]:
                    return True
        return False
    #plays the game by
    def play_game(self):
        while not self.board_is_full() and not self.game_won(self.grid):
            if self.playerturn:
                self.get_user_move()
                self.playerturn=False
            else:
                self.get_comp_move()
                self.playerturn=True
            self.make_board()
            self.game_won(self.grid)
        if self.board_is_full():
            print"You tied"
        if self.game_won(self.grid):
            if not self.playerturn:
                print "The Player wins"
            else:
                print "The Computer wins"
        print "thanks for playing"
   #makes the board when called
    def make_board(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                print self.grid[i][j],
                if j< len(self.grid[j])-1:
                    print'|',
            if i<len(self.grid)-1:
                print
                print "__ ___ __"
            else:
                print ""


#the main method is not part of the tictactoe class
#instead it is tjsut the main entry point of this file
def start():
    game = TicTacToe() #calls the _init__ method
    game.make_board()  #print what should be an empty grid
    game.play_game()   #calls the function that starts and perpetuates the game
if __name__ == "__main__":
    start()