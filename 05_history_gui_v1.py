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

        self.history_export = Button(self.button_frame, text="History / Export",
                                     bg="#2a0e99",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     activebackground="#1f0878",
                                     command=self.to_history)
        self.history_export.grid(row=1, column=0, padx=5, pady=5)

    def to_history(self):
        DisplayHistory(self)


class DisplayHistory:

    def __init__(self, partner):
        background = "#ffe6cc"

        self.history_box = Toplevel()

        # disable history button
        partner.history_export.config(state=DISABLED)

        # if users press cross at top, closes history and
        # re-enables history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, height=200)
        self.history_frame.grid()

        self.history_title = Label(self.history_frame, text="History / Export",
                                   font=("Arial", "16", "bold"))
        self.history_title.grid(row=0, pady=5)

        help_text = "To use the program, simply enter the temperature you wish to " \
                    "convert and then choose to convert to either degrees Celsius (centigrade) " \
                    "or Fahrenheit.\n\nNote that -273 degrees C (-459 F) is absolute zero " \
                    "(the coldest possible temperature). If you try to convert a temperature " \
                    "that is less than -273 degrees C, you will get an error message. To see " \
                    "your calculation history and export it to a text file, please click the " \
                    "'History / Export' button."

        self.history_text = Label(self.history_frame, text=help_text,
                                  wraplength=250, width=40, justify="left")
        self.history_text.grid(row=1, padx=5, pady=5)

        self.close_button = Button(self.history_frame, text="Close",
                                   bg="#e6ab17", fg="#FFFFFF",
                                   command=partial(self.close_history, partner),
                                   activebackground="#bf8d0d", width=7)
        self.close_button.grid(row=2, pady=5)

    # close history dialogue (used by button and x at top of dialogue)
    def close_history(self, partner):
        # put history button back to normal
        partner.history_export.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
