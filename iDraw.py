import tkinter as tk
from tkinter import ttk
import math
from DChart import BurmeseGrid  # BurmeseGrid component ကို import လုပ်ပါ

class ExampleApp:   
    def __init__(self, root):
        self.root = root
        self.root.title("BurmeseGrid Component Example")
        self.root.geometry("900x700")

        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        example1_frame = ttk.LabelFrame(main_frame, text="Example 1: Basic Usage", padding="10")
        example1_frame.pack(fill=tk.X, pady=10)

        grid1 = BurmeseGrid(example1_frame, width=250, height=250)
        grid1.draw_grid("ရာသီ").pack(pady=10)
    
      
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ExampleApp(root)
    root.mainloop()
