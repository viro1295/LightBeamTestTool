import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from function import *

lightbeam = ""
configure = ""
image = ""
hog_file = ""
log_file = ""


###GUI###
root = tk.Tk()
root.title("LightBeam test tool")
root.geometry("800x800")

selectfile_label = tk.Label(root, text="Select Files",font=("Arial", 11), anchor="w", fg="blue")
selectfile_label.grid(row=0, column=0)

lightbeam_button = tk.Button(root, text="LightBeam", command=lambda: choosefile_insertwidget(lightbeam, "Choose LightBeam version", lightbeam_label))
lightbeam_button.grid(row=1, column=0)
lightbeam_label = tk.Label(root, text=lightbeam)
lightbeam_label.grid(row=1, column=1)


configure_button = tk.Button(root, text="ConfigureFile", command=lambda: choosefile_insertwidget(configure, "Choose configure file", configure_label))
configure_button.grid(row=2, column=0)
configure_label = tk.Label(root, text=configure)
configure_label.grid(row=2, column=1)

image_button = tk.Button(root, text="ImageFolder", command=lambda: choosefile_insertwidget(image, "Choose image folder", image_label))
image_button.grid(row=3, column=0)
image_label = tk.Label(root, text=image)
image_label.grid(row=3, column=1)

hog_button = tk.Button(root, text="HogFile", command=lambda: choosefile_insertwidget(hog_file, "Choose Hog file", hog_label))
hog_button.grid(row=4, column=0)
hog_label = tk.Label(root, text=hog_file)
hog_label.grid(row=4, column=1)

setparameter_label = tk.Label(root, text="Setting Parameters",font=("Arial", 11), anchor="w", fg="blue")
setparameter_label.grid(row=5, column=0)

log_tick = tk.BooleanVar()
log_checkbutton = tk.Checkbutton(root, text="Enable Logging (Default: Disabled)", variable=log_tick, command=lambda: toggle_widgetstate(log_tick, log_inputbox, log_browsebutton))
log_checkbutton.grid(row=6, column=0)
log_inputbox = tk.Entry(root, state=tk.DISABLED)
log_inputbox.grid(row=6, column=1)
log_browsebutton = tk.Button(root, text="Browse", state=tk.DISABLED, command=lambda: choosefile_insertwidget(log_file, "Choose Log file", log_inputbox))
log_browsebutton.grid(row=6, column=2)

loglevel_label = tk.Label(root, text="Log Level (Default: 0)")
loglevel_label.grid(row=7, column=0)
loglevel_combobox = ttk.Combobox(root, values=["0", "1", "2", "3"])
loglevel_combobox.set("0")
loglevel_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, loglevel_combobox))
loglevel_combobox.grid(row=7, column=1)

heap_memory_label = tk.Label(root, text="Heap Memory (Default: 10000)")
heap_memory_label.grid(row=8, column=0)
heap_memory_combobox = ttk.Combobox(root, values=["10000","100000", "200000", "Other"])
heap_memory_combobox.set("10000")
heap_memory_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, heap_memory_combobox))
heap_memory_combobox.grid(row=8, column=1)

stack_memory_label = tk.Label(root, text="Stack Memory (Default: 11000)")
stack_memory_label.grid(row=9, column=0)
stack_memory_combobox = ttk.Combobox(root, values=["11000","20000", "50000", "Other"])
stack_memory_combobox.set("11000")
stack_memory_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, stack_memory_combobox))
stack_memory_combobox.grid(row=9, column=1)

iteration_label = tk.Label(root, text="Iteration (Default: 1)")
iteration_label.grid(row=10, column=0)
iteration_combobox = ttk.Combobox(root, values=["1","5", "10", "Other"])
iteration_combobox.set("1")
iteration_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, iteration_combobox))
iteration_combobox.grid(row=10, column=1)

disable_shortcuts_tick = tk.IntVar()
disable_shortcuts_button = tk.Checkbutton(root, text="Disable Shortcuts", variable=disable_shortcuts_tick, command=lambda: select_unselect(disable_shortcuts_tick, "Disable shortcuts is selected", "Disable shortcuts is not selected"))
disable_shortcuts_button.grid(row=11, column=0)

threads_number_label = tk.Label(root, text="Threads Number")
threads_number_label.grid(row=12, column=0)
threads_number_combobox = ttk.Combobox(root, values=["1","2", "3", "Other"])
threads_number_combobox.set("1")
threads_number_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, threads_number_combobox))
threads_number_combobox.grid(row=12, column=1)

stop_after_label = tk.Label(root, text="Stop after nLabels")
stop_after_label.grid(row=13, column=0)
stop_after_combobox = ttk.Combobox(root, values=["1","2", "3", "4", "5", "Other"])
stop_after_combobox.set("1")
stop_after_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, stop_after_combobox))
stop_after_combobox.grid(row=13, column=1)

progressive_slice_height_label = tk.Label(root, text="Progressive Slice Height (Default: 256)")
progressive_slice_height_label.grid(row=14, column=0)
progressive_slice_height_combobox = ttk.Combobox(root, values=["256", "Other"])
progressive_slice_height_combobox.set("256")
progressive_slice_height_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, progressive_slice_height_combobox))
progressive_slice_height_combobox.grid(row=14, column=1)

decode_timeout_label = tk.Label(root, text="Decode Timeout (Default: -1)")
decode_timeout_label.grid(row=15, column=0)
decode_timeout_combobox = ttk.Combobox(root, values=["100", "500", "1000", "Other"])
decode_timeout_combobox.set("-1")
decode_timeout_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, decode_timeout_combobox))
decode_timeout_combobox.grid(row=15, column=1)

progressive_instances_number_label = tk.Label(root, text="Progressive Instances Number")
progressive_instances_number_label.grid(row=16, column=0)
progressive_instances_number_combobox = ttk.Combobox(root, values=["1", "2", "3", "Other"])
progressive_instances_number_combobox.set("1")
progressive_instances_number_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, progressive_instances_number_combobox))
progressive_instances_number_combobox.grid(row=16, column=1)

repeat_label = tk.Label(root, text="Repeat (Default: 1)")
repeat_label.grid(row=17, column=0)
repeat_combobox = ttk.Combobox(root, values=["1", "2", "3", "Other"])
repeat_combobox.set("1")
repeat_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(event, repeat_combobox))
repeat_combobox.grid(row=17, column=1)

verbose_tick = tk.IntVar()
verbose_button = tk.Checkbutton(root, text="Display Verbose", variable=verbose_tick, command=lambda: select_unselect(verbose_tick, "Verbose display is selected", "Verbose display is not selected"))
verbose_button.grid(row=18, column=0)

create_batch_button = tk.Button(root, text="Create Batchfile", command=create_batch_file("C11", "C22", "C33"))
create_batch_button.grid(row=20, column=0)

add_button = tk.Button(root, text="Add", command=lambda: add_string(log_inputbox.get(), loglevel_combobox.get(), heap_memory_combobox.get(), stack_memory_combobox.get(), iteration_combobox.get(), threads_number_combobox.get(), stop_after_combobox.get(), progressive_slice_height_combobox.get(), decode_timeout_combobox.get(), progressive_instances_number_combobox.get(), repeat_combobox.get()))
add_button.grid(row=21, column=0)

create_cmd_button = tk.Button(root, text="Create CMD", command=lambda: create_single_cmd(lightbeam_label.cget("text").split("/")[-1], "configfile", "resultfolder", "imagefolder"))
create_cmd_button.grid(row=22, column=0)

root.mainloop()
