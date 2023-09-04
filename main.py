# import subprocess
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from function import *

lightbeam = ""
configure = ""
image = ""
hog_file = ""
log_file = ""
message = "This is message box!"

###GUI###
root = tk.Tk()
root.title("LightBeam test tool")
root.iconbitmap(".\\icon\\lightbeam_icon.ico")
root.geometry("800x600")

##################MenuBar##################
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Load LightBeam", command=lambda: choosefile_insertwidget(message_label, lightbeam, "Choose LightBeam version", lightbeam_label))
file_menu.add_command(label="Save Settings")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=file_menu)

run_menu = tk.Menu(menubar, tearoff=0)
run_menu.add_command(label="Create BatchFile", command=lambda: create_batch_file(message_label, "C11", "C22", "C33"))
run_menu.add_command(label="Create Single CMD", command=lambda: create_single_cmd(lightbeam_label.cget("text").split("/")[-1], "configfile", "resultfolder", "imagefolder"))
run_menu.add_command(label="Add String", command=lambda: add_string(log_inputbox.get(), loglevel_combobox.get(), heap_memory_combobox.get(), stack_memory_combobox.get(), iteration_combobox.get(), threads_number_combobox.get(), stop_after_combobox.get(), progressive_slice_height_combobox.get(), decode_timeout_combobox.get(), progressive_instances_number_combobox.get(), repeat_combobox.get()))
menubar.add_cascade(label="Run", menu=run_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Document", command=lambda: document_function(message_label, root))
help_menu.add_command(label="About", command=lambda: about_function(message_label, root))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

###################ToolBar###################
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)


lightbeam_button_photo = ImageTk.PhotoImage(Image.open(".\\icon\\lightbeam_file_icon.jpg"))
lightbeam_button = tk.Button(toolbar, image=lightbeam_button_photo, text="LightBeam", command=lambda: choosefile_insertwidget(message_label, lightbeam, "Choose LightBeam version", lightbeam_label))
lightbeam_button.bind("<Enter>",lambda event: show_tooltip(event, toolbar, lightbeam_button, "LightBeam"))
lightbeam_button.bind("<Leave>",lambda event: hide_tooltip(event, lightbeam_button))
lightbeam_button.pack(side=tk.LEFT, padx=2, pady=2)

configure_button_photo = ImageTk.PhotoImage(Image.open(".\\icon\\configfile_icon.jpg"))
configure_button = tk.Button(toolbar, image=configure_button_photo, text="ConfigureFile", command=lambda: choosefile_insertwidget(message_label, configure, "Choose configure file", configure_label))
configure_button.bind("<Enter>",lambda event: show_tooltip(event, toolbar, configure_button, "ConfigureFile"))
configure_button.bind("<Leave>",lambda event: hide_tooltip(event, configure_button))
configure_button.pack(side=tk.LEFT, padx=2, pady=2)

imagefolder_photo = ImageTk.PhotoImage(Image.open(".\\icon\\imagefolder_icon.jpg"))
image_button = tk.Button(toolbar, image=imagefolder_photo, text="ImageFolder", command=lambda: choosefile_insertwidget(message_label, image, "Choose image folder", image_label))
image_button.bind("<Enter>",lambda event: show_tooltip(event, toolbar, image_button, "ImageFolder"))
image_button.bind("<Leave>",lambda event: hide_tooltip(event, image_button))
image_button.pack(side=tk.LEFT, padx=2, pady=2)

hogfile_photo = ImageTk.PhotoImage(Image.open(".\\icon\\hogfile_icon.jpg"))
hog_button = tk.Button(toolbar, image=hogfile_photo, text="HogFile", command=lambda: choosefile_insertwidget(message_label, hog_file, "Choose Hog file", hog_label))
hog_button.bind("<Enter>",lambda event: show_tooltip(event, toolbar, hog_button, "HogFile"))
hog_button.bind("<Leave>",lambda event: hide_tooltip(event, hog_button))
hog_button.pack(side=tk.LEFT, padx=2, pady=2)

###################ConfigInfoFrame###################
configframe = tk.Frame(root, borderwidth=0.5, relief="solid")
configframe.pack(side=tk.TOP, fill=tk.X)

title_lightbeam_label = tk.Label(configframe, text="LightBeam: ")
title_lightbeam_label.grid(row=0, column=0, sticky='e')
lightbeam_label = tk.Label(configframe, text=lightbeam)
lightbeam_label.grid(row=0, column=1, sticky='w')

title_configure_label = tk.Label(configframe, text="ConfigureFile: ")
title_configure_label.grid(row=1, column=0, sticky='e')
configure_label = tk.Label(configframe, text=configure)
configure_label.grid(row=1, column=1, sticky='w')

title_image_label = tk.Label(configframe, text="ImageFolder: ")
title_image_label.grid(row=2, column=0, sticky='e')
image_label = tk.Label(configframe, text=image)
image_label.grid(row=2, column=1, sticky='w')

title_hog_label = tk.Label(configframe, text="HogFile: ")
title_hog_label.grid(row=3, column=0, sticky='e')
hog_label = tk.Label(configframe, text=hog_file)
hog_label.grid(row=3, column=1, sticky='w')

###################ParameterFrame###################
parameterframe = tk.Frame(root)
parameterframe.pack(side=tk.TOP, fill=tk.X)

log_tick = tk.BooleanVar()
log_checkbutton = tk.Checkbutton(parameterframe, text="Enable Logging (Default: Disabled)", variable=log_tick, command=lambda: toggle_widgetstate(message_label, log_tick, log_inputbox, log_browsebutton))
log_checkbutton.grid(row=0, column=0, sticky='e')
log_inputbox = tk.Entry(parameterframe, state=tk.DISABLED)
log_inputbox.grid(row=0, column=1, sticky='w')
log_browsebutton = tk.Button(parameterframe, text="Browse", state=tk.DISABLED, command=lambda: choosefile_insertwidget(message_label, log_file, "Choose Log file", log_inputbox))
log_browsebutton.grid(row=0, column=2, sticky='w')

loglevel_label = tk.Label(parameterframe, text="Log Level (Default: 0)")
loglevel_label.grid(row=1, column=0, sticky='e')
loglevel_combobox = ttk.Combobox(parameterframe, values=["0", "1", "2", "3"])
loglevel_combobox.set("0")
loglevel_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, loglevel_combobox))
loglevel_combobox.grid(row=1, column=1, sticky='w')

heap_memory_label = tk.Label(parameterframe, text="Heap Memory (Default: 10000)")
heap_memory_label.grid(row=2, column=0, sticky='e')
heap_memory_combobox = ttk.Combobox(parameterframe, values=["10000","100000", "200000", "Other"])
heap_memory_combobox.set("10000")
heap_memory_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, heap_memory_combobox))
heap_memory_combobox.grid(row=2, column=1, sticky='w')

stack_memory_label = tk.Label(parameterframe, text="Stack Memory (Default: 11000)")
stack_memory_label.grid(row=3, column=0, sticky='e')
stack_memory_combobox = ttk.Combobox(parameterframe, values=["11000","20000", "50000", "Other"])
stack_memory_combobox.set("11000")
stack_memory_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, stack_memory_combobox))
stack_memory_combobox.grid(row=3, column=1, sticky='w')

iteration_label = tk.Label(parameterframe, text="Iteration (Default: 1)")
iteration_label.grid(row=4, column=0, sticky='e')
iteration_combobox = ttk.Combobox(parameterframe, values=["1","5", "10", "Other"])
iteration_combobox.set("1")
iteration_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, iteration_combobox))
iteration_combobox.grid(row=4, column=1, sticky='w')

disable_shortcuts_tick = tk.IntVar()
disable_shortcuts_button = tk.Checkbutton(parameterframe, text="Disable Shortcuts", variable=disable_shortcuts_tick, command=lambda: select_unselect(message_label, disable_shortcuts_tick, "Disable shortcuts is selected", "Disable shortcuts is not selected"))
disable_shortcuts_button.grid(row=5, column=0, sticky='e')

threads_number_label = tk.Label(parameterframe, text="Threads Number")
threads_number_label.grid(row=6, column=0, sticky='e')
threads_number_combobox = ttk.Combobox(parameterframe, values=["1","2", "3", "Other"])
threads_number_combobox.set("1")
threads_number_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, threads_number_combobox))
threads_number_combobox.grid(row=6, column=1, sticky='w')

stop_after_label = tk.Label(parameterframe, text="Stop after nLabels")
stop_after_label.grid(row=7, column=0, sticky='e')
stop_after_combobox = ttk.Combobox(parameterframe, values=["1","2", "3", "4", "5", "Other"])
stop_after_combobox.set("1")
stop_after_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, stop_after_combobox))
stop_after_combobox.grid(row=7, column=1, sticky='w')

progressive_slice_height_label = tk.Label(parameterframe, text="Progressive Slice Height (Default: 256)")
progressive_slice_height_label.grid(row=8, column=0, sticky='e')
progressive_slice_height_combobox = ttk.Combobox(parameterframe, values=["256", "Other"])
progressive_slice_height_combobox.set("256")
progressive_slice_height_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, progressive_slice_height_combobox))
progressive_slice_height_combobox.grid(row=8, column=1, sticky='w')

decode_timeout_label = tk.Label(parameterframe, text="Decode Timeout (Default: -1)")
decode_timeout_label.grid(row=9, column=0, sticky='e')
decode_timeout_combobox = ttk.Combobox(parameterframe, values=["100", "500", "1000", "Other"])
decode_timeout_combobox.set("-1")
decode_timeout_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, decode_timeout_combobox))
decode_timeout_combobox.grid(row=9, column=1, sticky='w')

progressive_instances_number_label = tk.Label(parameterframe, text="Progressive Instances Number")
progressive_instances_number_label.grid(row=10, column=0, sticky='e')
progressive_instances_number_combobox = ttk.Combobox(parameterframe, values=["1", "2", "3", "Other"])
progressive_instances_number_combobox.set("1")
progressive_instances_number_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, progressive_instances_number_combobox))
progressive_instances_number_combobox.grid(row=10, column=1, sticky='w')

repeat_label = tk.Label(parameterframe, text="Repeat (Default: 1)")
repeat_label.grid(row=11, column=0, sticky='e')
repeat_combobox = ttk.Combobox(parameterframe, values=["1", "2", "3", "Other"])
repeat_combobox.set("1")
repeat_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, repeat_combobox))
repeat_combobox.grid(row=11, column=1, sticky='w')

verbose_tick = tk.IntVar()
verbose_button = tk.Checkbutton(parameterframe, text="Display Verbose", variable=verbose_tick, command=lambda: select_unselect(message_label, verbose_tick, "Verbose display is selected", "Verbose display is not selected"))
verbose_button.grid(row=12, column=0, sticky='e')

#######################MessageFrame#########################
messageframe = tk.Frame(root, borderwidth=0.5, relief="sunken", bg="#CCCCCC")
messageframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
message_label = tk.Label(messageframe, text=message, bg="#CCCCCC")
message_label.pack()


root.mainloop()
