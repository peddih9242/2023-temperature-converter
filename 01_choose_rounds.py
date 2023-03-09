from tkinter import *


class ChooseRounds:

    def __init__(self):

        self.intro_frame = Frame()
        self.intro_frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Game")
    ChooseRounds()
    root.mainloop()
