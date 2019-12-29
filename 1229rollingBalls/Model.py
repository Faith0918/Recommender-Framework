

class Model:
    def __init__(self):
        self.ball = Ball()
    def getBall(self):
        return self.ball
    def setBall(self, ball):
        self.ball = ball
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 1 
        self.dy = 1 
        
    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y
    def getDx(self):
        return self.dx
    def getDy(self):
        return self.dy
    def setDx(self, dx):
        self.dx = dx
    def setDy(self, dy):
        self.dy = dy