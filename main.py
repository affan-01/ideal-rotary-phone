from index import Window , Line , Point

def main():
    win = Window(800, 600)
    l = Line(Point(10,10),Point(500,500))
    win.line_draw(l,"black")
    win.wait_for_close()

main()
