import arcade
import random

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.x=400
        self.y=300
        self.l=20
        self.w=10
        self.speed=3
    
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.w,self.l,arcade.color.GREEN)

    def update_position(self):
        self.x += self.change_x
        self.y += self.change_y
        
        if self.x < 0:
            self.x=0
        if self.x > 799:
            self.x=799
        if self.y < 0:
            self.y=0
        if self.y > 599:
            self.y=599

class Fruit(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.x=random.randint(0,799)
        self.y=random.randint(0,599)

    def draw(self):
        arcade.draw_circle_filled(self.x,self.y,4,arcade.color.RED)

class Game(arcade.Window):
    def __init__(self):
        super().__init__()
        self.apple=Fruit()
        self.snake=Snake()
    
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()

    def on_update(self, delta_time: float):
        self.snake.update_position()
        if -5 < self.snake.x-self.apple.x < 5 and -5 < self.snake.y-self.apple.y < 5:
            self.apple=Fruit()
            #self.apple.draw()
     
    def on_key_press(self, key, modifiers: int):
        if key==arcade.key.RIGHT:
            self.snake.change_x= self.snake.speed
        if key==arcade.key.LEFT:
            self.snake.change_x= -self.snake.speed
        if key==arcade.key.UP:
            self.snake.change_y= self.snake.speed
        if key==arcade.key.DOWN:
            self.snake.change_y= -self.snake.speed

    def on_key_release(self, key, modifiers: int):
            self.snake.change_y=0
            self.snake.change_x=0

myGame=Game()
arcade.run()


