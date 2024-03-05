import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("Own To-Do List")

def task_adding():
    todo = task_add.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()  # Get priority input
    if todo != "":
        todo_box.insert(tkinter.END, f"Priority: {priority}, Task: {todo} - Due Date: {due_date}")
        task_add.delete(0, tkinter.END)
        due_date_entry.delete(0, tkinter.END)
        priority_entry.delete(0, tkinter.END)  # Clear priority entry after adding task
    else:
        tkinter.messagebox.showwarning(title="Attention !!", message="To add a task, please enter some task")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention !!", message="To delete a task, you must select a task !!")

def task_load():
    try:
        todo_list = pickle.load(open("tasks.dat", "rb"))
        todo_box.delete(0, tkinter.END)
        for todo in todo_list:
            todo_box.insert(tkinter.END, todo)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Attention !!", message="Cannot find tasks.dat")

def task_save():
    todo_list = todo_box.get(0, tkinter.END)
    pickle.dump(todo_list, open("tasks.dat", "wb"))

list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=20, width=50)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
scroller.config(command=todo_box.yview)

task_add = tkinter.Entry(window, width=50)
task_add.pack()

due_date_label = tkinter.Label(window, text="Due Date (YYYY-MM-DD):")
due_date_label.pack()

due_date_entry = tkinter.Entry(window, width=50)
due_date_entry.pack()

priority_label = tkinter.Label(window, text="Task Priority:")  # New label for priority
priority_label.pack()

priority_entry = tkinter.Entry(window, width=50)  # Entry widget for priority
priority_entry.pack()

add_task_button = tkinter.Button(window, text="CLICK TO ADD TASK", font=("arial", 20, "bold"), bg="red", width=40, command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="CLICK TO DELETE TASK", font=("arial", 20, "bold"), bg="yellow", width=40, command=task_removing)
remove_task_button.pack()

load_task_button = tkinter.Button(window, text="CLICK TO LOAD TASK", font=("arial", 20, "bold"), bg="green", width=40, command=task_load)
load_task_button.pack()

save_task_button = tkinter.Button(window, text="CLICK TO SAVE", font=("arial", 20, "bold"), bg="blue", width=40, command=task_save)
save_task_button.pack()

window.mainloop()
