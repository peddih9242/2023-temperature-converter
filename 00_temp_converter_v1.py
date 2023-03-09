# import modules
from tkinter import *
from functools import partial  # to prevent unwanted windows
from datetime import date
import re


# converter class
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

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter",
                                  font=("Arial", "16", "bold"))

        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame, text=instructions,
                                       wraplength=250, width=40, justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        self.output_label = Label(self.temp_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame, text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=lambda: self.temp_convert(-459),
                                        activebackground="#8a018a")
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame, text="To Fahrenheit",
                                           bg="#009900",
                                           fg=button_fg,
                                           font=button_font, width=12,
                                           command=lambda: self.temp_convert(-273),
                                           activebackground="#017301")
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_info = Button(self.button_frame, text="Help / Info",
                                bg="#e6ab17",
                                fg=button_fg,
                                font=button_font, width=12,
                                activebackground="#bf8d0d",
                                command=self.help_info)

        self.help_info.grid(row=1, column=0, padx=5, pady=5)

        self.history_export = Button(self.button_frame, text="History / Export",
                                     bg="#2a0e99",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     state=DISABLED, activebackground="#1f0878",
                                     command=lambda: self.to_history(self.all_calculations))

        self.history_export.grid(row=1, column=1, padx=5, pady=5)

    def help_info(self):
        DisplayHelp(self)

    def to_history(self, all_calculations):
        DisplayHistory(self, all_calculations)

    # temperature checking function, takes a minimum value and makes sure
    # number input is larger than min value
    def temp_check(self, min_value):

        has_error = "no"
        error = "Please enter a number larger than {}.".format(min_value)

        response = self.temp_entry.get()
        try:

            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # if errors found set variables to show error
        if has_error == "yes":

            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            # return number to be converted and enable history button
            self.history_export.config(state=NORMAL)
            return response

    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)

    # check temperature is valid then convert it
    def temp_convert(self, min_val):
        to_convert = self.temp_check(min_val)
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        elif min_val == -459:
            # do calculation
            answer = (to_convert - 32) * 5 / 9
            rounded_answer = self.round_ans(answer)
            rounded_to_convert = self.round_ans(to_convert)
            from_to = "{} F is {} C".format(rounded_to_convert, rounded_answer)

        # convert to fahrenheit
        else:
            answer = to_convert * 1.8 + 32
            rounded_answer = self.round_ans(answer)
            rounded_to_convert = self.round_ans(to_convert)
            from_to = "{} C is {} F".format(rounded_to_convert, rounded_answer)

        if set_feedback == "yes":
            # create user output and add to calculation history
            feedback = from_to.format(to_convert, answer)
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

        self.output_answer()

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):

        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.temp_entry.config(bg="#F8CECC")
            self.output_label.config(fg="#9C0000")

        else:
            self.temp_entry.config(bg="#FFFFFF")
            self.output_label.config(fg="#004C00")

        self.output_label.config(text=output)


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


class DisplayHistory:

    def __init__(self, partner, all_calculations):

        self.history_box = Toplevel()

        # set maximum number of calculations to 5
        # which can be changed to show fewer / more calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # set up filename & calculation strings
        self.var_filename = StringVar()
        self.var_calc_string = StringVar()
        self.var_calc_list = StringVar()
        self.var_todays_date = StringVar()

        # make a calculation string from oldest to newest (only used when exporting)
        calc_history_text = ""
        for item in all_calculations:
            calc_history_text += item
            calc_history_text += "\n"

        self.var_calc_list.set(calc_history_text)

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
        self.var_calc_string.set(calc_string_text)

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

        self.filename_feedback = Label(self.history_frame, text="",
                                       wraplength=300,
                                       font=("Arial", "13", "bold"))
        self.filename_feedback.grid(row=5)

        self.history_button_frame = Frame(self.history_frame, padx=5, pady=5)
        self.history_button_frame.grid(row=6)

        self.export_button = Button(self.history_button_frame, text="Export",
                                    bg="#1c2591", fg="#FFFFFF", activebackground="#121969",
                                    width=7, command=lambda: self.make_file())
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

        return filename

    # retrieves date and creates DD_MM_YYYY string
    def get_date(self):
        today = date.today()
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        todays_date = "{}/{}/{}".format(day, month, year)
        self.var_todays_date.set(todays_date)

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

    # give feedback to user based on if valid input given
    def make_file(self):

        # retrieve filename
        filename = self.filename_entry.get()

        if filename == "":
            # get date and create default filename
            filename = self.filename_maker(filename)

        # check that filename is valid
        valid = self.check_filename(filename)

        # shows output to show the user if input was okay or not
        if valid == "":
            filename += ".txt"
            exported_text = "Success! Your calculation history has been saved as {}".format(filename)
            self.filename_entry.config(bg="#b3e8b5")
            self.filename_feedback.config(text=exported_text, fg="#108f16")
            self.var_filename.set(filename)

            # write content to file
            self.write_to_file()

        else:
            self.filename_entry.config(bg="#eda4a4")
            self.filename_feedback.config(text=valid, fg="#ab3a40")

    def write_to_file(self):

        # get calculation string and set stringvar filename
        self.get_date()

        generated_date = self.var_todays_date.get()
        filename = self.var_filename.get()

        # set up strings to be written to file
        heading = "**** Temperature Calculations ****\n"
        date_generated = "Generated: {}\n".format(generated_date)
        sub_heading = "Here is your calculation history from oldest to newest."
        calc_list = self.var_calc_list.get()

        output_list = [heading, date_generated, sub_heading, calc_list]

        # open text file
        export_file = open(filename, "w+")

        # write output to file
        for item in output_list:
            export_file.write(item)
            export_file.write("\n")

        # close text file
        export_file.close()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
