# Author: Alexander Jones
# Class: CS361-400 Summer '22
# Version: 0.1.0

# Description: gui.py renders the visual components of the time-series
# visualization tool. Data is passed to the matplot
from tkinter import messagebox
from tkinter.tix import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import math



# def plot():
#
#     # figure contianing the plot
#     fig = plt.Figure(figsize=(5,5,), dpi=100)
#     # Create TESTING y values, using sine function
#     y = [math.sin(i) for i in range(101)]
#     # Add the subplot
#     plot1 = fig.add_subplot(111)
#     plot1.plot(y)
#     # Create Tkinter canvas containing Matplotlib figure
#     canvas = FigureCanvasTkAgg(fig, master=root)


# Heuristic #1 (of 8): Explain the benefits of using new and existing features
#                       - For the time being this is covered in the help window.
def csh1():
    tk.messagebox.showinfo("New feature: Select different statistical views to see different views of your data.")


# Heuristic #2 (of 8): Explain the costs of using new and existing features
#                       - Window pop up with alert on click
def csh2_radiobtn():
    tk.messagebox.showinfo("Choosing different statistical views may make plots different than you expect. If you are "
                          "unfamiliar with these views, please see the documentation: ImaginaryWebsite.link")
    
def csh2_default():
    tk.messagebox.showinfo("This is the default view.")

# Heuristic #3 (of 8): Let people gather as much information as they want, and no more than they want
#                      - The interface and design of the application is made so that users can explore freely. Tooltips
#                           reveal more information on hover, and windows appear when creating different views.
# Heuristic #4 (of 8): Keep familiar features available
#                      - Resizing and typical application features will be present.
# Heuristic #6 (of 8): Provide an explicit path through the task
#                      - Described in the help window
def csh6_help_window():
    tk.messagebox.showinfo("Normal Operation: \n1. Click the choose file button\n2. Select a file in your file explorer"
                           "\n3. After selecting, hit upload.\n 4. Your blood glucose data should now be displayed in"
                           "the plots.\n\nNew features! Now use the new statistical views for blood glucose data over"
                           "time. The views, median, variance, and standard deviation, will allow you to look at your "
                           "data in new and different ways!")
# Heuristic #7 (of 8): Provide ways to try out different approaches
# This is accomplished by having all of the options available to the user at face value.
# Heuristic #8 (of 8): Encourage tinkerers to tinker mindfully
# Again, This is accomplished by having all of the options available to the user at face value.

# ------------------ This is ALL GUI stuff --------------------------------------
# Color constants
bg_color = "#f6f2ff"
text_color = "#491d8b"
frame_color = "#e8daff"


root = tk.Tk()
# CSH4 Keep familiar features available
# Currently not working, revision?
root.resizable(height=None, width=None)

# root.geometry('500x500') # Fixed window size? or make dynamically scalable?
content = tk.Frame(root, background=bg_color)
frame = tk.Frame(content, borderwidth=5, relief="ridge")

# Radio Button Nested Frame

data_display_type = tk.StringVar()
# Average buttons
average1 = tk.Radiobutton(content, text="Average", variable=data_display_type, value='average')
average2 = tk.Radiobutton(content, text="Average", variable=data_display_type, value='average')
average3 = tk.Radiobutton(content, text="Average", variable=data_display_type, value='average')
average4 = tk.Radiobutton(content, text="Average", variable=data_display_type, value='average')


# Median buttons
median1 = tk.Radiobutton(content, text="Median", variable=data_display_type, value='median', command=lambda: csh2_radiobtn())
median2 = tk.Radiobutton(content, text="Median", variable=data_display_type, value='median', command=lambda: csh2_radiobtn())
median3 = tk.Radiobutton(content, text="Median", variable=data_display_type, value='median', command=lambda: csh2_radiobtn())
median4 = tk.Radiobutton(content, text="Median", variable=data_display_type, value='median', command=lambda: csh2_radiobtn())
# Variance Buttons
variance1 = tk.Radiobutton(content, text="Variance", variable=data_display_type, value='variance', command=lambda: csh2_radiobtn())
variance2 = tk.Radiobutton(content, text="Variance", variable=data_display_type, value='variance', command=lambda: csh2_radiobtn())
variance3 = tk.Radiobutton(content, text="Variance", variable=data_display_type, value='variance', command=lambda: csh2_radiobtn())
variance4 = tk.Radiobutton(content, text="Variance", variable=data_display_type, value='variance', command=lambda: csh2_radiobtn())
# Std Dev Buttons
std_dev1 = tk.Radiobutton(content, text="Standard Deviation", variable=data_display_type, value='stddev', command=lambda: csh2_radiobtn())
std_dev2 = tk.Radiobutton(content, text="Standard Deviation", variable=data_display_type, value='stddev', command=lambda: csh2_radiobtn())
std_dev3 = tk.Radiobutton(content, text="Standard Deviation", variable=data_display_type, value='stddev', command=lambda: csh2_radiobtn())
std_dev4 = tk.Radiobutton(content, text="Standard Deviation", variable=data_display_type, value='stddev', command=lambda: csh2_radiobtn())

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
# Help button
help_btn = tk.Button(content, text="Help!", command=lambda: csh6_help_window())

# Slider
time_window = tk.Scale(from_=0, to=90, orient="horizontal")



# Cognitive Style Heuristics Compliance
vis_csh1 = tk.Label(content, text="First Plot CSH")
vis_csh2 = tk.Label(content, text="Second Plot CSH")
drop1_csh = tk.Label(content, text="Dropdown1 CSH")
drop2_csh = tk.Label(content, text="Dropdown2 CSH")
drop3_csh = tk.Label(content, text="Dropdown3 CSH")
drop4_csh = tk.Label(content, text="Dropdown4 csh")
#       1               2                   3              4
# ---------------------------------------------------------------|
# 1 date_label    | date_label_var  |               | upload_btn   |
# ---------------------------------------------------------------|
# 2 vis_title1    | vis_csh1       | drop1_csh     | drop2_csh     |
# ---------------------------------------------------------------|
# 3 vis_plot1     | vis_plot1      | radio_btn1    |radio_btn2     |
# ---------------------------------------------------------------|
# 4 vis_plot1     | vis_plot1      | radio_btn2    |radio_btn2     |
# ---------------------------------------------------------------|
# 5 vis_plot1     | vis_plot1      | radio_btn3    |radio_btn2     |
# ---------------------------------------------------------------|
# 6 vis_plot1     | vis_plot1      | radio_btn4    |radio_btn2     |
# ---------------------------------------------------------------|
# 7 vis_title2    | vis_csh2       | drop1_csh     | drop2_csh     |
# ---------------------------------------------------------------|
# 8 vis_plot2     | vis_plot2      | radio_btn1    |radio_btn2     |
# ---------------------------------------------------------------|
# 9 vis_plot2     | vis_plot2      | radio_btn2    |radio_btn2     |
# ---------------------------------------------------------------|
# 10 vis_plot2     | vis_plot2      | radio_btn3    |radio_btn2     |
# ---------------------------------------------------------------|
# 11 vis_plot2     | vis_plot2      | radio_btn4    |radio_btn2     |
# ---------------------------------------------------------------|
# 12 slider         | slider        | undo_btn      | redo_btn      |
# ---------------------------------------------------------------|

# Row 1
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=11)
date_label.grid(column=0, row=0)
date_label_var.grid(column=1, row=0)
upload_btn.grid(column=2, row=0)
help_btn.grid(column=3, row=0)

# Row 2
vis_title1.grid(column=0, row=1)
vis_csh1.grid(column=1, row=1)
drop1_csh.grid(column=2, row=1)
drop2_csh.grid(column=3, row=1)

# Row 3
# plot1.grid(column=0, row=2, columnspan=2, rowspan=4)
average1.grid(column=2, row=2)
average2.grid(column=3, row=2)


# Row 4
median1.grid(column=2, row=3)
median2.grid(column=3, row=3)

# Row 5
variance1.grid(column=2, row=4)
variance2.grid(column=3, row=4)

# Row 6
std_dev1.grid(column=2, row=5)
std_dev2.grid(column=3, row=5)
# plot2.grid(column=0, row=3, columnspan=2, rowspan=4)


# Row 7
vis_title2.grid(column=0, row=6)
vis_csh2.grid(column=1, row=6)
drop3_csh.grid(column=2, row=6)
drop4_csh.grid(column=3, row=6)

# Row 8
# plot2.grid(column=0, row=7, columnspan=2, rowspan=4)
average3.grid(column=2, row=7)
average4.grid(column=3, row=7)

# Row 9
median3.grid(column=2, row=8)
median4.grid(column=3, row=8)

# Row 10
variance3.grid(column=2, row=9)
variance4.grid(column=3, row=9)

# Row 11
std_dev3.grid(column=2, row=10)
std_dev4.grid(column=3, row=10)

# Row 12
time_window.grid(column=0, row=11, columnspan=2)
undo_btn.grid(column=2, row=11)
redo_btn.grid(column=3, row=11)
# Main loop to begin looking for event listeners
root.mainloop()