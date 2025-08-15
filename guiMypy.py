import tkinter as tk
from tkinter import ttk
import pandas as pd

# CSV ဖတ်ခြင်း
df = pd.read_csv('dataCSV.csv', encoding='utf-8')

# Data cleaning
df['TownName'] = df['TownName'].fillna('').str.strip()
df['SRName'] = df['SRName'].fillna('').str.strip()
df['Latitude'] = df['Latitude'].fillna('0.0').astype(str).str.strip()
df['Longitude'] = df['Longitude'].fillna('0.0').astype(str).str.strip()

# Valid rows only
df = df[(df['TownName'] != '') & (df['SRName'] != '')]

# Unique states
states = sorted(df['SRName'].unique().tolist())

# Town data dictionary
town_data = {
    row['TownName']: {
        'state': row['SRName'],
        'lat': row['Latitude'],
        'lon': row['Longitude']
    }
    for _, row in df.iterrows()
}

# GUI setup
root = tk.Tk()
root.title("Burmese Astrology City Selector")

# State ComboBox
state_label = ttk.Label(root, text="State:")
state_label.pack(pady=5)
state_combo = ttk.Combobox(root, values=states, state="readonly")
state_combo.pack(pady=5)

# Town ComboBox
town_label = ttk.Label(root, text="Town:")
town_label.pack(pady=5)
town_combo = ttk.Combobox(root, state="readonly")
town_combo.pack(pady=5)

# Latitude & Longitude Labels
lat_label = ttk.Label(root, text="Latitude: ")
lat_label.pack(pady=5)
lon_label = ttk.Label(root, text="Longitude: ")
lon_label.pack(pady=5)

# Function to update towns based on selected state
def update_towns(event):
    selected_state = state_combo.get()
    filtered_towns = df[df['SRName'] == selected_state]['TownName'].unique().tolist()
    town_combo['values'] = sorted(filtered_towns)
    town_combo.set('')
    lat_label.config(text="Latitude: ")
    lon_label.config(text="Longitude: ")

# Function to update lat/lon based on selected town
def update_lat_lon(event):
    selected_town = town_combo.get()
    if selected_town in town_data:
        lat = town_data[selected_town]['lat']
        lon = town_data[selected_town]['lon']
        lat_label.config(text=f"Latitude: {lat}")
        lon_label.config(text=f"Longitude: {lon}")
    else:
        lat_label.config(text="Latitude: ")
        lon_label.config(text="Longitude: ")

# Bind selections
state_combo.bind("<<ComboboxSelected>>", update_towns)
town_combo.bind("<<ComboboxSelected>>", update_lat_lon)

# Run GUI
root.mainloop()