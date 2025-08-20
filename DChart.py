import tkinter as tk
from tkinter import ttk

class BurmeseGrid:
    def __init__(self, parent, width=300, height=300, bg="lightgray"):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.cell_size = (min(width, height) // 5 )-10

    def draw_grid(self, label_text="မြန်မာ"):
        c_x, c_y = self.center_x, self.center_y 
        cell = self.cell_size

        # Vertical lines
        self.canvas.create_line(c_x  - cell, c_y - (5*cell), c_x - cell, c_y + (5*cell), fill="black", width=1)
        self.canvas.create_line(c_x + cell, c_y - 5*cell, c_x + cell, c_y + 5*cell, fill="black", width=1)

        # Horizontal lines
        self.canvas.create_line(c_x - 5*cell, c_y - cell, c_x + 5*cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x - 5*cell, c_y + cell, c_x + 5*cell, c_y + cell, fill="black", width=1)

        # Diagonal lines
        self.canvas.create_line(c_x - 5*cell, c_y - 5*cell, c_x - cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x + 5*cell, c_y - 5*cell, c_x + cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x - cell, c_y + cell, c_x - 5*cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x + cell, c_y + cell, c_x + 5*cell, c_y + 5*cell, fill="black", width=1)

        # Center label
        self.canvas.create_text(c_x, c_y, text=label_text, font=("Myanmar Text", 14, "bold"), fill="black")

        return self

    def pack(self, **kwargs):
        self.canvas.pack(**kwargs)
        return self

    def grid(self, **kwargs):
        self.canvas.grid(**kwargs)
        return self

    def place(self, **kwargs):
        self.canvas.place(**kwargs)
        return self

    def get_canvas(self):
        return self.canvas


class GridApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Burmese Grid Components")
        self.root.geometry("1000x800")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Burmese Grid Components - ActiveX Style", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Create frame for grids
        grid_container = ttk.Frame(main_frame)
        grid_container.pack(fill=tk.BOTH, expand=True)
        
        # Create three grid instances with different labels
        self.grid1 = BurmeseGrid(grid_container, width=250, height=250)
        self.grid2 = BurmeseGrid(grid_container, width=250, height=250)
        self.grid3 = BurmeseGrid(grid_container, width=250, height=250)
        
        # Draw grids with specific labels
        self.grid1.draw_grid("ရာသီ").grid(row=0, column=0, padx=20, pady=10)
        self.grid2.draw_grid("ဘာဝ").grid(row=0, column=1, padx=20, pady=10)
        self.grid3.draw_grid("နဝင်း").grid(row=0, column=2, padx=20, pady=10)
        
        # Add labels below each grid
        ttk.Label(grid_container, text="Grid 1 - ရာသီ", font=("Myanmar Text", 12)).grid(row=1, column=0)
        ttk.Label(grid_container, text="Grid 2 - ဘာဝ", font=("Myanmar Text", 12)).grid(row=1, column=1)
        ttk.Label(grid_container, text="Grid 3 - နဝင်း", font=("Myanmar Text", 12)).grid(row=1, column=2)
        
        # Add usage instructions
        instruction_text = """
如何使用这些组件:
1. 创建实例: grid = BurmeseGrid(parent_frame)
2. 绘制网格: grid.draw_grid("标签文本")
3. 布局: grid.pack() 或 grid.grid() 或 grid.place()
4. 获取画布: canvas = grid.get_canvas()
"""
        instruction_label = ttk.Label(main_frame, text=instruction_text, 
                                    justify=tk.LEFT, font=("Arial", 10))
        instruction_label.pack(pady=20)


# 使用示例 1: 单独使用组件
def create_single_grid():
    window = tk.Toplevel()
    window.title("ဘယ်နေရာပေါ်တာလည်း")
    window.geometry("400x400")
    
    grid = BurmeseGrid(window, width=300, height=300)
    grid.draw_grid("တစ်ခုတည်း").pack(pady=50)


# 使用示例 2: 动态创建多个组件
def create_multiple_grids():
    window = tk.Toplevel()
    window.title("အေင်ဘာလေ")
    window.geometry("800x300")
    
    container = ttk.Frame(window)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    labels = ["ပထမ", "ဒုတိယ", "တတိယ", "စတုတ္ထ"]
    
    for i, label in enumerate(labels):
        grid = BurmeseGrid(container, width=150, height=150)
        grid.draw_grid(label).grid(row=0, column=i, padx=10)
        ttk.Label(container, text=f"Grid {i+1}").grid(row=1, column=i)


if __name__ == "__main__":
    root = tk.Tk()
    app = GridApplication(root)
    
    # 添加一些控制按钮来演示组件的可重用性
    control_frame = ttk.Frame(root)
    control_frame.pack(pady=10)
    
    ttk.Button(control_frame, text="单独网格示例", command=create_single_grid).pack(side=tk.LEFT, padx=5)
    ttk.Button(control_frame, text="多个网格示例", command=create_multiple_grids).pack(side=tk.LEFT, padx=5)
    
    


  
    root.mainloop()