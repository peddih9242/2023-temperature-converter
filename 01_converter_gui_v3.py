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
                                activebackground="#bf8d0d")
        self.help_info.grid(row=1, column=0, padx=5, pady=5)

        self.history_export = Button(self.button_frame, text="History / Export",
                                     bg="#2a0e99",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     state=DISABLED, activebackground="#1f0878")

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

            # -- delete code below when history component is working
            print(self.all_calculations)

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
