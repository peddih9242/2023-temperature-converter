from tkinter import *


class Converter:

    def __init__(self):

        # initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=3)

        self.help_info = Button(self.button_frame, text="Help / Info",
                                bg="#e6ab17",
                                fg=button_fg,
                                font=button_font, width=12,
                                activebackground="#bf8d0d",
                                command=self.to_help)
        self.help_info.grid(row=1, column=0, padx=5, pady=5)

    @staticmethod
    def to_help():
        DisplayHelp()


class DisplayHelp:

    def __init__(self):
        background = "#ffe6cc"

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_title = Label(self.help_frame, text="Help / Information",
                                font=("Arial", "16", "bold"), bg=background)
        self.help_title.grid(row=0)

        help_text = "To use the program, simply enter the temperature you wish to " \
               "convert and then choose to convert to either degrees Celsius (centigrade) " \
               "or Fahrenheit.\n\nNote that -273 degrees C (-459 F) is absolute zero " \
               "(the coldest possible temperature). If you try to convert a temperature " \
               "that is less than -273 degrees C, you will get an error message. To see " \
               "your calculation history and export it to a text file, please click the " \
               "'History / Export' button."

        self.help_text = Label(self.help_frame, text=help_text,
                               wraplength=250, width=40, justify="left", bg=background)
        self.help_text.grid(row=1, padx=5, pady=5)

        self.close_button = Button()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
