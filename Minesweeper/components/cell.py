from tkinter import Button

class Cell():
    all = []

    def __init__(self, x, y, mine=False):
        self.mine = mine
        self.btn = None
        self.x = x
        self.y = y
        self.value = f"{self.x} {self.y}"

        Cell.all.append(self)


    def new_btn(self, location):
        btn = Button(
            location,
            text=self.value,
            height=2,
            width=4
        )
        self.btn = btn
        self.btn.bind('<Button-1>', self.cb_left_click)
        self.btn.bind('<Button-3>', self.cb_right_click)
        return self
    

    def cb_left_click(self, event):
        print(f"Left click on {self.value}")
        print("Event: ", event)


    def cb_right_click(self, event):
        print(f"Right click on {self.value}")
        print("Event: ", event)

    
    def __repr__(self):
        return f"Cell({self.value})"


    @staticmethod
    def randomize():
        pass