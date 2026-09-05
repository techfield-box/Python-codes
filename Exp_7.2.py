import tkinter as tk
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect('spandan.csv')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students (name TEXT,branch TEXT,fav_game TEXT)')
conn.commit()

def submit():
        cursor.execute('INSERT INTO students VALUES(?, ?, ?)',(e1.get(),e2.get(),e3.get()))
        conn.commit()
        messagebox.showinfo("SUCCESS","DATA SAVED!")
        e1.delete(0,tk.END); e2.delete(0,tk.END); e3.delete(0,tk.END)
        
def view():
        new_win=tk.Toplevel(root)
        new_win.title("Records")
        cursor.execute('SELECT*FROM students')
        rows=cursor.fetchall()
        
        for i,row in enumerate(rows):
                tk.Label(new_win,text=f"{row[0]} | {row[1]} | {row[2]}").pack()
                

root=tk.Tk()
root.title("Spandan Registration")

tk.Label(root,text="Name:").grid(row=0, column=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)

tk.Label(root,text="Branch:").grid(row=1, column=0)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)

tk.Label(root,text="Fav Game:").grid(row=2, column=0)
e3 = tk.Entry(root)
e3.grid(row=2, column=1)    

tk.Button(root,text="Submit", command=submit).grid(row=3, column=0)
tk.Button(root,text="View Records", command=view).grid(row=3, column=1)

root.mainloop()
