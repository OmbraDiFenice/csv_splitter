import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from splitter import split_csv
import os


def ask_for_input_file(input_file_var: tk.Variable) -> None:
    input_file_path = filedialog.askopenfilename()
    input_file_var.set(input_file_path)


def ask_for_output_dir(output_dir_var: tk.Variable) -> None:
    output_dir_path = filedialog.askdirectory()
    output_dir_var.set(output_dir_path)


def do_split(input_file: str, output_file: str, rows_per_file: int,
             status_var: tk.Variable) -> None:
    try:
        split_csv(input_file, output_file, rows_per_file)
        status_var.set("Done")
    except Exception as e:
        status_var.set(str(e))


def app():
    root = tk.Tk()
    root.title("CSV splitter")
    root.geometry("300x200")

    status_var = tk.Variable()

    input_file_var = tk.Variable()
    ttk.Label(root, textvariable=input_file_var, relief=tk.SUNKEN).pack(fill=tk.X, expand=True)
    ttk.Button(root, text="Input CSV",
               command=lambda: ask_for_input_file(input_file_var)).pack()

    output_dir_var = tk.Variable(value=os.getcwd())
    ttk.Label(root, textvariable=output_dir_var, relief=tk.SUNKEN).pack(fill=tk.X, expand=True)
    ttk.Button(root, text="Output directory",
               command=lambda: ask_for_output_dir(output_dir_var)).pack()

    rows_per_file_var = tk.Variable(value=50)
    number_cb = root.register(lambda text: text.isdigit() or text == "")
    ttk.Label(root, text="Number of rows per csv").pack()
    ttk.Entry(root, textvariable=rows_per_file_var,
              validate="all",
              validatecommand=(number_cb, "%P")).pack()

    ttk.Button(root, text="Split!",
               command=lambda: do_split(
                   input_file_var.get(),
                   output_dir_var.get(),
                   int(rows_per_file_var.get()),
                   status_var,
                )).pack()

    ttk.Label(root, textvariable=status_var).pack(fill=tk.X, expand=True)

    tk.mainloop()


if __name__ == "__main__":
    app()
