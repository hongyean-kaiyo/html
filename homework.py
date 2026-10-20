import tkinter as tk
from medule import *

# ---------- Colors ----------
BG = '#1e1e2e'        # window background
CARD = '#2a2a3d'      # panels
TEXT = '#cdd6f4'      # text
BLUE = '#7aa2f7'      # add buttons
RED = '#f7768e'       # delete buttons
GREEN = '#9ece6a'     # update / search buttons

root = tk.Tk()
root.geometry('600x520')
root.title('LinkedList')
root.config(bg=BG)

link = LinkedList()

def click_add_first():
    link.add_first(en1.get())
    la5.config(text=link.display())

def click_add_last():
    link.add_last(en1.get())
    la5.config(text=link.display())

def click_add_pos():
    link.add_position(en1.get(), int(en2.get()))
    la5.config(text=link.display())

def click_del_first():
    link.delete_first()
    la5.config(text=link.display())

def click_del_last():
    link.delete_last()
    la5.config(text=link.display())

def click_del_pos():
    link.delete_position(int(en2.get()))
    la5.config(text=link.display())

def click_update():
    link.update(en1.get(), int(en2.get()))
    la5.config(text=link.display())

def click_search():
    position = link.search(en1.get())
    if position:
        la4.config(text=f'Found at position {position}')
    else:
        la4.config(text='Not found')

def make_button(parent, text, command, color):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg='#1e1e2e',
        activebackground=TEXT,
        font=('Segoe UI', 10, 'bold'),
        relief='flat',
        cursor='hand2',
        width=18,
        pady=6
    )

la1 = tk.Label(
    root,
    text='LinkedList',
    bg=BG,
    fg=BLUE,
    font=('Segoe UI', 22, 'bold')
)
la1.pack(pady=(15, 5))

input_frame = tk.Frame(
    root,
    bg=CARD,
    padx=15,
    pady=15
)
input_frame.pack(padx=20, pady=10, fill='x')

la2 = tk.Label(
    input_frame,
    text='Value',
    bg=CARD,
    fg=TEXT,
    font=('Segoe UI', 10)
)
la2.grid(
    row=0,
    column=0,
    sticky='w',
    pady=5
)

en1 = tk.Entry(
    input_frame,
    font=('Segoe UI', 11),
    relief='flat',
    width=25
)
en1.grid(
    row=0,
    column=1,
    padx=10,
    ipady=4
)
la0 = tk.Label(
    input_frame,
    text='(Only For add & update)',
    bg=CARD,
    fg=TEXT,
    font=('Segoe UI', 10)
)
la0.grid(
    row=0,
    column=2,
    sticky='w',
    pady=5
)
la3 = tk.Label(
    input_frame,
    text='Position',
    bg=CARD,
    fg=TEXT,
    font=('Segoe UI', 10)
)
la3.grid(
    row=1,
    column=0,
    sticky='w',
    pady=5
)

en2 = tk.Entry(
    input_frame,
    font=('Segoe UI', 11),
    relief='flat',
    width=25
)
en2.grid(
    row=1,
    column=1,
    padx=10,
    ipady=4
)

btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=5)

buttons = [
    ('Add First', click_add_first, BLUE),
    ('Delete First', click_del_first, RED),
    ('Add Last', click_add_last, BLUE),
    ('Delete Last', click_del_last, RED),
    ('Add at Position', click_add_pos, BLUE),
    ('Delete at Position', click_del_pos, RED),
    ('Update', click_update, GREEN),
    ('Search', click_search, GREEN),
]

for i, cmd in enumerate(buttons):
    make_button(btn_frame, cmd[0], cmd[1], cmd[2])\
    .grid(
        row=i // 2,
        column=i % 2,
        padx=8,
        pady=6
    )

result_frame = tk.Frame(
    root,
    bg=CARD,
    padx=15,
    pady=15
)
result_frame.pack(padx=20, pady=15, fill='x')

la4 = tk.Label(
    result_frame,
    text='Result : ',
    bg=CARD,
    fg=GREEN,
    font=('Segoe UI', 11, 'bold')
)
la4.pack(anchor='w')

la5 = tk.Label(
    result_frame,
    text='',
    bg=CARD,
    fg=TEXT,
    font=('Consolas', 12),
    wraplength=520,
    justify='left'
)
la5.pack(anchor='w', pady=5)

root.mainloop()