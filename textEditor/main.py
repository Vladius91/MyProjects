import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

from astroid import Lambda


def open_file(window, text_edit):
    # e o "aplicatie" externa/ meniul de deschidere a fisierelor
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0,tkinter.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tkinter.END, content)
    window.title(f"OpenFile:{filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    with open(filepath,"w") as f:
        content = text_edit.get(1.0,tkinter.END)
        f.write(content)
    window.title(f"OpenFile:{filepath}")



def main():

    #arhitextura applicatiei
    window = Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1,minsize=500)

    #fontul
    text_edit = tkinter.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    #bara de setari + butoane
    #bara de setari + butoane
    frame = tkinter.Frame(window, relief=tkinter.RAISED, bd=2, )
    save_button = tkinter.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tkinter.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5)
    open_button.grid(row=1, column=0, padx=5)
    frame.grid(row=0, column=0, sticky="ns")

#scortcuts
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


main()