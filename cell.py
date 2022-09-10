from turtle import fillcolor
from index import*

class Cell:
    
    def __init__(self,win = None):
        self.l_wall = True
        self.r_wall = True
        self.t_wall = True
        self.b_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.__visited = False
        self._win = win
    
    def draw(self,x1,y1,x2,y2,win):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self._win = win
        
        if self.l_wall:
            l = Line(Point(x1,y1),Point(x1,y2))
            self._win.line_draw(l,"red")
        if self.r_wall:
            l = Line(Point(x2,y1),Point(x2,y2))
            self._win.line_draw(l,"black")
        if self.t_wall:
            l = Line(Point(x1,y1),Point(x2,y1))
            self._win.line_draw(l,"red")
        if self.b_wall:
            l = Line(Point(x1,y2),Point(x2,y2))
            self._win.line_draw(l,"black")
    
    def draw_move(self,to_cell,undo = False):
        mid_x = (self.x1 + self.x2)/2
        mid_y = (self.y1 + self.y2)/2

        to_mid_x = (to_cell.x1 + to_cell.x2)/2
        to_mid_y = (to_cell.y1 + to_cell.y2)/2

        line = Line(Point(mid_x,mid_y),Point(to_mid_x,to_mid_y))
        self._win.line_draw(line,"red")
        