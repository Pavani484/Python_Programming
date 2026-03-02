import tkinter as tk
root = tk.Tk()
root.title("Frame")
root.geometry("400x500")
frame = tk.Frame(root, bg="blue", width=300, height=200)
frame.pack(pady=20)
label = tk.Label(frame, text="Hello, Pavani!", bg="pink")
label.pack(padx=20, pady=20)
root.mainloop()



















