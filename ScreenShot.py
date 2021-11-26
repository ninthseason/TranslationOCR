# 截图模块
# Powered by Kl1nge5
# 2021/11/25 中午，好累
# tk有点不灵活，比较难做

from PIL import ImageGrab
import tkinter as tk


class Shot:
    def __init__(self):
        self.top = tk.Tk()
        self.top.attributes('-fullscreen', True)
        self.top.attributes('-alpha', 0.2)
        self.top.config(bg='white')
        self.top.bind('<Button-1>', self.B1)
        self.top.bind('<ButtonRelease-1>', self.B2)
        self.top.bind('<Button-3>', self.B3)
        self.top.bind('<Motion>', self.M)
        self.top.bind('<KeyPress-Escape>', self.killByEsc)

        self.canvas = tk.Canvas(self.top, highlightthickness=0, width=self.top.winfo_screenwidth(), height=self.top.winfo_screenheight())
        self.canvas.place(x=0, y=0)

        self.scale = 1
        self.x = 0
        self.y = 0
        self.move = False

        self.img = None

    def B1(self, e):
        e.x *= self.scale
        e.y *= self.scale
        print(f'B1 {e.x}, {e.y}')
        self.move = True
        self.x = e.x
        self.y = e.y

    def B2(self, e):
        e.x *= self.scale
        e.y *= self.scale
        print(f'B2 {e.x}, {e.y}')
        self.move = False
        self.img = ImageGrab.grab((self.x if e.x > self.x else e.x, self.y if e.y > self.y else e.y,
                                   self.x if e.x < self.x else e.x, self.y if e.y < self.y else e.y))

    def B3(self, e):
        print('SHOT')
        self.kill()

    def M(self, e):
        if self.move:
            self.updateArea(e.x, e.y)

    def updateArea(self, x, y):
        self.canvas.delete('rec')
        self.canvas.create_rectangle(self.x / self.scale, self.y / self.scale, x, y, fill='black',
                                     outline='red', width=2, tag='rec')

    def start(self):
        self.top.mainloop()

    def kill(self):
        self.top.destroy()

    def killByEsc(self, e):
        self.img = None
        self.top.destroy()

    # 当系统缩放高于150%，需要调整该值以适应截图尺寸
    def setScale(self, scale):
        self.scale = scale

    def getImage(self):
        return self.img


if __name__ == '__main__':
    shot = Shot()
    shot.setScale(1.5)
    shot.start()
