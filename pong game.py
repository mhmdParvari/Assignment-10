import math
import random
import arcade

class Racket(arcade.Sprite):
    def __init__(self,x_position,game):
        super().__init__()
        self.game=game
        self.center_x=x_position
        self.center_y=game.height//2
        self.width=4
        self.height=100
        self.speed=4

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,arcade.color.WHITE)

    def move(self):
        self.center_y += self.change_y
        if self.center_y+50 > self.game.height:
            self.center_y = self.game.height-50
        if self.center_y-50 < 0:
            self.center_y = 50

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.center_x=self.game.width//2
        self.center_y=self.game.height//2
        self.speed=6
        self.width=4
        self.height=4
        
        self.angle=math.radians(random.randint(0,359))
        self.x_direction=math.cos(self.angle)
        self.y_direction=math.sin(self.angle)
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,8,arcade.color.RED)

    def move(self):
        self.center_x += self.x_direction * self.speed
        self.center_y += self.y_direction * self.speed
        if self.center_y > self.game.height:
            self.y_direction *= -1
        if self.center_y < 0:
            self.y_direction *= -1
        
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=500,title='pong')
        self.myRacket=Racket(self.width-15,self)
        self.oppRacket=Racket(15,self)
        self.ball=Ball(self)
        self.myScore=0
        self.oppScore=0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(self.width//2,self.height,self.width//2,0,arcade.color.GREEN)
        self.myRacket.draw()
        self.oppRacket.draw()
        self.ball.draw()
        arcade.draw_text(str(self.myScore),(self.width//2)+15,self.height-40,arcade.color.YELLOW,25)
        arcade.draw_text(str(self.oppScore),(self.width//2)-30,self.height-40,arcade.color.YELLOW,25)

    def on_update(self, delta_time: float):
        self.ball.move()
        self.myRacket.move()
        self.oppRacket.move()
        self.AI_set()
        if arcade.check_for_collision(self.ball, self.myRacket) or arcade.check_for_collision(self.ball, self.oppRacket):
            self.ball.x_direction *= -1 
        self.checkForWin()

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.UP:
            self.myRacket.change_y = self.myRacket.speed
        if key == arcade.key.DOWN:
            self.myRacket.change_y = -self.myRacket.speed

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.UP:
            self.myRacket.change_y = 0
        if key == arcade.key.DOWN:
            self.myRacket.change_y = 0
    
    def AI_set(self):
        self.oppRacket.change_y = self.ball.y_direction * self.oppRacket.speed
        
    def checkForWin(self):
        if self.ball.center_x > self.width:
            self.oppScore += 1
            self.ball=Ball(self)
        if self.ball.center_x < 0:
            self.myScore += 1
            self.ball=Ball(self)
        
mygame=Game()
arcade.run()
