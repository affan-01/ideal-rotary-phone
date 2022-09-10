from multiprocessing.spawn import import_main_path
from index import*
from cell import*
from maze import*

def main():
    win = Window(800, 600)
    maze = Maze(1,1,10,10,10,10,20,20,win)
    maze._create_cells()

main()
