# Author:
# Class:
# Version:

# Description:

import tkinter as tk
import matplotlib.pyplot as plt


root = tk.Tk()

content = tk.Frame(root)
frame = tk.Frame(content, borderwidth=5, relief="ridge")

# Data upload
date_label = tk.Label(content, text="Viewing Data Date Range: ")
date_label_var = tk.Label(content, text="DD/MM/YY-DD/MM/YY")
upload_btn = tk.Button(content, text="Choose file")

# Visualization decoration
vis_title1 = tk.Label(content, text="First Plot Title")
vis_title2 = tk.Label(content, text="Second Plot Title")

# Undo/Redo buttons
undo_btn = tk.Button(content, text="Undo")
redo_btn = tk.Button(content, text="Redo")

# Radio Button Nested Frame


# Cognitive Style Heuristics Compliance
vis_csh1 = tk.Label(content, text="First Plot CSH")
vis_csh2 = tk.Label(content, text="Second Plot CSH")
drop1_csh = tk.Label(content, text="Dropdown1 CSH")
drop2_csh = tk.Label(content, text="Dropdown2 CSH")
drop3_csh = tk.Label(content, text="Dropdown3 CSH")
drop4_csh = tk.Label(content, text="Dropdown4 csh")

# ---------------------------------------------------------------|
# date_label    | date_label_var    |               | upload_btn |
# ---------------------------------------------------------------|
# vis_title1    | vis_csh1          | drop1_csh     | drop2_csh  |
# ---------------------------------------------------------------|
# vis_plot1     | vis_plot1         | dropdown1     | dropdown2  |
# ---------------------------------------------------------------|
# vis_title2    | vis_csh2          | drop3_csh     | drop4_csh  |
# ---------------------------------------------------------------|
# vis_plot2     | vis_plot2         | dropdown1     | dropdown2  |
# ---------------------------------------------------------------|
# slider         | slider            | undo_btn      | redo_btn  |
# ---------------------------------------------------------------|

# Row 1
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=4, rowspan=6)
date_label.grid(column=0, row=0)
date_label_var.grid(column=1, row=0)
upload_btn.grid(column=3, row=0, columnspan=2)
# Row 2
vis_title1.grid(column=0, row=1)
vis_csh1.grid(column=1, row=1)
drop1_csh.grid(column=2, row=1)
drop2_csh.grid(column=3, row=1)
# Row 3
# plot1.grid(column=0, row=2, columnspan=2)
# Nested radio button grid1.grid(column=2, row=2)
# Nested radio button grid2.grid(column=3, row =2)

# Row 4
# plot2.grid(column=0, row=3, columnspan=2)
# Nested radio button grid3.grid(column=2, row=3)
# Nested radio button grid4.grid(column=2, row=4)

# Row 5
# slider.grid(column=0, row=0, columnspan=2)
undo_btn.grid(column=2, row=3)
redo_btn.grid(column=3, row=3)
# Main loop to begin looking for event listeners
root.mainloop()