# သင့်ရဲ့ Python ဖိုင်ထဲမှာ
import tkinter as tk
from DChart import BurmeseGrid  # BurmeseGrid component ကို import လုပ်ပါ

# အသုံးပြုနည်း
root = tk.Tk()
grid = BurmeseGrid(root)
grid.draw_grid("ရာသီ").pack()
root.mainloop()