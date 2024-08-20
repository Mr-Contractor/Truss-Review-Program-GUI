# Importing all relavent libraries

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

# -----------------------------------------------------------------------------------------------------------


def upload_truss_drawing():
    return

def run_analysis():
    return


# -----------------------------------------------------------------------------------------------------------

# Creating root box

root = tk.Tk()
root.title("Truss Review Assistant - MiTek")
root.geometry("650x950")
root.resizable(False, False)

# -----------------------------------------------------------------------------------------------------------

# Creating a main frame to hold everything

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# -----------------------------------------------------------------------------------------------------------

# Title

title_label = ttk.Label(main_frame, text = "Truss Review Assistant - MiTek", font=("Helvetica", 16))
title_label.pack(anchor = 'w')

# -----------------------------------------------------------------------------------------------------------

# File upload section

upload_frame = ttk.LabelFrame(main_frame,text="1. Upload shop drawing",padding = '15')
upload_frame.pack(fill=tk.X, pady = 15)

upload_button = ttk.Button(upload_frame, text="Load file", command=upload_truss_drawing)
upload_button.pack(side=tk.LEFT)

loading_label = ttk.Label(upload_frame, text="Loading status (%)")
loading_label.pack(side=tk.LEFT, padx=10)

loading_status = ttk.Progressbar(upload_frame, orient=tk.HORIZONTAL, length=200, mode='determinate') 
loading_status.pack(side=tk.LEFT)

# -----------------------------------------------------------------------------------------------------------

# Load input section

load_data_frame = ttk.LabelFrame(main_frame, text = "2. Loading Data", padding = "15")
load_data_frame.pack(fill=tk.X, pady=15)

# Roof dead load entry

ttk.Label(load_data_frame, text="Design roof dead load:").grid(row=0, column=0, sticky=tk.W)
roof_dead_load_entry = ttk.Entry(load_data_frame)
roof_dead_load_entry.grid(row=0, column=1, padx=20)
roof_dead_load_entry.insert(0,"21")
ttk.Label(load_data_frame, text="psf").grid(row=0, column=2, sticky=tk.W)

# Roof live load entry slope >= 4/12

ttk.Label(load_data_frame, text="Design roof live load (slope >= 4/12):").grid(row=1, column=0, sticky=tk.W)
roof_live_load1_entry = ttk.Entry(load_data_frame)
roof_live_load1_entry.grid(row=1, column=1, padx=20)
roof_live_load1_entry.insert(0,"16")
ttk.Label(load_data_frame, text="psf").grid(row=1, column=2, sticky=tk.W)

# Roof live load entry slope < 4/12

ttk.Label(load_data_frame, text="Design roof live load (slope < 4/12):").grid(row=2, column=0, sticky=tk.W)
roof_live_load2_entry = ttk.Entry(load_data_frame)
roof_live_load2_entry.grid(row=2, column=1, padx=20)
roof_live_load2_entry.insert(0,"20")
ttk.Label(load_data_frame, text="psf").grid(row=2, column=2, sticky=tk.W)

# Floor dead load entry

ttk.Label(load_data_frame, text="Design floor dead load:").grid(row=3, column=0, sticky=tk.W)
floor_dead_load_entry = ttk.Entry(load_data_frame)
floor_dead_load_entry.grid(row=3, column=1, padx=20)
floor_dead_load_entry.insert(0,"18")
ttk.Label(load_data_frame, text="psf").grid(row=3, column=2, sticky=tk.W)

# Floor live load entry

ttk.Label(load_data_frame, text="Design floor live load:").grid(row=4, column=0, sticky=tk.W)
floor_live_load_entry = ttk.Entry(load_data_frame)
floor_live_load_entry.grid(row=4, column=1, padx=20)
floor_live_load_entry.insert(0,"40")
ttk.Label(load_data_frame, text="psf").grid(row=4, column=2, sticky=tk.W)

# Truss spacing entry

ttk.Label(load_data_frame, text="Truss spacing:").grid(row=5, column=0, sticky=tk.W)
truss_spacing_entry = ttk.Entry(load_data_frame)
truss_spacing_entry.grid(row=5, column=1, padx=20)
truss_spacing_entry.insert(0,"24")
ttk.Label(load_data_frame, text="inches").grid(row=5, column=2, sticky=tk.W)

# -----------------------------------------------------------------------------------------------------------

# Deflection input section

deflection_data_frame = ttk.LabelFrame(main_frame, text = "3. Deflection Data", padding = "15")
deflection_data_frame.pack(fill=tk.X, pady=15)

deflection_options = ["L/240","L/360","L/480"]

# Roof live load deflection limit

ttk.Label(deflection_data_frame, text="Roof live load deflection limit:").grid(row=0, column=0, sticky=tk.W)
roof_live_deflection = ttk.Combobox(deflection_data_frame, values = deflection_options, state = 'readonly')
roof_live_deflection.current(1)
roof_live_deflection.grid(row=0, column=1, padx=55)

# Roof total load deflection limit

ttk.Label(deflection_data_frame, text="Roof total load deflection limit:").grid(row=1, column=0, sticky=tk.W)
roof_total_deflection = ttk.Combobox(deflection_data_frame, values = deflection_options, state = 'readonly')
roof_total_deflection.current(0)
roof_total_deflection.grid(row=1, column=1, padx=55)

# Floor live load deflection limit

ttk.Label(deflection_data_frame, text="Floor live load deflection limit:").grid(row=2, column=0, sticky=tk.W)
floor_live_deflection = ttk.Combobox(deflection_data_frame, values = deflection_options, state = 'readonly')
floor_live_deflection.current(2)
floor_live_deflection.grid(row=2, column=1, padx=55)

# Floor total load deflection limit

ttk.Label(deflection_data_frame, text="Floor total load deflection limit:").grid(row=3, column=0, sticky=tk.W)
floor_total_deflection = ttk.Combobox(deflection_data_frame, values = deflection_options, state = 'readonly')
floor_total_deflection.current(1)
floor_total_deflection.grid(row=3, column=1, padx=55)

# -----------------------------------------------------------------------------------------------------------

# Design code input section

design_code_data_frame = ttk.LabelFrame(main_frame, text = "4. Design code criteria", padding = "15")
design_code_data_frame.pack(fill=tk.X, pady=15)

design_building_code_options = ["IBC 2021","IBC 2018","IBC 2015","IBC 2012","IBC 2009","IBC 2006",
                                "IRC 2021","IRC 2018","IRC 2015","IRC 2012","IRC 2009","IRC 2006"]

design_wind_code_options = ["ASCE 7-22","ASCE 7-16","ASCE 7-10","ASCE 7-05","ASCE 7-02"]

risk_category_options = ["I","II","III","VI"]

# Design building code

ttk.Label(design_code_data_frame, text="Design building code:").grid(row=0, column=0, sticky=tk.W)
design_building_code = ttk.Combobox(design_code_data_frame, values = design_building_code_options, state = 'readonly')
design_building_code.current(0)
design_building_code.grid(row=0, column=1, padx=105)

# Design wind standard

ttk.Label(design_code_data_frame, text="Design wind standard:").grid(row=1, column=0, sticky=tk.W)
design_wind_standard = ttk.Combobox(design_code_data_frame, values = design_wind_code_options, state = 'readonly')
design_wind_standard.current(0)
design_wind_standard.grid(row=1, column=1, padx=105)

# Risk Category

ttk.Label(design_code_data_frame, text="Risk Category:").grid(row=2, column=0, sticky=tk.W)
risk_category = ttk.Combobox(design_code_data_frame, values = risk_category_options, state = 'readonly')
risk_category.current(1)
risk_category.grid(row=2, column=1, padx=105)

# Design wind speed

ttk.Label(design_code_data_frame, text="Design wind speed:").grid(row=3, column=0, sticky=tk.W)
design_wind_speed = ttk.Entry(design_code_data_frame)
design_wind_speed.grid(row=3, column=1)
ttk.Label(design_code_data_frame, text="mph").grid(row=3, column=2, sticky=tk.W)

# -----------------------------------------------------------------------------------------------------------

# Buttons and status
button_frame = ttk.LabelFrame(main_frame, text = "5. Run file", padding = '15')
button_frame.pack(fill=tk.X, pady=15)

run_button = ttk.Button(button_frame, text="Run", command = run_analysis)
run_button.pack(side=tk.LEFT)

status_bar = ttk.Label(button_frame, text="Run status (%)") 
status_bar.pack(side=tk.LEFT, padx=10)

run_status = ttk.Progressbar(button_frame, orient=tk.HORIZONTAL, length=200, mode='determinate') 
run_status.pack(side=tk.LEFT)

# -----------------------------------------------------------------------------------------------------------

# Disclaimer

disclaimer = "The Truss Review Assistant is intended as a supplementary tool to aid in cursory reviews of truss shop drawings. The reviewer shall conduct a comprehensive and independent examination of all shop drawings. The application and its results do not guarantee the accuracy or completeness of the output, and users should exercise their own judgment in interpreting the results."

disclaimer_frame = ttk.LabelFrame(main_frame,text="Disclaimer",padding = '15')
disclaimer_frame.pack(fill=tk.X, pady = 15)

disclaimer_label = ttk.Label(disclaimer_frame, text=disclaimer, font=("Helvetica", 7), relief=tk.FLAT, borderwidth=0, wraplength=550)  # Adjust wraplength as needed
disclaimer_label.pack()

# -----------------------------------------------------------------------------------------------------------

# Close button

close_button = ttk.Button(main_frame, text="Close", command=root.destroy)
close_button.pack(side=tk.RIGHT, anchor=tk.SE)

root.mainloop()