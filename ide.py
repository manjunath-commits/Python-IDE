from tkinter import *
import tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from tkinter import font

compiler = Tk()
compiler.title('A Simple Python IDE')
compiler.geometry("600x600")
pyLogo = PhotoImage(file='python.png')
compiler.iconphoto(False, pyLogo)

file_path = ''
def set_path(path):
    global file_path
    file_path = path

#save as function
def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_path(path)
        compiler.title(path.split('/')[-1])

#open file function
def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_path(path)
        compiler.title(path.split('/')[-1])

#run function
def run():
    if file_path == '':
        save_prompt = Toplevel(background="#20232A")
        save_prompt.iconphoto(False,pyLogo)
        save_prompt.geometry("140x60")
        text = Label(save_prompt, 
            text='Please save your code',
            background="#20232A",
            fg="White",
            padx=20,
            pady=20)
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    code_output.delete('1.0',END)
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)

#file menu
menu_bar = Menu(compiler,background='Blue',fg='White')
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

#run menu
menu_bar.add_command(label='Run', command=run)
compiler.config(menu=menu_bar)

#editor
editor = Text(height=28,
            background="#20232A",
            fg="White",
            insertbackground='yellow',
            font = ("Lucida Sans Typewriter", 10))
editor.pack()

#output
code_output = Text(height=10,
                background="#20232A",
                fg="Yellow",
                font = ("Lucida Sans Typewriter", 10))
code_output.pack()
output_label = tkinter.Label(editor, text='Output',background="White",fg="Black",width=90)
output_label.place(relx = 0.0,
                   rely = 1.0,
                   anchor = 'sw')

compiler.mainloop()

