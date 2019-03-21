import tkinter as tk
import random

from PIL import Image
from PIL import ImageTk

class ICanvas(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(ICanvas, self).__init__()
        self.width = kw['width']
        self.height = kw['height']
        self.canvas = tk.Canvas(self, width = kw['width'], height = kw['height'], background='#1C1C1C')
        self.xsb = tk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky='ew')
        self.ysb.grid(row=0, column=1, sticky='ns')
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # button1 = tk.Button(self, text = 'Quit')
        # button1.configure(width = 10, activebackground = '#33B5E5')
        # button1_window = self.canvas.create_window(10, 10, anchor='nw', window=button1)


        self.canvas.bind('<ButtonPress-1>', self.move_start)
        self.canvas.bind('<B1-Motion>', self.move_move)
        self.canvas.bind('<Button-4>', self.zoomerP)
        self.canvas.bind('<Button-5>', self.zoomerM)

    def draw(self, img):
        self.img = img
        self.raw_w, self.raw_h = img.size
        self.on_canvas = img.resize((self.width, self.height), Image.ANTIALIAS)
        self.update_canvas()
    def update_canvas(self):
        self.scale = 1
        imgtk = ImageTk.PhotoImage(image = self.on_canvas)
        self.canvas.imgtk = imgtk
        self.canvas.create_image(0,0,image = imgtk, anchor="nw")

    def create_image(self, *args, **kw):
        self.canvas.create_image(args, kw)

    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def zoomerP(self,event):
        if self.scale == 2.0:
            return
        self.scale += 0.1
        self.on_canvas = self.img.resize((int(self.raw_w * self.scale), int(self.raw_h * self.scale)))
        self.update_canvas()
        self.canvas.configure(scrollregion = self.canvas.bbox('all'))
    def zoomerM(self,event):
        if self.scale == 1.0:
            return
        self.scale -= 0.1
        self.on_canvas = self.img.resize((int(self.raw_w * self.scale), int(self.raw_h * self.scale)))
        self.update_canvas()
        self.canvas.configure(scrollregion = self.canvas.bbox('all'))
    
    def zoom(self, x, y, scale):
        if self.randomise:
            r_percentage_area = round(random.uniform(0.1, self.percentage_area), 2)
        else:
            r_percentage_area = self.percentage_area

        w, h = image.size
        w_new = int(floor(w * r_percentage_area))  # TODO: Floor might return 0, so we need to check this.
        h_new = int(floor(h * r_percentage_area))
        # take (x,y) as center and crop
        random_left_shift = random.randint(0, (w - w_new))  # Note: randint() is from uniform distribution.
        random_down_shift = random.randint(0, (h - h_new))
        # x - w * 
        # self.on_canvas = self.img.resize()
        image = image.crop((random_left_shift, random_down_shift, w_new + random_left_shift, h_new + random_down_shift))

        return image.resize((w, h), resample = Image.BICUBIC)
