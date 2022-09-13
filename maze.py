from cell import Cell
import time 
import random

class Maze:
    def __init__(self,
    x1,
    x2,
    y1,
    y2,
    num_rows,
    num_columns,
    cell_size_x,
    cell_size_y,
    win = None,
    seed = None
    ):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)
    
    #creating a grid of cells 
    def _create_cells(self):
        self._cells = []
        for i in range(0,self.__num_rows):
            temp = []
            for j in range(0,self.__num_columns):
                c = Cell(self._win)
                temp.append(c)
            self._cells.append(temp)

        for i in range(0,self.__num_rows):
            for j in range(0,self.__num_columns):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2,self._win)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    #breaking walls of the grid randomly to form a maze
    def _break_walls(self,i,j):
        self._cells[i][j].visited = True

        while True:
            next_index_list = []
            directions = 0
            #checking which direction to choose
            if i > 0 and self._cells[i-1][j].visited == False:
                next_index_list.append((i-1,j))
                directions += 1
            if i < self.__num_rows-1 and self._cells[i+1][j].visited == False:
                next_index_list.append((i+1,j))
                directions += 1
            if j > 0 and self._cells[i][j-1].visited == False:
                next_index_list.append((i,j-1))
                directions += 1
            if j < self.__num_columns-1 and self._cells[i][j+1].visited == False:
                next_index_list.append((i,j+1))
                directions += 1
            
            #if no possible moves
            if directions == 0:
                self._draw_cell(i,j)
                return 
            
            chosen_direction = random.randrange(directions)
            next_index = next_index_list[chosen_direction]

            if next_index[0] == i+1:
                self._cells[i][j].r_wall = False
                self._cells[i+1][j].l_wall = False
            if next_index[0] == i-1:
                self._cells[i][j].l_wall = False
                self._cells[i-1][j].r_wall = False
            if next_index[1] == j+1:
                self._cells[i][j].b_wall = False
                self._cells[i][j+1].t_wall = False
            if next_index[1] == j-1:
                self._cells[i][j].t_wall = False
                self._cells[i][j-1].b_wall = False
            
            self._animate()
            self._break_walls(next_index[0] , next_index[1])





            



