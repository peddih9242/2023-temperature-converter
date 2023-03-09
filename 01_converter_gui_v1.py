from tkinter import *

class Converter:

    def __init__(self):

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

        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9C0000")
        self.temp_error.grid(row=3)

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
                                           font=button_font, width=12)
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

        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # check for error and make history button normal if valid input given
        if has_error == "yes":
            print(self.temp_error.config(text=error, fg="#9C0000"))
        else:
            print(self.temp_error.config(text="You are OK", fg="blue"))

            # enable history button if valid input given
            self.history_export.config(state=NORMAL)

            return response


    # check temperature is more than -459 and convert it
    def to_celsius(self):

        self.temp_check(-459)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()