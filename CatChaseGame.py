#cat chases the mouse. cat moves 2 spaces for mouse's 1 move.
#mouse must try to escape the board to win.
#mouse is controlled by the player (WASD keys to move)
import random

class catMouse:
    def __init__(self, width, height, mouseRow, mouseCol, catRow, catCol):
        self.width = width
        self.height = height
        self.mouseRow = mouseRow
        self.mouseCol = mouseCol
        self.catRow = catRow
        self.catCol = catCol

        self.data = [['  ']*width for row in range(height)]
        
        for row in range(0,self.height):
            for col in range(0,self.width):
                if row == self.mouseRow and col == self.mouseCol:
                    self.data[row][col] = '🐭'
                elif row == self.catRow and col == self.catCol:
                    self.data[row][col] = '😺'
                elif row == 0 or row == self.height-1 or col == 0 or col == self.width-1:
                    self.data[row][col] = '🟩'
                elif random.choice([0,1,2,3]) == 1:
                    self.data[row][col] = '⬛'
                
    def __repr__(self):
        s = ''
        for row in range(0,self.height):
            for col in range(0,self.width):
                s += self.data[row][col]
            s += '\n'
        return s

    def move(self, direction):
        """ move moves the mouse in the direction specified"""
        if direction in 'wW':
            self.mouseRow -= 1
            self.data[self.mouseRow][self.mouseCol] = '🐭'
            self.data[self.mouseRow + 1][self.mouseCol] = '  '
        elif direction in 'aA':
            self.mouseCol -= 1
            self.data[self.mouseRow][self.mouseCol] = '🐭'
            self.data[self.mouseRow][self.mouseCol + 1] = '  '
        elif direction in 'sS':
            self.mouseRow += 1
            self.data[self.mouseRow][self.mouseCol] = '🐭'
            self.data[self.mouseRow - 1][self.mouseCol] = '  '
        elif direction in 'dD':
            self.mouseCol += 1
            self.data[self.mouseRow][self.mouseCol] = '🐭'
            self.data[self.mouseRow][self.mouseCol - 1] = '  '
    
    def mouseallowsMove(self, direction):
        """mouseallowsMove checks if the mouse (user) can move in the direction specified.
        Mouse can only move into a spot with no walls, or is green.
        """
        if direction in 'wWaAsSdD':
            if direction in 'wW' and (self.data[self.mouseRow - 1][self.mouseCol] == '  ' or self.data[self.mouseRow - 1][self.mouseCol] == '🟩'):
                return True
            elif direction in 'aA' and (self.data[self.mouseRow][self.mouseCol - 1] == '  ' or self.data[self.mouseRow][self.mouseCol - 1] == '🟩'):
                return True
            elif direction in 'sS' and (self.data[self.mouseRow + 1][self.mouseCol] == '  ' or self.data[self.mouseRow + 1][self.mouseCol] == '🟩'):
                return True
            elif direction in 'dD' and (self.data[self.mouseRow][self.mouseCol + 1] == '  ' or self.data[self.mouseRow][self.mouseCol + 1] == '🟩'):
                return True
            return False
        else:
            return False
    
    def catmove(self, direction):
        """catmove moves cat to new spot in direction specified and replaces its path with a wall
        """
        if direction in 'wW':
            self.catRow -= 1
            self.data[self.catRow][self.catCol] = '😺'
            self.data[self.catRow + 1][self.catCol] = '⬛'
        elif direction in 'aA':
            self.catCol -= 1
            self.data[self.catRow][self.catCol] = '😺'
            self.data[self.catRow][self.catCol + 1] = '⬛'
        elif direction in 'sS':
            self.catRow += 1
            self.data[self.catRow][self.catCol] = '😺'
            self.data[self.catRow - 1][self.catCol] = '⬛'
        elif direction in 'dD':
            self.catCol += 1
            self.data[self.catRow][self.catCol] = '😺'
            self.data[self.catRow][self.catCol - 1] = '⬛'

    def catAImove(self):
        """ catAImove is how the cat decides to move when it's cat's turn
        """
        if self.catRow == self.mouseRow:            #cat & mouse in SAME row
            if self.catCol > self.mouseCol:         #cat is right of mouse
                self.catmove('a')                    
            else:                                   #cat is left of mouse
                self.catmove('d')               #cat move to right if possible
        elif self.catRow > self.mouseRow:           #cat is below mouse
            self.catmove('w')                   #cat moves up if possible
        else:                                       #cat is above mouse
            self.catmove('s')   


    def hostGame(self):
        '''hostGame runs the cat chase game! meow meow :)
        '''
        print(self)
        whoWon = ''

        while True:
            move = 'X'
            while self.mouseallowsMove(move) == False:  #will keep asking for input until it is a valid move
                move = input("Input w (up), a (left), s (down), d (right) to move the mouse: ")
            self.move(move)
            print(self)

            if self.catRow == self.mouseRow and self.catCol == self.mouseCol:
                print("Sorry, the cat caught you. You lost. :(")
                whoWon = 'cat'
                break
            if self.mouseRow == 0 or self.mouseRow == self.height-1 or self.mouseCol == 0 or self.mouseCol == self.width - 1:
                print("Congratulations, you win! :)")
                whoWon = 'mouse'
                break 

            self.catAImove()
            print('The cat has made its first move.')
            print(self)

            if self.catRow == self.mouseRow and self.catCol == self.mouseCol:
                print("Sorry, the cat caught you. You lost. :(")
                whoWon = 'cat'
                break
            if self.mouseRow == 0 or self.mouseRow == self.height-1 or self.mouseCol == 0 or self.mouseCol == self.width - 1:
                print("Congratulations, you win! :)")
                whoWon = 'mouse'
                break 

            self.catAImove()
            print('The cat has made its second move.')
            print(self)

            if self.catRow == self.mouseRow and self.catCol == self.mouseCol:
                print("Sorry, the cat caught you. You lost. :(")
                whoWon = 'cat'
                break
            if self.mouseRow == 0 or self.mouseRow == self.height-1 or self.mouseCol == 0 or self.mouseCol == self.width - 1:
                print("Congratulations, you win! :)")
                whoWon = 'mouse'
                break
        if whoWon == 'mouse':
            return True
        return False


    def playGame(self):
        """playGame allows the player to play Cat Chase however many times they want and keeps track of the score!"""
        print("\nWelcome to Cat Chase!\n")
        play = 1
        wins = 0
        loss = 0

        while play == 1:
            print("The score is currently \n        Cat Wins: " + str(loss) + "\nMouse (you) wins: " + str(wins))
            b = catMouse(20,20,10,10,1,1)
            if b.hostGame():
                wins += 1
            else:
                loss += 1
            play = int(input("Would you like to play again? Type 0 for no, 1 for yes: "))
        
        print("\nThanks for playing! You won " + str(wins) + " times and lost " + str(loss) + " times.")


b = catMouse(20,20,10,10,1,1)