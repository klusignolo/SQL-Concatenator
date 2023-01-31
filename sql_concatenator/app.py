import tkinter as tk
import sql_concatenator.utils.tkinter_utils as tk_utils
import random


# ************** GLOBAL VARIABLES (fonts, really) *************

NORM_FONT = ("Verdana", 10)
HEADER_FONT = ("Verdana", 12, "bold")
BOLD_FONT = ("Verdana", 10, "bold")
STRIKE_FONT = ("Verdana", 10, "overstrike")


# ************** Main App *************

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("SQL Query Concatenator 2022.0")

        MainFrame(self).grid()
        

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=master)

        self.line_check_var = tk.IntVar(value=1)
        self.custom_check_var = tk.IntVar(value=0)

        # ************ Declare TKinter UI Stuff *********************
        input_label = tk.Label(self, text="Input:", font=HEADER_FONT)
        output_label = tk.Label(self, text="Output:", font=HEADER_FONT)
        self.copy_label = tk.Label(self, font=NORM_FONT)
        delimiter_label = tk.Label(self, font=BOLD_FONT, text="Delimiter:")

        self.input_entry = tk.Text(self, width=45, height=20, font=NORM_FONT)
        self.output_entry = tk.Text(self, width=45, height=20, font=NORM_FONT)
        self.custom_check_entry = tk.Entry(self, width=5, font=NORM_FONT)
        tk_utils.update_widget_text(self.custom_check_entry, ",")

        self.line_check = tk.Checkbutton(self, variable=self.line_check_var, text="Line")
        self.custom_check = tk.Checkbutton(self, variable=self.custom_check_var, text="Custom:")

        concatbtn = tk.Button(self, text="Concatenate!", width=25, command=self.concat_button_pressed)
        clipbtn = tk.Button(self, text="Copy to Clipboard!", width=25, command=self.clip_button_pressed)

        # *********** Now, grid the stuff. ********

        # Labels
        input_label.grid(row=0, column=0, columnspan=2)
        output_label.grid(row=0, column=2, columnspan=2)
        delimiter_label.grid(row=1, column=4, sticky='w', columnspan=2)
        self.copy_label.grid(row=6, column=4, columnspan=2)

        # Entries
        self.custom_check_entry.grid(row=3, column=5, sticky='w')

        # Text Entries
        self.input_entry.grid(row=1, column=0, columnspan=2, rowspan=12, padx=3, pady=3)
        self.output_entry.grid(row=1, column=2, columnspan=2, rowspan=12)

        # Checkboxes
        self.line_check.grid(row=2, column=4, sticky='w')
        self.custom_check.grid(row=3, column=4, sticky='w')

        # Buttons
        concatbtn.grid(row=4, column=4, columnspan=2, padx=5)
        clipbtn.grid(row=5, column=4, columnspan=2, padx=5)

        self.input_entry.focus()

    def clip_button_pressed(self):
        tk_utils.clip(self, self.output_entry.get("1.0", tk.END))
        tk_utils.update_widget_text(self.copy_label, "Copied!")

    def concat_button_pressed(self):
        tk_utils.update_widget_text(self.copy_label, "")
        tk_utils.update_widget_text(self.output_entry, "")
        user_input: str = self.input_entry.get("1.0", tk.END)
        is_line_checked = self.line_check_var.get()
        is_custom_checked = self.custom_check_var.get()
        custom_delimiter = self.custom_check_entry.get()

        output = Concatenator.concatenate(
            input=user_input, 
            is_line_split=is_line_checked, 
            is_custom_split=is_custom_checked, 
            custom_delimiter=custom_delimiter
        )
        tk_utils.update_widget_text(self.output_entry, output)


class Concatenator:
    @staticmethod
    def concatenate(input: str, is_line_split: bool, is_custom_split: bool, custom_delimiter: str = ""):
        if input.strip() == "":
            return Concatenator.joyful_fellow()

        items_to_concatenate: list[str] = []

        if is_line_split and is_custom_split:
            split_rows = input.split('\n')
            items_to_concatenate = [row.strip().strip(custom_delimiter) for row in split_rows]

        elif is_custom_split and not is_line_split:
            items_to_concatenate = input.replace('\n', '').split(custom_delimiter)

        else:
            split_rows = input.split('\n')
            items_to_concatenate = [row.strip() for row in split_rows]
        

        for item in range(len(items_to_concatenate)):
            # Ignore blank lines and add single quotes
            if items_to_concatenate[item].strip() != '':
                items_to_concatenate[item] = "'" + items_to_concatenate[item].replace('\n', '') + "',"
        # Remove the last comma after the items are combined
        output = "".join(items_to_concatenate)[:-1]
        return "(" + output + ")"

    @staticmethod
    def joyful_fellow() -> str:
        happy_faces = [
            "凸(⊙▂⊙ )", 
            "凸ಠ益ಠ)凸", 
            "凸-_-凸", 
            "凸(-_-ﾒ)", 
            "凸(¬‿¬)", 
            "ノಠ_ಠノ", 
            "⊙.☉",
            "◔_◔",
            "(ノ=Д=)ノ┻━┻",
            "ಠ╭╮ಠ",
            "(ノಠ益ಠ)ノ彡┻━┻"]
        return happy_faces[random.randint(0, len(happy_faces) - 1)]
