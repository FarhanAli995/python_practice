import tkinter as tk

r = tk.Tk()
r.title("pygwidgets example")
r.geometry("800x600")
r['bg']='light blue'

tk.Label(r,text="Default input text",bg='light blue').place(x=50,y=30)
tk.Entry(r,width=40).place(x=50,y=60)
tk.Label(r,text="DRAG\nME",bg="gray",width=10,height=5,relief="raised").place(x=350,y=60)
tk.Label(r,text="Here is some centered display text.\nLoop counter: 95",bg='light grey').place(x=200,y=150)
tk.Label(r,text="Here is some display text. Loop counter:95",bg='white').place(x=50,y=250)
tk.Button(r,text="Restart").place(x=150,y=280)

for data, x, var in [
    ([("Allow radio btns", 30), ("Low", 60), ("Med", 90), ("High", 120)], 550, tk.IntVar()),
    ([("Allow Radio Buttons", 170), ("Radio Text 1", 200), ("Radio Text 2", 230), ("Radio Text 3", 260)], 570, tk.IntVar())
]:
    var.set(0)
    for i, (t, y) in enumerate(data):
        (tk.Checkbutton if i == 0 else tk.Radiobutton)(
            r, text=t, bg='light grey', **({'variable': var, 'value': i} if i else {})
        ).place(x=(550 if i == 0 else x), y=y)

tk.Button(r,text="Show Status").place(x=550,y=300)
tk.Button(r,text="START").place(x=550,y=400)
tk.Label(r,text="Click then up/down to resize,\nleft/right to rotate",bg='light grey').place(x=50,y=480)
tk.Label(r,text="Click then type l, r, d, u, s, or Space",bg='light grey').place(x=550,y=480)

r.mainloop()                                