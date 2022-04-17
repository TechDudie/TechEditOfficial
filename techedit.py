import tkinter
import tkinter.filedialog
import os

root = tkinter.Tk()
root.title(f"techedit - {os.getcwd()}/Untitled")
global name
global noname
name = f"{os.getcwd()}/Untitled"
noname = True

def new():
    global name
    global noname
    if noname:
        name = tkinter.filedialog.asksaveasfilename()
        noname = False
    open(name, "w").close()
    root.title(f"techedit - {name}")

def ask():
    name = tkinter.filedialog.askopenfilename()
    text.delete("1.0", tkinter.END)
    try:
        text.insert(tkinter.END, open(name).read())
    except:
        return None
    noname = False
    root.title(f"techedit - {name}")

def save():
    global name
    global noname
    content = text.get("1.0","end-1c")
    if noname:
        name = tkinter.filedialog.asksaveasfilename()
        noname = False
    file_h = open(name, "w")
    file_h.write(content)
    file_h.close()

def saveas():
    global name
    global noname
    content = text.get("1.0","end-1c")
    name = tkinter.filedialog.asksaveasfilename()
    noname = False
    file_h = open(name, "w")
    file_h.write(content)
    file_h.close()

def select_all(event):
    text.tag_add(tkinter.SEL, "1.0", tkinter.END)
    text.mark_set(tkinter.INSERT, "1.0")
    text.see(tkinter.INSERT)
    return 'break'

menubar = tkinter.Menu(root, foreground='black', activebackground='white', activeforeground='black')
file = tkinter.Menu(menubar, tearoff=0)
file.add_command(label="New", command=new)
file.add_command(label="Open", command=ask)
file.add_command(label="Save", command=save)
file.add_command(label="Save As", command=saveas)
file.add_separator()
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)

root.grid_columnconfigure(0, weight=1)
global text
text = tkinter.Text(root, undo=True)
text.grid(row=0, column=0)

edit = tkinter.Menu(menubar, tearoff=0)
edit.add_command(label="Undo", command=lambda: text.edit_undo())
edit.add_command(label="Redo", command=lambda: text.edit_redo())
edit.add_separator()
edit.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
edit.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
edit.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
edit.add_separator()
edit.add_command(label="Select All", command=select_all)
menubar.add_cascade(label="Edit", menu=edit)

global rclick
rclick = tkinter.Menu(root, tearoff=0)
rclick.add_command(label="Undo", command=lambda: text.edit_undo())
rclick.add_command(label="Redo", command=lambda: text.edit_redo())
rclick.add_separator()
rclick.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
rclick.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
rclick.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
rclick.add_separator()
rclick.add_command(label="Select All", command=select_all)

def show_rclick(event):
    global rclick
    rclick.tk.call("tk_popup", rclick, event.x_root, event.y_root)

def cut(e): text.event_generate("<<Cut>>")
def copy(e): text.event_generate("<<Copy>>")
def paste(e): text.event_generate("<<Paste>>")
def undo(e): text.edit_undo()
def redo(e): text.edit_redo()

root.bind_class("Text", "<Button-3><ButtonRelease-3>", show_rclick)
root.bind_class("Text", "<Control-a>", select_all)
root.bind_class("Text", "<Control-x>", cut)
root.bind_class("Text", "<Control-c>", copy)
root.bind_class("Text", "<Control-v>", paste)
root.bind_class("Text", "<Control-z>", undo)
root.bind_class("Text", "<Control-y>", redo)

root.config(menu=menubar)
root.mainloop()
