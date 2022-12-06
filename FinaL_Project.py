from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import LANGUAGES
from tkinter import filedialog
import translate
from PIL import Image, ImageTk


# FUNCTIONS
def clear():
    des_text.delete(0.0, END)
    src_text.delete(0.0, END)


def translator():
    c = src_lang.get()
    c1 = des_lang.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, translator)


def trans():
    if len(src_text.get("1.0",END))==1 and len(des_text.get("1.0",END))==1:
        messagebox.showerror("Error !", 'Pls fill the text box before translating ')
    else:
        translator2 = translate.Translator(to_lang=des_lang.get())
        translated = translator2.translate(src_text.get(0.0, END))
        des_text.delete(1.0, END)
        des_text.insert(0.0, translated)
        values = "\n" + src_text.get("1.0",END) + "\n" + des_text.get("1.0",END)
        print(values)


# GUI
root = Tk()
root.title("Google Translator")
root.geometry("1040x350")
root.resizable(False, False)
root.configure(background="#b4cbfe")

#MenuBar
def save_as():
    myFile = filedialog.asksaveasfilename(defaultextension='.html')

    if not myFile:
        return

    with open(myFile, 'w', encoding='utf-8') as f:
        values = "\n" + src_text.get("1.0",END) + "\n" + des_text.get("1.0",END)
        f.write(values)

def new():
    new_window= Toplevel(root)
    new_window.title("Feedback")
    new_window.geometry("400x400")
    new_window["bg"]="powder blue"

    l1= Label(new_window, text="Feedback Form",font=("Calibri",30), bg="powder blue")
    l1.place(x=100,y=40)

    name_label = Label(new_window, text="FullName", bg="powder blue")
    name_label.place(x=70, y=130)

    name_entrytext = Entry(new_window)
    name_entrytext.place(x=240, y=130)

    email_label = Label(new_window, text="Email", bg="powder blue")
    email_label.place(x=70, y=180)

    email_entrytext = Entry(new_window)
    email_entrytext.place(x=240, y=180)

    def submit():
        Rbutton = var.get()
        if (Rbutton == 1):
            radio = "Yes"
        else:
            radio= "No"

        user_values = "\n" + name_entrytext.get() + "\n" + email_entrytext.get() + "\n" + radio
        print(user_values)
        file = open("Translator.txt", 'a')
        file.write(user_values)
        file.close()

    r_label = Label(new_window, text="Liked the Translator?", bg="powder blue")
    r_label.place(x=70, y=230)

    var = IntVar()
    radiobutton = Radiobutton(new_window, text="Yes", value=1, variable=var, bg="powder blue")
    radiobutton.place(x=235, y=230)

    radiobutton1 = Radiobutton(new_window, text="No", value=2, variable=var, bg="powder blue")
    radiobutton1.place(x=290, y=230)

    button_1 = Button(new_window, text="Submit", width=15, bg="powder blue", command=submit)
    button_1.place(x=180, y=280)


menu_example=Menu(root)
file_menu = Menu(menu_example)
file_menu.add_command(label="Open")
file_menu.add_command(label="New Window", command=new)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="Exit",command=root.destroy)
menu_example.add_cascade(label="File",menu=file_menu)


edit_menu = Menu(menu_example)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Copy")
menu_example.add_cascade(label="Edit",menu=edit_menu)
root.config(menu=menu_example)

# WIDGET 1
Frame1 = Frame(root, bg="#b4cbfe", bd=5)
Frame1.place(x=10, y=120, width=410, height=180)

src_text = Text(root, font="arial 10", height=10, wrap=WORD, padx=6, pady=10, width=52, relief=GROOVE)
src_text.place(x=14, y=120)

scrollbar = Scrollbar(Frame1)
scrollbar.pack(side="right", fill="y")
scrollbar.configure(command=src_text.yview)
src_text.configure(yscrollcommand=scrollbar.set)

# WIDGET 2
Frame2 = Frame(root, bg="#b4cbfe", bd=5)
Frame2.place(x=600, y=120, width=410, height=180)

des_text = Text(root, font="arial 10", height=10, wrap=WORD, padx=4, pady=10, width=53, relief=GROOVE)
des_text.place(x=600, y=120)

scrollbar_2 = Scrollbar(Frame2)
scrollbar_2.pack(side="right", fill="y")
scrollbar_2.configure(command=des_text.yview)
des_text.configure(yscrollcommand=scrollbar_2.set)

# LANGUAGE COMBOBOX
lang = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=lang, width=30)
src_lang.place(x=140, y=20, height=25)
src_lang.set("English")

des_lang = ttk.Combobox(root, values=lang, width=30)
des_lang.place(x=740, y=20, height=25)
des_lang.set("Hindi")


# IMAGE
arrow_img = ImageTk.PhotoImage(Image.open("arrow.png"))
image_label = Label(root, image=arrow_img, width=88, height=50)
image_label.place(x=466, y=50)

language = googletrans.LANGUAGES
language_ = list(language.values())
lang1 = language.keys()

# LABELS
label1 = Label(root, text="English", font="segoe 30 bold", bg="#ff7caf", width=17, relief=GROOVE)
label1.place(x=14, y=50)

label2 = Label(root, text="Hindi", font="segoe 30 bold", bg="#ff7caf", width=17, relief=GROOVE)
label2.place(x=600, y=50)

# BUTTONS
button_trans = Button(root, text="Click me \n Translate", font="Imapact 15 bold italic",
                      activebackground="purple", cursor="hand2", bd=5, bg="blue", fg="white", command=trans)

button_trans.place(x=452, y=230)

button_2 = Button(root, text="Clear", font="Imapact 10 bold", bg="powder blue",
                  activebackground="red", fg="black", width=10, command=clear)

button_2.place(x=463, y=190)

# CALLING FUNCTION SO THAT LABEL NAME CHANGES
translator()

root.mainloop()
