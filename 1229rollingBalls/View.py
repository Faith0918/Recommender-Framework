import tkinter

class View:
    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title("Game")
        self.tk.resizable(0,0)
        self.frame = tkinter.Frame(self.tk, width=500, height=400)
        self.frame.pack()
        self.drawingComponent = DrawingComponent(self.frame)
             

    def addViewElement(self, position):
        self.drawingComponent.addComponent(position)
    
    def drawElement(self, x, y):
        position = Position(x,y)
        self.drawingComponent.repaint(position)
        # self.canvas.move(self.id, x, y)
        self.tk.update_idletasks()
        self.tk.update()
      
class DrawingComponent:
    def __init__(self, frame):
        self.canvas = tkinter.Canvas(frame,width=500, height=400)
        self.component = any
        
    def addComponent(self,position):
        x = position.getX()
        y = position.getY()
        self.component = self.canvas.create_oval(x, y, x+10, y+10, fill="black")

    def repaint(self, position):
        self.canvas.move(self.component, position.getX(),position.getY())
        self.canvas.pack()
        

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x = x
    def setY(self, y):
        self.y = y

