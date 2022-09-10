from tkinter import Tk, BOTH , Canvas


class Window:
    def __init__(self,width,height):
        self.__root_widget = Tk()
        self.__root_widget.title('Maze Solver')
        self.__canvas = Canvas(self.__root_widget,bg="white",width=width,height=height)
        self.__canvas.pack()
        self.__Window_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def line_draw(self,line,fill_color):
        line.draw(self.__canvas,fill_color)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__Window_running = True
        while self.__Window_running == True:
            self.redraw()

    def close(self):
        self.__Window_running = False

class Point:

    def __init__(self,x_cordinate,y_cordinate):
        self.x = x_cordinate
        self.y = y_cordinate

class Line:

    def __init__(self,point_1,point_2):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point_1.x,self.point_1.y,self.point_2.x,self.point_2.y,fill = fill_color,width=2)
        canvas.pack()



    