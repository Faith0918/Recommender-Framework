import Model
import View
import time

class Core:
    def __init__(self):
        self.view = View.View()
        self.model = Model.Model()

    def run(self):
        x = self.model.getBall().getX()
        y = self.model.getBall().getY()
        position = View.Position(x, y)
        self.view.addViewElement(position)
        while 1:
            self.reflectBall()
            self.moveBall()
            time.sleep(0.01)

    def reflectBall(self):
        ball = self.model.getBall()
        x = ball.getX()
        y = ball.getY()
        if x>500:
            ball.setDx(-1)
            
        elif x<0:
            ball.setDx(1)
        if y>400:
           
            ball.setDy(-1)
        elif y<0:
            ball.setDy(1)
        self.model.setBall(ball)

    def moveBall(self):
        ball = self.model.getBall()
        ball.setX(ball.getX()+ball.getDx())
        ball.setY(ball.getY()+ball.getDy())
        self.model.setBall(ball)
        self.view.drawElement(ball.getDx(), ball.getDy())
           


core = Core()
core.run()

