import tkinter as tk

class BurmeseGrid:
    def __init__(self, parent, width=300, height=300, bg="lightgray"):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.cell_size = (min(width, height) // 5) - 10

        self.zodiac_names = [
            "မိဿ", "ပြိဿ", "မေထုန်", "ကရကဋ်", "သိဟ်", "ကန်",
            "တူ", "ဗြိစ္ဆာ", "ဓနု", "မကာရ", "ကုမ်", "မိန်"
        ]

        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_grid(self, label_text="ရာသီ"):
        c_x, c_y = self.center_x, self.center_y
        cell = self.cell_size

        # Grid lines
        self.canvas.create_line(c_x - cell, c_y - 5*cell, c_x - cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x + cell, c_y - 5*cell, c_x + cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x - 5*cell, c_y - cell, c_x + 5*cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x - 5*cell, c_y + cell, c_x + 5*cell, c_y + cell, fill="black", width=1)
        self.canvas.create_line(c_x - 5*cell, c_y - 5*cell, c_x - cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x + 5*cell, c_y - 5*cell, c_x + cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x - cell, c_y + cell, c_x - 5*cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x + cell, c_y + cell, c_x + 5*cell, c_y + 5*cell, fill="black", width=1)

        # Center label
        self.canvas.create_text(c_x, c_y, text=label_text, font=("Myanmar Text", 14, "bold"), fill="black")

        # Zodiac labels
        self.draw_zodiac_labels()

        return self

    def draw_zodiac_labels(self):
        c_x, c_y = self.center_x, self.center_y
        cell = self.cell_size

        positions = [
            (0, -2*cell),        # မိဿ
            (-2*cell, -2*cell),  # ပြိဿ
            (2*cell, -2*cell),   # မေထုန်
            (2*cell, 0),         # ကရကဋ်
            (2*cell, 2*cell),    # သိဟ်
            (0, 2*cell),         # ကန်
            (-2*cell, 2*cell),   # တူ
            (-2*cell, 0),        # ဗြိစ္ဆာ
            (-cell, -cell),      # ဓနု
            (cell, -cell),       # မကာရ
            (cell, cell),        # ကုမ်
            (-cell, cell)        # မိန်
        ]

        for name, (dx, dy) in zip(self.zodiac_names, positions):
            self.canvas.create_text(self.center_x + dx, self.center_y + dy, text=name, font=("Myanmar Text", 12), fill="darkgreen")

    def on_click(self, event):
        # Absolute click position
        x, y = event.x, event.y

        # Relative to center
        dx = x - self.center_x
        dy = y - self.center_y

        # Display dot and label
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="red", outline="")
        self.canvas.create_text(x + 10, y, text=f".({dx}, {dy})", font=("Myanmar Text", 10), fill="blue")
        self.canvas.create_text(10, 10, text=f"cell_size = {self.cell_size}", anchor="nw", font=("Myanmar Text", 10), fill="gray")

# 🖼️ Main UI Integration
def main():
    root = tk.Tk()
    root.title("မြန်မာဗေဒင် Grid Viewer")

    grid_frame = tk.Frame(root)
    grid_frame.pack(padx=10, pady=10)

    grid = BurmeseGrid(grid_frame)
    grid.draw_grid()
    grid.canvas.pack()

    root.mainloop()

if __name__ == "__main__":
    main()