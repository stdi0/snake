from tkinter import *
from time import *
from random import *

WIDTH = 500
HEIGHT = 500
directions = []
directions.append((0,-20))

def check_game_over():
    for elem in snake_body:
        if canv.coords(snake_head) == canv.coords(elem):
            return True
    return False

def spawn_food():
    global apple
    x1 = choice([i for i in range(0,500,20)])
    y1 = choice([i for i in range(0,500,20)])
    x2 = x1 + 20
    y2 = y1 + 20
    apple = canv.create_oval([x1,y1],[x2,y2], fill="white")

def food_inspection():
    if canv.coords(snake_head) == canv.coords(apple):
        return True
    else:
        return False

def change_xy(event):
    print(event.keysym)
    if event.keysym == 'Right' and directions[-1][0] != -20:
            x = 20
            y = 0
            directions.append((x,y))
    if event.keysym == 'Left' and directions[-1][0] != 20:
            x = -20
            y = 0
            directions.append((x,y))
    if event.keysym == 'Up' and directions[-1][1] != 20:
            x = 0
            y = -20
            directions.append((x,y))
    if event.keysym =='Down' and directions[-1][1] != -20:
            x = 0
            y = 20
            directions.append((x,y))

def go():
   #tmp = (0,-20)
   i = 0
   while True:
        try:
            x, y = directions[i]
            tmp = (x, y)
            i += 1
        except:
            x, y = tmp
        prev_coords = canv.coords(snake_head)
        canv.move(snake_head,x,y)
        print(canv.coords(snake_head))
        if canv.coords(snake_head)[1] < 0:
            x1,y1,x2,y2 = canv.coords(snake_head)
            y1, y2 = HEIGHT-20, HEIGHT
            canv.coords(snake_head,x1,y1,x2,y2)
        if canv.coords(snake_head)[3] > 500:
            x1,y1,x2,y2 = canv.coords(snake_head)
            y1, y2 = 0, 20
            canv.coords(snake_head,x1,y1,x2,y2)
        if canv.coords(snake_head)[2] > 500:
            x1,y1,x2,y2 = canv.coords(snake_head)
            x1, x2 = 0, 20
            canv.coords(snake_head,x1,y1,x2,y2)
        if canv.coords(snake_head)[0] < 0:
            x1,y1,x2,y2 = canv.coords(snake_head)
            x1, x2 = WIDTH-20, WIDTH
            canv.coords(snake_head,x1,y1,x2,y2)    

        for k, elem in enumerate(snake_body):
            x1,y1,x2,y2 = prev_coords
            prev_coords = canv.coords(snake_body[k])
            canv.coords(snake_body[k],x1,y1,x2,y2)
        
        if check_game_over():
            break

        snake_tail = prev_coords
        if food_inspection():
            canv.delete(apple)
            x1,y1,x2,y2 = snake_tail
            snake_body.append(canv.create_oval([x1,y1],[x2,y2], fill="white"))
            spawn_food()
        #canv.after(350,go)
        canv.update()
        sleep(0.2)


root = Tk()
canv = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
canv.pack()

snake_head = canv.create_oval([240,240],[260,260], fill="white")
snake_body = []
apple = canv.create_oval([0,20],[20,40], fill="white")
#snake_body.append(canv.create_oval([240,260],[260,280], fill="white"))
#snake_body.append(canv.create_oval([240,280],[260,300], fill="white"))
#snake_body.append(canv.create_oval([240,300],[260,320], fill="white"))
#snake_body.append(canv.create_oval([240,320],[260,340], fill="white"))
root.bind("<KeyPress>", change_xy)

go()
#im ='/Users/irina_dashevskaya/project/example.gif'
#ph_im =PhotoImage(file=im)
#canv.create_image(1,1,anchor=NW,image=ph_im)
root.mainloop()
