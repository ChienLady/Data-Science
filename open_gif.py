import tkinter as tk
from PIL import Image  

def update(ind):
    global root, label

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


file = Image.open('pigif.gif')
frameCnt = file.n_frames
root = tk.Tk()
frames = [tk.PhotoImage(file='pigif.gif', format = f'gif -index {i}') for i in range(frameCnt)]
label = tk.Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()