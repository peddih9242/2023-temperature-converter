from tkinter import *

class Converter:

    def __init__(self):

        # initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

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
                                       wrap=250, width=40, justify="left")
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
                                        command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame, text="To Fahrenheit",
                                           bg="#009900",
                                           fg=button_fg,
                                           font=button_font, width=12,
                                           command=self.to_fahrenheit)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_info = Button(self.button_frame, text="Help / Info",
                                bg="#e6ab17",
                                fg=button_fg,
                                font=button_font, width=12)
        self.help_info.grid(row=1, column=0, padx=5, pady=5)

        self.history_export = Button(self.button_frame, text="History / Export",
                                     bg="#2a0e99",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     state=DISABLED)

        self.history_export.grid(row=1, column=1, padx=5, pady=5)

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


    # check temperature is more than -459 and convert it
    def to_celsius(self):

        to_convert_f = self.temp_check(-459)

        if to_convert_f != "invalid":
            # do calculation
            self.var_feedback.set("Converting {} to C :)".format(to_convert_f))

        self.output_answer()

    # check temperature is more than -273 and convert it
    def to_fahrenheit(self):

        to_convert_c = self.temp_check(-273)

        if to_convert_c != "invalid":
            # do calculation
            self.var_feedback.set("Converting {} to F :)".format(to_convert_c))

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

    def convert_to_celsius(self):
        self.to_convert_f

    def convert_to_fahrenheit(self):


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()