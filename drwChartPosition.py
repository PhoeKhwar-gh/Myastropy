import tkinter as tk
from tkinter import ttk
import math

class BurmeseGrid:
    def __init__(self, parent, width=600, height=600, bg="white"):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.cell_size = (min(width, height) // 10)  # Adjusted for better visibility
        self.points = []  # Store clicked points and their info

    def draw_grid(self, label_text="ရာသီ"):
        c_x, c_y = self.center_x, self.center_y 
        cell = self.cell_size

        # Clear previous drawings
        self.canvas.delete("all")
        
        # Draw the outer square
        self.canvas.create_rectangle(c_x - 5*cell, c_y - 5*cell, 
                                    c_x + 5*cell, c_y + 5*cell, 
                                    outline="black", width=2)
        
        # Draw the inner square (rotated 45 degrees)
        points = [
            c_x, c_y - 5*cell,  # top
            c_x + 5*cell, c_y,   # right
            c_x, c_y + 5*cell,   # bottom
            c_x - 5*cell, c_y    # left
        ]
        self.canvas.create_polygon(points, outline="black", width=2, fill="")
        
        # Draw diagonal lines
        self.canvas.create_line(c_x - 5*cell, c_y - 5*cell, c_x - cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x + 5*cell, c_y - 5*cell, c_x + cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x - cell, c_y + cell, c_x - 5*cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x + cell, c_y + cell, c_x + 5*cell, c_y + 5*cell, fill="black", width=1)
        
        # Draw vertical and horizontal lines
        self.canvas.create_line(c_x - cell, c_y - 5*cell, c_x - cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x + cell, c_y - 5*cell, c_x + cell, c_y + 5*cell, fill="black", width=1)
        self.canvas.create_line(c_x - 5*cell, c_y - cell, c_x + 5*cell, c_y - cell, fill="black", width=1)
        self.canvas.create_line(c_x - 5*cell, c_y + cell, c_x + 5*cell, c_y + cell, fill="black", width=1)
        
        # Draw center circle and label
        self.canvas.create_oval(c_x - 20, c_y - 20, c_x + 20, c_y + 20, outline="black", width=2)
        self.canvas.create_text(c_x, c_y, text=label_text, font=("Myanmar Text", 14, "bold"), fill="black")
        
        # Draw zodiac signs at the corners
        zodiac_signs = ["မိဿ", "ပြိဿ", "မေထုန်", "ကရကဋ်", "သိဟ်", "ကန်", "တူ", "ဗြိစ္ဆာ", "ဓနု", "မကာရ", "ကုမ်", "မိန်"]
        positions = [
            (c_x - 4.5*cell, c_y - 4.5*cell),  # Top-left
            (c_x, c_y - 5.2*cell),             # Top
            (c_x + 4.5*cell, c_y - 4.5*cell),  # Top-right
            (c_x + 5.2*cell, c_y),             # Right
            (c_x + 4.5*cell, c_y + 4.5*cell),  # Bottom-right
            (c_x, c_y + 5.2*cell),             # Bottom
            (c_x - 4.5*cell, c_y + 4.5*cell),  # Bottom-left
            (c_x - 5.2*cell, c_y),             # Left
            (c_x - 3.5*cell, c_y - 3.5*cell),  # Inner top-left
            (c_x + 3.5*cell, c_y - 3.5*cell),  # Inner top-right
            (c_x + 3.5*cell, c_y + 3.5*cell),  # Inner bottom-right
            (c_x - 3.5*cell, c_y + 3.5*cell)   # Inner bottom-left
        ]
        
        for i, (x, y) in enumerate(positions):
            self.canvas.create_text(x, y, text=zodiac_signs[i], font=("Myanmar Text", 10), fill="black")
        
        return self
    
    def place_planet(self, planet_name, zodiac_sign, degrees, minutes):
        # Map zodiac signs to positions on the grid
        zodiac_positions = {
            "Aries": (0, 0),         # မိဿ
            "Taurus": (1, 0),        # ပြိဿ
            "Gemini": (2, 0),        # မြင်း
            "Cancer": (3, 0),        # ကုဋ်
            "Leo": (0, 1),           # သိဟ်
            "Virgo": (1, 1),         # ကန်
            "Libra": (2, 1),         # တူ
            "Scorpio": (3, 1),       # ဗြိစ္ဆာ
            "Sagittarius": (0, 2),   # ဓနု
            "Capricorn": (1, 2),    # မကာရ
            "Aquarius": (2, 2),     # ကုံ
            "Pisces": (3, 2)        # မိန်
        }
        
        # Map Burmese zodiac names to English
        zodiac_mapping = {
            "မိဿ": "Aries",
            "ပြိဿ": "Taurus",
            "မြင်း": "Gemini",
            "ကုဋ်": "Cancer",
            "သိဟ်": "Leo",
            "ကန်": "Virgo",
            "တူ": "Libra",
            "ဗြိစ္ဆာ": "Scorpio",
            "ဓနု": "Sagittarius",
            "မကာရ": "Capricorn",
            "ကုံ": "Aquarius",
            "မိန်": "Pisces"
        }
        
        # If zodiac_sign is in Burmese, convert to English
        if zodiac_sign in zodiac_mapping:
            zodiac_sign = zodiac_mapping[zodiac_sign]
        
        if zodiac_sign not in zodiac_positions:
            return
        
        # Get the position in the grid
        pos_x, pos_y = zodiac_positions[zodiac_sign]
        
        # Calculate the exact position based on degrees (0-30 in each sign)
        total_degrees = degrees + minutes/60.0
        fraction = total_degrees / 30.0  # Each sign is 30 degrees
        
        # Calculate coordinates
        c_x, c_y = self.center_x, self.center_y
        cell = self.cell_size
        
        # Different calculation based on which quadrant the sign is in
        if pos_x == 0:  # Left side
            x = c_x - 4.5*cell + (fraction * 3*cell) if pos_y == 0 else \
                c_x - 3.5*cell - (fraction * 3*cell) if pos_y == 2 else \
                c_x - 5*cell
        elif pos_x == 1:  # Middle
            x = c_x - cell + (fraction * 2*cell) if pos_y == 0 else \
                c_x + cell - (fraction * 2*cell) if pos_y == 2 else \
                c_x
        else:  # Right side
            x = c_x + 4.5*cell - (fraction * 3*cell) if pos_y == 0 else \
                c_x + 3.5*cell + (fraction * 3*cell) if pos_y == 2 else \
                c_x + 5*cell
        
        if pos_y == 0:  # Top row
            y = c_y - 5*cell
        elif pos_y == 1:  # Middle row
            y = c_y - cell + (fraction * 2*cell) if pos_x == 0 else \
                c_y + cell - (fraction * 2*cell) if pos_x == 3 else \
                c_y
        else:  # Bottom row
            y = c_y + 5*cell
        
        # Draw the planet
        planet_color = {
            "Sun": "red",
            "Moon": "lightblue",
            "Mars": "red",
            "Mercury": "green",
            "Jupiter": "orange",
            "Venus": "yellow",
            "Saturn": "brown",
            "Uranus": "blue",
            "Neptune": "purple",
            "Pluto": "black"
        }.get(planet_name, "gray")
        
        # Draw the planet symbol
        radius = 10
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, 
                               fill=planet_color, outline="black")
        
        # Add planet name
        self.canvas.create_text(x, y+15, text=planet_name, font=("Arial", 8), fill="black")
        
        # Store the point information
        self.points.append((planet_name, x, y, zodiac_sign, degrees, minutes))
        
        return self

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("မြန်မာဗေဒင် ဂြိုဟ်တည်နေရာ")
    
    grid = BurmeseGrid(root, width=700, height=700)
    grid.canvas.pack(pady=10)
    grid.draw_grid()
    
    # Add planets based on the provided data
    planets_data = [
        ("၁", "Leo", 29, 21),
        ("၂", "Leo", 16, 22),
        ("၃", "Libra", 9, 35),
        ("၄", "Leo", 11, 10),
        ("၅", "Cancer", 16, 2),
        ("၆", "Cancer", 25, 50),
        ("၇", "Aries", 0, 39),
        ("U", "Gemini", 1, 22),
        ("N", "Aries", 1, 35),
        ("P", "Aquarius", 1, 57)
    ]
    
    for planet, sign, deg, min in planets_data:
        grid.place_planet(planet, sign, deg, min)
    
    root.mainloop()