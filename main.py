from tkinter import *
from time import *
from random import *
import os
import sys

class SnakeGame:

    WIDTH = 500
    HEIGHT = 500

    def check_game_over(self):
        for elem in self.snake_body:
            if self.canv.coords(self.snake_head) == self.canv.coords(elem):
                self.canv.create_text(250,250, text="Game Over",
                    font="Verdana 18", justify=CENTER, fill="red")
                return True
        return False

    def spawn_food(self):
        x1 = choice([i for i in range(0,500,20)])
        y1 = choice([i for i in range(0,500,20)])
        x2 = x1 + 20
        y2 = y1 + 20
        for elem in self.snake_body:
            if self.canv.coords(elem) == [x1,y1,x2,y2]:
                return self.spawn_food()
        self.apple = self.canv.create_oval([x1,y1],[x2,y2], fill="#FFFF00")

    def food_inspection(self):
        if self.canv.coords(self.snake_head) == self.canv.coords(self.apple):
            return True
        else:
            return False

    def change_xy(self, event):
        print(event.keysym)
        if event.keysym == 'Right' and self.directions[-1][0] != -20:
                x = 20
                y = 0
                self.directions.append((x,y))
        if event.keysym == 'Left' and self.directions[-1][0] != 20:
                x = -20
                y = 0
                self.directions.append((x,y))
        if event.keysym == 'Up' and self.directions[-1][1] != 20:
                x = 0
                y = -20
                self.directions.append((x,y))
        if event.keysym =='Down' and self.directions[-1][1] != -20:
                x = 0
                y = 20
                self.directions.append((x,y))

    def go(self):
       i = 0
       while True:
            try:
                x, y = self.directions[i]
                tmp = (x, y)
                i += 1
            except IndexError:
                x, y = tmp
            prev_coords = self.canv.coords(self.snake_head)
            self.canv.move(self.snake_head,x,y)

            if self.canv.coords(self.snake_head)[1] < 0:
                x1,y1,x2,y2 = self.canv.coords(self.snake_head)
                y1, y2 = self.HEIGHT-20, self.HEIGHT
                self.canv.coords(self.snake_head,x1,y1,x2,y2)
            if self.canv.coords(self.snake_head)[3] > 500:
                x1,y1,x2,y2 = self.canv.coords(self.snake_head)
                y1, y2 = 0, 20
                self.canv.coords(self.snake_head,x1,y1,x2,y2)
            if self.canv.coords(self.snake_head)[2] > 500:
                x1,y1,x2,y2 = self.canv.coords(self.snake_head)
                x1, x2 = 0, 20
                self.canv.coords(self.snake_head,x1,y1,x2,y2)
            if self.canv.coords(self.snake_head)[0] < 0:
                x1,y1,x2,y2 = self.canv.coords(self.snake_head)
                x1, x2 = self.WIDTH-20, self.WIDTH
                self.canv.coords(self.snake_head,x1,y1,x2,y2)    

            for k, elem in enumerate(self.snake_body):
                x1,y1,x2,y2 = prev_coords
                prev_coords = self.canv.coords(self.snake_body[k])
                self.canv.coords(self.snake_body[k],x1,y1,x2,y2)
            
            if self.check_game_over():
                break

            if self.food_inspection():
                self.canv.delete(self.apple)
                x1,y1,x2,y2 = prev_coords
                self.snake_body.append(self.canv.create_oval([x1,y1],[x2,y2], fill="white"))
                self.spawn_food()
            
            self.canv.update()
            sleep(0.2)

    def __init__(self):
        self.canv = Canvas(root, width=self.WIDTH, height=self.HEIGHT, bg="#003300")
        self.canv.pack()
        self.im = os.path.realpath(os.path.dirname(sys.argv[0])) + '/background.gif'
        self.ph_im =PhotoImage(file=self.im)
        self.canv.create_image(1,1,anchor=NW,image=self.ph_im)
        self.snake_head = self.canv.create_oval([240,240],[260,260], fill="white")
        self.snake_body = []
        self.directions = [(0,-20)]
        self.spawn_food()
        root.bind("<KeyPress>", self.change_xy)            

root = Tk()
newgame = SnakeGame()
newgame.go()

root.mainloop()
