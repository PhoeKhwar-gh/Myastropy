import tkinter as tk

class BurmeseGrid:
    def __init__(self, root, width=300, height=300):
        self.root = root
        self.width = width
        self.height = height
        self.cell_size = (min(width, height) // 5) - 10

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.position_label = tk.Label(root, text="Mouse Grid Position: (x, y)", font=("Myanmar Text", 10))
        self.position_label.pack()

        self.canvas.bind("<Motion>", self.update_mouse_position)

        self.draw_grid()
        self.draw_axes()

    def draw_grid(self):
        cx = self.width // 2
        cy = self.height // 2

        self.canvas.create_rectangle(
            cx - 2 * self.cell_size, cy - 2 * self.cell_size,
            cx + 2 * self.cell_size, cy + 2 * self.cell_size,
            outline="black", width=2
        )

        for i in range(-2, 3):
            x = cx + i * self.cell_size
            self.canvas.create_line(x, cy - 2 * self.cell_size, x, cy + 2 * self.cell_size, fill="gray")

        for j in range(-2, 3):
            y = cy + j * self.cell_size
            self.canvas.create_line(cx - 2 * self.cell_size, y, cx + 2 * self.cell_size, y, fill="gray")

    def draw_axes(self):
        cx = self.width // 2
        cy = self.height // 2

        for i in range(1, 5):
            x = cx + i * self.cell_size
            self.canvas.create_line(x, cy - 5, x, cy + 5, fill="blue")
            self.canvas.create_text(x, cy + 15, text=str(i), font=("Myanmar Text", 10), fill="blue")

        for j in range(1, 5):
            y = cy + j * self.cell_size
            self.canvas.create_line(cx - 5, y, cx + 5, y, fill="red")
            self.canvas.create_text(cx - 15, y, text=f"-{j}", font=("Myanmar Text", 10), fill="red")

        self.canvas.create_line(cx - 10, cy, cx + 10, cy, fill="black")
        self.canvas.create_line(cx, cy - 10, cx, cy + 10, fill="black")
        self.canvas.create_text(cx + 5, cy - 15, text="(0,0)", font=("Myanmar Text", 10), fill="black")

    def update_mouse_position(self, event):
        cx = self.width // 2
        cy = self.height // 2

        grid_x = (event.x - cx) // self.cell_size
        grid_y = -(event.y - cy) // self.cell_size  # Invert Y to match Cartesian

        self.position_label.config(text=f"Mouse Grid Position: ({grid_x}, {grid_y})")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Myanmar Astrology Grid with Grid Coordinates")
    BurmeseGrid(root)
    root.mainloop()