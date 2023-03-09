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
        all_calculations = ["0 degrees C = 32 degrees F", "0 degrees F = -18 degrees C",
                            "-273 degrees C = -459 degrees F"]

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

        history_text = "Below are your recent calculations - showing {} / {}" \
                       " calculations. All calculations are shown to the nearest degree".format(len(all_calculations), len(all_calculations))

        self.history_text = Label(self.history_frame, text=history_text,
                                  wraplength=300, width=50, justify="left")
        self.history_text.grid(row=1, padx=5, pady=5)

        self.show_history = Label(self.history_frame, text=all_calculations,
                                  width=40, background=background, wraplength=300)
        self.show_history.grid(row=2, padx=5, pady=5)

        export_text = "Either choose a custom file name (and push <Export>) or" \
                      "simply push <Export> to save your calculations in a text" \
                      "file. If the filename already exists, it will be overwritten."
        self.export_text = Label(self.history_frame, text=export_text, width=50, wraplength=300,
                                 justify="left")
        self.export_text.grid(row=3, padx=5, pady=5)

        self.filename_entry = Entry(self.history_frame, width=50)
        self.filename_entry.grid(row=4, padx=5, pady=5, ipady=10)

        self.filename_error = Label(self.history_frame, text="Error message if filename invalid",
                                    fg="#ab3a40")
        self.filename_error.grid(row=5)

        self.history_button_frame = Frame(self.history_frame, padx=5, pady=5)
        self.history_button_frame.grid(row=6)

        self.export_button = Button(self.history_button_frame, text="Export",
                                    bg="#1c2591", fg="#FFFFFF", activebackground="#121969",
                                    width=7)
        self.export_button.grid(row=0, column=0)

        self.close_button = Button(self.history_button_frame, text="Close",
                                   bg="#b1b1b3", fg="#FFFFFF",
                                   command=partial(self.close_history, partner),
                                   activebackground="#a1a1a1", width=7)
        self.close_button.grid(row=0, column=1)

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
