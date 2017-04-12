from tkinter import *
from tkinter import messagebox

def ask_quit():
    if messagebox.askyesno("Notice","Exit?"):
        root.destroy()

def cal():
    window = Toplevel(root)
    window.title("Answer:")
    ##window.config(width=800)
    ##print("It is running.")
    Label(window,text = v.get(),font = ('Courier,48')).pack(fill = Y, expand = 1, side =LEFT)
##    Label(window,text = "=",font = ('Courier,48')).grid(row = 0,column = 1)
    Label(window,text = '='+str(eval(v.get())),font = ('Courier,48')).pack(fill = Y, expand = 1, side =LEFT)

root = Tk()
root.protocol("WM_DELETE_WINDOW",ask_quit)
m = Menu(root)
root.config(height=400,width=800)
root.title("Calculator")
##root.geometry("800x800")

##设置菜单栏
root.config(menu=m)

##添加菜单标签1：File
filemenu = Menu(m)
m.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")

##添加菜单标签2：Tool
toolmenu = Menu(m)
m.add_cascade(label="tool",menu=toolmenu)
# toolmenu.add_command(label="New")
# toolmenu.add_command(label="Open...")
# toolmenu.add_command(label="Save")
# toolmenu.add_separator()
# toolmenu.add_command(label="Exit")

##添加菜单标签3：Help
helpmenu = Menu(m)
m.add_cascade(label="help",menu=helpmenu)
# helpmenu.add_command(label="New")
# helpmenu.add_command(label="Open...")
# helpmenu.add_command(label="Save")
# helpmenu.add_separator()
# helpmenu.add_command(label="Exit")

##Label(root,text="Please input your equation:").grid(sticky=E)
##v = StringVar()
##Entry(root,textvariable=v).grid(row=0,column=1)
##Button(root,text="OK",command=cal).grid(row=0,column=2)
Label(root,text="Please input your equation:").place(x=100,y=180)

v = StringVar()
ent=Entry(root,textvariable=v)
ent.place(x=400,y=180)

##ent.bind("<Enter>",cal);ent.focus_set()



Button(root,text="OK",command=cal).place(x=600,y=180)

root.mainloop()


