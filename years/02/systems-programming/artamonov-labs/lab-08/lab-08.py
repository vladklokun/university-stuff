import tkinter as tk
import time

CANVAS_WIDTH = 320
CANVAS_HEIGHT = 240

XVELOCITY = 5
YVELOCITY = 0

class Ball:
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        self.id = canvas.create_oval(*args, **kwargs)
        self.vx = XVELOCITY
        self.vy = YVELOCITY
        
    def move(self):
        # Get bounding box coordinates
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        
        # If ball's bounding box is at right canvas border, move left
        if x2 > CANVAS_WIDTH:
            self.vx = -XVELOCITY
            
        # If ball's bounding box is at left canvas border, move right
        if x1 < 0:
            self.vx = XVELOCITY
            
        self.canvas.move(self.id, self.vx, self.vy)
        
class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.canvas = tk.Canvas(self.master, width = CANVAS_WIDTH,
                                height = CANVAS_HEIGHT)
        self.canvas.pack()
        self.balls = [
            Ball(self.canvas, 2, 2, 40, 40, fill = 'blue', tag = 'ballA'),
        ]
        
        self.master.after(0, self.animation)
        
    def animation(self):
        for ball in self.balls:
            ball.move()
            
        self.master.after(20, self.animation)
        
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
main()
