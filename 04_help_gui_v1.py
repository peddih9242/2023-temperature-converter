from tkinter import *
from functools import partial  # to prevent unwanted windows


class Converter:

    def __init__(self):

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
                                command=self.help_info)
        self.help_info.grid(row=1, column=0, padx=5, pady=5)

    def help_info(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        background = "#ffe6cc"

        self.help_box = Toplevel()

        # disable help button
        partner.help_info.config(state=DISABLED)

        # if users press cross at top, closes help and
        # re-enables help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_title = Label(self.help_frame, text="Help / Information",
                                font=("Arial", "16", "bold"), bg=background)
        self.help_title.grid(row=0, pady=5)

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

        self.close_button = Button(self.help_frame, text="Close",
                                   bg="#e6ab17", fg="#FFFFFF",
                                   command=partial(self.close_help, partner),
                                   activebackground="#bf8d0d", width=7)
        self.close_button.grid(row=2, pady=5)

    # close help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # put help button back to normal
        partner.help_info.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
