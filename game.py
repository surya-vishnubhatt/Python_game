# You can add methods to this class if you wish.
# The only thing you cannot do is change the names
# of the member variables.
# The argument could be made that Hero and Object should
# be the same class, but I did not do this because:
#   - In my own solution, I have some additional, different
#     methods in each of these two classes.
#   - I thought it might introduce some unnecessary confusion.
class Hero:
    def __init__(self, symbol, start_x, start_y):
        self.symbol = symbol
        self.x = start_x
        self.y = start_y

    # You don't have to use this if you don't want to.
    def draw_on_board(self, board):
        board[self.y][self.x] = self.symbol

# You can add methods to this class if you wish.
# The only thing you cannot do is change the names
# of the member variables.
class Object:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y

    # You don't have to use this if you don't want to.
    def draw_on_board(self, board):
        board[self.y][self.x] = self.symbol

class Building:
    def __init__(self, x, y):
        self.width = 6
        self.height = 4
        self.door_height = 2
        self.door_width = 2
        self.x = x
        self.y = y
    def draw_on_board(self, board):
        # try:
        for i in range(self.y, self.y + self.height):
            board[i][self.x + self.width-1] = '|'
            board[i][self.x] ='|'
            for j in range(self.x, self.x + self.width):
                board[self.y][j] = '-'
                board[self.y+self.height-1][j] = '-'
                #Draw the door
                board[self.y+self.height-1][self.x+2] = '&'
                board[self.y+self.height-1][self.x+3] = '&'
                board[self.y+self.height-2][self.x+2] = '&'
                board[self.y+self.height-2][self.x+3]='&'

    # Returns True if given the location of this building, the point
    # indicated by (x,y) touches this building in any way.
    def contains(self, x, y):
        boolVar = False
        for i in range(self.y,self.y+self.height):
            for j in range(self.x,self.x+self.width):
                if j == x and i == y:
                    boolVar = True
        return boolVar

# You don't need to use this function, but I found it useful
# when I wanted to inspect the board from the Interpreter /
# after running the program.
def print_board(board):
    for row in board:
        for spot in row:
            print(spot, end='')
        print()

class Game:
    def __init__(self, input_file_name):
        # You can add member variables to this class.
        # However, you cannot change the names of any of
        # the member variables below; the autograder will
        # expect these member variables to have the names
        # that they have.

        self.hero = None
        self.num_objects = 0
        self.board = None
        self.buildings = []
        self.objects = []
        self.down_key = None
        self.up_key = None
        self.right_key = None
        self.left_key = None
        self.read_input_file(input_file_name)
        self.hero.draw_on_board(self.board)
        self.user_quit = False
        self.all_objects_collected = False


    def read_input_file(self, input_file_name):
        file_in = open(input_file_name)
        list1 = []
        board_list = []
        for line in file_in:
            list1.append(line)
        board_dim = list1[0].split()
        x_val = int(board_dim[0])
        y_val = int(board_dim[1])
        board = []
        for i in range(y_val):
            newlist =[]
            for j in range(x_val):
                newlist.append(' ')
            board += [newlist]
        #DRAW BOARD
        for i in range(y_val):
            board[i][x_val-1] = '|'
            board[i][0] = '|'
            for j in range(x_val):
                board[y_val-1][j] = '-'
                board[0][j] = '-'
                board[0][0] = " "
                board[0][x_val-1] = " "
                board[y_val-1][x_val-1] = " "
                board[y_val-1][0] = " "
        self.board = board
        icon_list = list1[1].split()
        hero = Hero(icon_list[0],int(icon_list[1]),int(icon_list[2]))
        self.hero = hero
        self.up_key = list1[2][0]
        self.left_key = list1[3][0]
        self.down_key = list1[4][0]
        self.right_key = list1[5][0]
        self.objects = []
        self.buildings = []
        self.objrec = []
        self.build_coll = []
        self.obj_icons = []
        for i in range(6, len(list1)):
            newlist = list1[i].split()
            if newlist[0] == "o":
                o1 = Object(newlist[1],int(newlist[2]),int(newlist[3]))
                self.objects.append(o1)
                o1.draw_on_board(board)
                self.objrec.append([int(newlist[2]), int(newlist[3])])
                self.obj_icons.append(newlist[1])
            elif newlist[0] == "b":
                b1 = Building(int(newlist[1]),int(newlist[2]))
                self.buildings.append(b1)
                self.build_coll.append([int(newlist[1]), int(newlist[2])])
                b1.draw_on_board(board)
        self.num_objects = len(self.objects)

    def print_game(self):
        for row in self.board:
            for spot in row:
                print(spot, end='')
            print()

    def game_ended(self):
        return self.all_objects_collected or self.user_quit

    def move_up(self):
        self.hero.y -= 1
        oldpos_y = self.hero.y + 1
        #COLLISION DETECTION WITH BUILDINGS OR EDGES
        predict_val_x = self.hero.x
        predict_val_y = self.hero.y
        if self.board[predict_val_y][predict_val_x] == "&" or  self.board[predict_val_y][predict_val_x] == "|" or  self.board[predict_val_y][predict_val_x] == "-":
            self.hero.y = oldpos_y
            self.hero.draw_on_board(self.board)
        else:
            self.board[oldpos_y][self.hero.x] = " "
            self.hero.draw_on_board(self.board)

    def move_down(self):
        self.hero.y += 1
        oldpos_y1 = self.hero.y - 1
        #COLLISION DETECTION WITH BUILDINGS OR EDGES
        predict_val_x = self.hero.x
        predict_val_y = self.hero.y
        if self.board[predict_val_y][predict_val_x] == "&" or  self.board[predict_val_y][predict_val_x] == "|" or  self.board[predict_val_y][predict_val_x] == "-":
            self.hero.y = oldpos_y1
            self.hero.draw_on_board(self.board)
        else:
            self.board[oldpos_y1][self.hero.x] = " "
            self.hero.draw_on_board(self.board)

    def move_right(self):
        self.hero.x += 1
        oldpos_x = self.hero.x - 1
        #COLLISION DETECTION WITH BUILDINGS OR EDGES
        predict_val_x = self.hero.x
        predict_val_y = self.hero.y
        if self.board[predict_val_y][predict_val_x] == "&" or  self.board[predict_val_y][predict_val_x] == "|" or  self.board[predict_val_y][predict_val_x] == "-":
            self.hero.x = oldpos_x
            self.hero.draw_on_board(self.board)
        else:
            self.board[self.hero.y][oldpos_x] = " "
            self.hero.draw_on_board(self.board)

    def move_left(self):
        self.hero.x -= 1
        oldpos_x1 = self.hero.x + 1
        #COLLISION DETECTION WITH BUILDINGS OR EDGES
        predict_val_x = self.hero.x
        predict_val_y = self.hero.y
        if self.board[predict_val_y][predict_val_x] == "&" or  self.board[predict_val_y][predict_val_x] == "|" or  self.board[predict_val_y][predict_val_x] == "-":
            self.hero.x = oldpos_x1
            self.hero.draw_on_board(self.board)
        else:
            self.board[self.hero.y][oldpos_x1] = " "
            self.hero.draw_on_board(self.board)
    def run(self):
        # TODO: Finish the implementation. Implement movement
        # and collision detection. You have much flexibity in
        # how you modify this function. For example, you can
        # remove the definitions and usages of the game_ended()
        # and all_objects_collected() methods if you don't want
        # to use those. (My own implementation uses those methods.)
        quit_cmds = ['q', 'end', 'exit']
        count = 0
        boolVar = False
        while not self.game_ended():
            self.print_game()
            #INCREMENT COUNT EACH TIME OBJECT IS COLLECTED
            for i in range(len(self.objrec)):
                if self.objrec[i][0] == self.hero.x and self.objrec[i][1] == self.hero.y:
                    count += 1
                    self.objrec[i] = "100000"
                    if count == self.num_objects:
                        boolVar = True
            if boolVar:
                self.all_objects_collected = True
                break
            inp = input("Enter: ")
            if inp in quit_cmds or count == self.num_objects:
                self.user_quit = True
                break
            else:
                if inp == self.up_key:
                    self.move_up()
                elif inp == self.down_key:
                    self.move_down()
                elif inp == self.right_key:
                    self.move_right()
                elif inp == self.left_key:
                    self.move_left()
                else:
                    print("Invalid command")
        if self.user_quit:
            self.print_game()
            print("You are a quitter!")
        else:
            print("Congratulations: you've collected all of the items!")

g = Game("input1.txt")
g.run()