import tkinter as tk

r = tk.Tk()
r.title("pygwidgets example")
r.geometry("800x600")
r['bg'] = 'lightgray'  

tk.Label(r, text="Default input text", bg='#1e1e2f', fg='white').place(x=50, y=30)
tk.Entry(r, width=40, bg='#f0f0f5', fg='black', insertbackground='black').place(x=50, y=60)
tk.Label(r, text="DRAG\nME", bg="darkgray", fg='white', width=10, height=5, relief="raised").place(x=350, y=60)
tk.Label(r, text="Here is some centered display text.\nShowing the number of Frames \nLoop counter: 95", fg='black').place(x=50, y=150)
tk.Label(r, text="Here is some display text. Loop counter:95", bg='#f8f8ff', fg='black').place(x=50, y=250)
tk.Button(r, text="Restart", bg='darkgray', fg='white', activebackground='lightgray').place(x=150, y=280)

for data, x, var in [
    ([("Allow radio btns", 30), ("Low", 60), ("Med", 90), ("High", 120)], 550, tk.IntVar()),
    ([("Allow Radio Buttons", 170), ("Radio Text 1", 200), ("Radio Text 2", 230), ("Radio Text 3", 260)], 570, tk.IntVar())
]:
    var.set(0)
    for i, (t, y) in enumerate(data):
        (tk.Checkbutton if i == 0 else tk.Radiobutton)(
            r, text=t, bg='#dcdcdc', fg='black', activebackground='#c0c0c0',
            **({'variable': var, 'value': i} if i else {})
        ).place(x=(550 if i == 0 else x), y=y)

tk.Button(r, text="Show Status", bg='darkgray', fg='white', activebackground='lightgray').place(x=550, y=300)
tk.Button(r, text="START", bg='darkgray', fg='lightgray', activebackground='#218838').place(x=550, y=400)
tk.Label(r, text="Click then up/down arrow to resize,\nleft/right arrow to rotate. \nh and v to flip horizontally/vertically", bg='#d3d3d3', fg='black').place(x=50, y=480)
tk.Label(r, text="Click then type l, r, d, u, s, or Space", bg='#d3d3d3', fg='black').place(x=550, y=480)

r.mainloop()