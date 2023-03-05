from tkinter import *
from functools import partial  # to prevent unwanted windows
from datetime import date
import re

class Converter:

    def __init__(self):
        self.all_calculations = ['0 F is -18 C', '0 C is 32 F', '11 F is -12 C',
                                 '11 C is 52 F', '12 F is -11 C']

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
                                     command=lambda: self.to_history(self.all_calculations))
        self.history_export.grid(row=1, column=0, padx=5, pady=5)

    def to_history(self, all_calculations):
        DisplayHistory(self, all_calculations)


class DisplayHistory:

    def __init__(self, partner, all_calculations):

        self.history_box = Toplevel()

        # set maximum number of calculations to 5
        # which can be changed to show fewer / more calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

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

        num_calcs = len(all_calculations)

        max_calcs = 5

        # function converts contents of calculation list into a string
        calc_string_text = self.get_calc_string(all_calculations)

        if num_calcs > max_calcs:
            calc_background = "#FFE6CC"  # peach colour
            showing_all = "Below are your recent calculations - showing {} / {}" \
                          " calculations. Please export your calculations " \
                          "to see your full calculation history".format(max_calcs, num_calcs)

        else:
            calc_background = "#B4FACB"  # pale green colour
            showing_all = "Below is your calculation history."

        # history text and label
        hist_text = "{} \n\nAll calculations are shown to the nearest degree.".format(showing_all)

        self.history_text = Label(self.history_frame, text=hist_text,
                                  wraplength=300, width=50, justify="left")
        self.history_text.grid(row=1, padx=5, pady=5)

        self.show_history = Label(self.history_frame, text=calc_string_text,
                                  width=40, background=calc_background, wraplength=300)

        self.show_history.grid(row=2, padx=5, pady=5)

        export_text = "Either choose a custom file name (and push <Export>) or" \
                      "simply push <Export> to save your calculations in a text" \
                      "file. If the filename already exists, it will be overwritten."

        self.export_text = Label(self.history_frame, text=export_text,
                                 width=50, wraplength=300,
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
                                    width=7, command=lambda: self.filename_maker(self.filename_entry.get()))
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

    # change calculation list into a string so that it can
    # be outputted as a label
    def get_calc_string(self, var_calculations):
        # get maximum calculations to display
        # (was set in __init__ function)
        max_calcs = self.var_max_calcs.get()
        calc_string = ""

        # work out how many times we need to loop
        # to output either last five calcs or all calcs
        if len(var_calculations) >= max_calcs:
            stop = max_calcs

        else:
            stop = len(var_calculations)

        # iterate to all but last item,
        # adding item and line break to calculation string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations) - item - 1]

            calc_string += "\n"

        # add final item without an extra linebreak
        # ie: last item on list will be fifth from the end
        if len(var_calculations) >= max_calcs:
            calc_string += var_calculations[-max_calcs]
        else:
            calc_string += var_calculations[0]

        return calc_string

    # if filename is blank, returns default name
    # otherwise checks filename and either returns
    # an error or returns the filename (with .txt extension)
    def filename_maker(self, filename):

        # creates default filename
        # (YYYY_MM_DD_temperature_calculations)
        if filename == "":

            # set filename_ok to "" so we can see
            # default name for testing purposes
            filename_ok = ""
            date_part = self.get_date()
            filename = "{}_temperature_calculations".format(date_part)

        # checks filename has only a-z / A-Z / underscores
        else:
            filename_ok = self.check_filename(filename)

        if filename_ok == "":
            filename += ".txt"

        else:
            filename = filename_ok

        return filename


    # retrieves date and creates DD_MM_YYYY string
    @staticmethod
    def get_date():
        today = date.today()
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        return "{}_{}_{}".format(day, month, year)


    # checks that filename only contains letters,
    # numbers and underscores. returns either "" if
    # filename is ok or the problem if an error is found
    @staticmethod
    def check_filename(filename):
        problem = ""

        # regular expression to check filename is valid
        valid_char = "[A-za-z0-9_]"

        # iterates through filename and checks each character
        for character in filename:
            if re.match(valid_char, character):
                continue

            elif character == " ":
                problem = "Sorry, no spaces allowed"

            else:
                problem = "Sorry, no {}'s allowed".format(character)
            break

        if problem != "":
            problem = "{}. Use letters / numbers / " \
                    "underscores only".format(problem)

        return problem

        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
