from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

#TKINTER used for GUI 
#Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
#It is a thin object-oriented layer on top of Tcl/Tk.
#It is easy to use, and it is very portable, so it can run on many different platforms.
#It is a Light weight GUI toolkit.

#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"


window = Tk()
window.title("")
window.geometry("485x450")
window.configure(background=co0)
window.resizable(width=FALSE,height=FALSE)

#root = Tk()
#root.geometry("485x450")


#frames
frame_up = Frame(window, bg=co2, width=500, height=50)
frame_up.grid(row=0, column=0, sticky="nsew", padx=0 , pady=1)

frame_down = Frame(window, bg=co0, width=500, height=150)
frame_down.grid(row=1, column=0, sticky="nsew", padx=0 , pady=1)

frame_table = Frame(window, bg=co0, width=500, height=100, relief="flat")
frame_table.grid(row=2, column=0, sticky="NW", columnspan=2, padx=10 , pady=1,)

#Function
def show():
    global tree 
    
    listheader = ['Name','Gender','Telephone']
    demo_list =  view()
    
    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")
    
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.yview)
    
    tree.configure(yscrollcommand=vsb.set , xscrollcommand=hsb.set)
    
    tree.grid(column=0,row=0, sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')
    
    #tree head
    
    tree.heading(0, text ='Name', anchor=NW)
    tree.heading(1, text ='Gender', anchor=NW)
    tree.heading(2, text ='Telephone', anchor=NW)
    
    #tree colums
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=150, anchor='nw')
    tree.column(2, width=200, anchor='nw')
    
    for item in demo_list:
        tree.insert('', 'end', values=item)
    
    
show()

def insert():
    Name = e_name.get()
    Gender = c_gender.get()
    telephone = e_telephone.get()
    
    
    data = [Name, Gender, telephone]
    
    
    if Name == '' or Gender == '' or telephone == '' :
        messagebox.showerror("Error", "Please fill all fields")
    else:
        add(data)
        messagebox.showinfo('data', 'data add done')
        
        e_name.delete(0, 'end')
        c_gender.delete(0,'end')
        e_telephone.delete(0, 'end')
        
        show()
        
        
def to_update():
    try:
        tree_data = tree.focus()
        tree_dictinory = tree.item(tree_data)
        tree_list = tree_dictinory['values']
        
        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        
        e_name.insert(0, Name)
        c_gender.insert(0, Gender)
        e_telephone.insert(0, Telephone)
        
        def confirm():
            new_name = e_name.get()
            new_gender = c_gender.get()
            new_telephone = e_telephone.get()
            
            data = [new_telephone,new_name, new_gender, new_telephone]
            
            update(data)
            
            messagebox.showinfo('Success', 'Data updated')
            
            e_name.delete(0, 'end')
            c_gender.delete(0, 'end')
            e_telephone.delete(0, 'end')
            
            for widget in frame_table.winfo_children():
                widget.destroy()
                
            b_confirm.destroy()
            
            show()
            
        b_confirm = Button(frame_down, text="Confirm",width=10, height=1, font=('Ivy 8 bold'), bg=co2, fg=co0 , command= confirm)
        b_confirm.place(x= 290 , y= 110 )
        
    except IndexError:
        messagebox.showinfo('Error', 'Select data')
        
        
def to_remove():
    try :
        tree_data = tree.focus()
        tree_dictinory = tree.item(tree_data)
        tree_list = tree_dictinory['values']
        tree_telephone = str(tree_list[2])
        
        remove(tree_telephone)
        
        messagebox.showinfo('Success', 'Data removed')
        
        for widget in frame_table.winfo_children():
             widget.destroy()
     
        show()
                 
    except IndexError:
        messagebox.showinfo('Error', 'Select data')
        
        
def to_search():
    telephone = e_search.get()
    
    data = search(telephone)
    
    def delete_command():
        tree.delete(*tree.get_children())
        
    delete_command()
    
    for item in data:
        tree.insert('', 'end', values=item)
        
    e_search.delete(0, 'end')


def check_number():
    number = e_telephone.get()
    if len(number) == 10 and number.startswith("9"):
        messagebox.showinfo("Success", "Number is correct")
    else:
        messagebox.showerror("Error", "Number is incorrect")
    
Button_check = Button(frame_down, text="Check Number", command=check_number)
Button_check.pack(side=TOP)
Button_check.place(x=120, y=120)

#frame_up widgets

app_name = Label(frame_up, text="Contacts 📞", height=1,font=('verdana 17 bold'),bg= co2,fg= co0)
app_name.grid(row=0, column=0, sticky="nsew", padx=10)
app_name.place(x=5, y=5)
# Button_check = Button(frame_down, text="Check Number", command=check_number)
# Button_check.pack(side=TOP)
# Button_check.place(x=120, y=120)

#frame_down widgets 
l_name = Label(frame_down, text="Name *", width= 20, height=1, font=('Ivy 10'), bg=co0 , anchor=NW)
l_name.grid(row=0, column=0, sticky="nsew", padx=10)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25,  justify='left',highlightthickness=1,relief="solid")
e_name.grid(row=0, column=1, sticky="nsew", padx=10)
e_name.place(x=80, y=20)

# e_gender = ttk.Combobox(frame_down, width=25, justify='left')
# e_gender['values'] = ("Male", "Female", "Other")
# e_gender.grid(row=0, column=1, sticky="w", padx=10, pady=10)

l_gender = Label(frame_down, text="Gender *", width= 20, height=1, font=('Ivy 10'), bg=co0 , anchor=NW)
l_gender.grid(row=0, column=0, sticky="nsew", padx=10)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['','Male','Female']
c_gender.grid(row=0, column=1, sticky="nsew", padx=10)
c_gender.place(x=80, y=50)


l_telephone = Label(frame_down, text="Telephone *",height=1, font=('Ivy 10'), bg=co0 , anchor=NW,)
l_telephone.grid(row=0, column=0, sticky="nsew", padx=10)
l_telephone.place(x=10, y=80)
e_telephone = Entry(frame_down, width=25,  justify='left',highlightthickness=1,relief="solid")
e_telephone.grid(row=0, column=1, sticky="nsew", padx=10)
e_telephone.place(x=80, y=80)

b_search = Button(frame_down, text="Search",height=1, font=('Ivy 8 bold'), bg=co2, fg=co0, command= to_search)
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=16,  justify='left',font=('Ivy',11),highlightthickness=1,relief='solid')
e_search.place(x=347, y=20)

b_view = Button(frame_down, text="View",width=10, height=1, font=('Ivy 8 bold'), bg=co2, fg=co0 , command=show)
b_view.place(x=290, y=50)

b_add = Button(frame_down, text="Add",width=10, height=1, font=('Ivy 8 bold'), bg=co2, fg=co0, command=insert)
b_add.place(x=400, y=50)

b_update = Button(frame_down, text="Update",width=10, height=1, font=('Ivy 8 bold'), bg=co2, fg=co0, command= to_update)
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text="Delete",width=10, height=1, font=('Ivy 8 bold'), bg=co2, fg=co0 , command=to_remove)
b_delete.place(x=400, y=110)

window.mainloop()
