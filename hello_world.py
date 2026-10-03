import tkinter as tk

# 1. Create the main application window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# 2. Define an action for the button
def on_click():
    label.config(text="Button Clicked!")

# 3. Create and position a text label widget
label = tk.Tkinter = tk.Label(root, text="Hello, World!", font=("Arial", 14))
label.pack(pady=20)

# 4. Create and position a button widget
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# 5. Start the application event loop
root.mainloop()
