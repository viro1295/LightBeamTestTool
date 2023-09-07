# import subprocess
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from function import *

lightbeam = ""
configure = ""
resultfolder = ""
imagefolder = ""
hogfile = ""
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
run_menu.add_command(label="Create BatchFile", command=lambda: create_batch_file(message_label, lightbeam_label.cget("text").split("/")[-1], log_addCMD_tick, log_inputbox.get(), loglevel_addCMD_tick, loglevel_combobox.get(),  heap_memory_addCMD_tick, heap_memory_combobox.get(), stack_memory_addCMD_tick, stack_memory_combobox.get(), iteration_addCMD_tick, iteration_combobox.get(), disable_shortcuts_addCMD_tick, threads_number_addCMD_tick, threads_number_combobox.get(), stop_after_addCMD_tick, stop_after_combobox.get(), progressive_slice_height_addCMD_tick, progressive_slice_height_combobox.get(), decode_timeout_addCMD_tick, decode_timeout_combobox.get(), progressive_instances_number_addCMD_tick, progressive_instances_number_combobox.get(), repeat_addCMD_tick, repeat_combobox.get(), verbose_addCMD_tick))
run_menu.add_command(label="Create Single CMD", command=lambda: create_single_cmd(message_label, lightbeam_label.cget("text").split("/")[-1], configure_label.cget("text"), "resultfolder", imagefolder_label.cget("text"), log_addCMD_tick, log_inputbox.get(), loglevel_addCMD_tick, loglevel_combobox.get(),  heap_memory_addCMD_tick, heap_memory_combobox.get(), stack_memory_addCMD_tick, stack_memory_combobox.get(), iteration_addCMD_tick, iteration_combobox.get(), disable_shortcuts_addCMD_tick, threads_number_addCMD_tick, threads_number_combobox.get(), stop_after_addCMD_tick, stop_after_combobox.get(), progressive_slice_height_addCMD_tick, progressive_slice_height_combobox.get(), decode_timeout_addCMD_tick, decode_timeout_combobox.get(), progressive_instances_number_addCMD_tick, progressive_instances_number_combobox.get(), repeat_addCMD_tick, repeat_combobox.get(), verbose_addCMD_tick))
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

resultfolder_photo = ImageTk.PhotoImage(Image.open(".\\icon\\resultfolder_icon.jpg"))
resultfolder_button = tk.Button(toolbar, image=resultfolder_photo, text="ResultFolder", command=lambda: choosefolder_insertwidget(message_label, resultfolder, "Choose result folder", resultfolder_label))
resultfolder_button.bind("<Enter>",lambda event: show_tooltip(event, toolbar, resultfolder_button, "ResultFolder"))
resultfolder_button.bind("<Leave>",lambda event: hide_tooltip(event, resultfolder_button))
resultfolder_button.pack(side=tk.LEFT, padx=2, pady=2)

imagefolder_photo = ImageTk.PhotoImage(Image.open(".\\icon\\imagefolder_icon.jpg"))
imagefolder_button = tk.Button(toolbar, image=imagefolder_photo, text="ImageFolder", command=lambda: choosefolder_insertwidget(message_label, imagefolder, "Choose image folder", imagefolder_label))
imagefolder_button.bind("<Enter>",lambda event: show_tooltip(event, toolbar, imagefolder_button, "ImageFolder"))
imagefolder_button.bind("<Leave>",lambda event: hide_tooltip(event, imagefolder_button))
imagefolder_button.pack(side=tk.LEFT, padx=2, pady=2)

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

title_resultfolder_label = tk.Label(configframe, text="ResultFolder: ")
title_resultfolder_label.grid(row=2, column=0, sticky='e')
resultfolder_label = tk.Label(configframe, text=resultfolder)
resultfolder_label.grid(row=2, column=1, sticky='w')

title_imagefolder_label = tk.Label(configframe, text="ImageFolder: ")
title_imagefolder_label.grid(row=3, column=0, sticky='e')
imagefolder_label = tk.Label(configframe, text=imagefolder)
imagefolder_label.grid(row=3, column=1, sticky='w')

###################ParameterFrame###################
parameterframe = tk.Frame(root)
parameterframe.pack(side=tk.TOP, fill=tk.X)

hogfile_tick = tk.BooleanVar()
hogfile_checkbutton = tk.Checkbutton(parameterframe, text="Hog File (Default: None)", variable=hogfile_tick, command=lambda: toggle_widgetstate(message_label, hogfile_tick, hogfile_inputbox, hogfile_browsebutton))
hogfile_checkbutton.grid(row=0, column=0, sticky='e')
hogfile_inputbox = tk.Entry(parameterframe, state=tk.DISABLED)
hogfile_inputbox.grid(row=0, column=1, sticky='w')
hogfile_browsebutton = tk.Button(parameterframe, text="Browse", state=tk.DISABLED, command=lambda: choosefile_insertwidget(message_label, hogfile, "Choose Hog file", hogfile_inputbox))
hogfile_browsebutton.grid(row=0, column=2, sticky='w')
hogfile_addCMD_tick = tk.BooleanVar()
hogfile_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=hogfile_addCMD_tick, command=lambda: check_addtoCMD(message_label, hogfile_addCMD_tick, "-t ", hogfile_inputbox.get()))
hogfile_addCMD_checkbutton.grid(row=0, column=3, sticky='w')

log_tick = tk.BooleanVar()
log_checkbutton = tk.Checkbutton(parameterframe, text="Enable Logging (Default: Disabled)", variable=log_tick, command=lambda: toggle_widgetstate(message_label, log_tick, log_inputbox, log_browsebutton))
log_checkbutton.grid(row=1, column=0, sticky='e')
log_inputbox = tk.Entry(parameterframe, state=tk.DISABLED)
log_inputbox.grid(row=1, column=1, sticky='w')
log_browsebutton = tk.Button(parameterframe, text="Browse", state=tk.DISABLED, command=lambda: choosefile_insertwidget(message_label, log_file, "Choose Log file", log_inputbox))
log_browsebutton.grid(row=1, column=2, sticky='w')
log_addCMD_tick = tk.BooleanVar()
log_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=log_addCMD_tick, command=lambda: check_addtoCMD(message_label, log_addCMD_tick, "-l ", log_inputbox.get()))
log_addCMD_checkbutton.grid(row=1, column=3, sticky='w')

loglevel_label = tk.Label(parameterframe, text="Log Level (Default: 0)")
loglevel_label.grid(row=2, column=0, sticky='e')
loglevel_combobox = ttk.Combobox(parameterframe, values=["0", "1", "2", "3"])
loglevel_combobox.set("0")
loglevel_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, loglevel_combobox))
loglevel_combobox.grid(row=2, column=1, sticky='w')
loglevel_addCMD_tick = tk.BooleanVar()
loglevel_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=loglevel_addCMD_tick, command=lambda: check_addtoCMD(message_label, loglevel_addCMD_tick, "--log_level ", loglevel_combobox.get()))
loglevel_addCMD_checkbutton.grid(row=2, column=3, sticky='w')

heap_memory_label = tk.Label(parameterframe, text="Heap Memory (Default: 10000)")
heap_memory_label.grid(row=3, column=0, sticky='e')
heap_memory_combobox = ttk.Combobox(parameterframe, values=["10000","100000", "200000", "Other"])
heap_memory_combobox.set("10000")
heap_memory_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, heap_memory_combobox))
heap_memory_combobox.grid(row=3, column=1, sticky='w')
heap_memory_addCMD_tick = tk.BooleanVar()
heap_memory_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=heap_memory_addCMD_tick, command=lambda: check_addtoCMD(message_label, heap_memory_addCMD_tick, "-m ", heap_memory_combobox.get()))
heap_memory_addCMD_checkbutton.grid(row=3, column=3, sticky='w')

stack_memory_label = tk.Label(parameterframe, text="Stack Memory (Default: 11000)")
stack_memory_label.grid(row=4, column=0, sticky='e')
stack_memory_combobox = ttk.Combobox(parameterframe, values=["11000","20000", "50000", "Other"])
stack_memory_combobox.set("11000")
stack_memory_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, stack_memory_combobox))
stack_memory_combobox.grid(row=4, column=1, sticky='w')
stack_memory_addCMD_tick = tk.BooleanVar()
stack_memory_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=stack_memory_addCMD_tick, command=lambda: check_addtoCMD(message_label, stack_memory_addCMD_tick, "--stack ", stack_memory_combobox.get()))
stack_memory_addCMD_checkbutton.grid(row=4, column=3, sticky='w')

iteration_label = tk.Label(parameterframe, text="Iteration (Default: 1)")
iteration_label.grid(row=5, column=0, sticky='e')
iteration_combobox = ttk.Combobox(parameterframe, values=["1","5", "10", "Other"])
iteration_combobox.set("1")
iteration_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, iteration_combobox))
iteration_combobox.grid(row=5, column=1, sticky='w')
iteration_addCMD_tick = tk.BooleanVar()
iteration_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=iteration_addCMD_tick, command=lambda: check_addtoCMD(message_label, iteration_addCMD_tick, "-i ", iteration_combobox.get()))
iteration_addCMD_checkbutton.grid(row=5, column=3, sticky='w')

disable_shortcuts_tick = tk.IntVar()
disable_shortcuts_button = tk.Checkbutton(parameterframe, text="Disable Shortcuts", variable=disable_shortcuts_tick, command=lambda: select_unselect(message_label, disable_shortcuts_tick, "Disable shortcuts is selected", "Disable shortcuts is not selected"))
disable_shortcuts_button.grid(row=6, column=0, sticky='e')
disable_shortcuts_addCMD_tick = tk.BooleanVar()
disable_shortcuts_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=disable_shortcuts_addCMD_tick, command=lambda: check_addtoCMD(message_label, disable_shortcuts_addCMD_tick, "--disable-shortcuts ", ""))
disable_shortcuts_addCMD_checkbutton.grid(row=6, column=3, sticky='w')

threads_number_label = tk.Label(parameterframe, text="Threads Number")
threads_number_label.grid(row=7, column=0, sticky='e')
threads_number_combobox = ttk.Combobox(parameterframe, values=["1","2", "3", "Other"])
threads_number_combobox.set("1")
threads_number_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, threads_number_combobox))
threads_number_combobox.grid(row=7, column=1, sticky='w')
threads_number_addCMD_tick = tk.BooleanVar()
threads_number_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=threads_number_addCMD_tick, command=lambda: check_addtoCMD(message_label, threads_number_addCMD_tick, "--threads ", threads_number_combobox.get()))
threads_number_addCMD_checkbutton.grid(row=7, column=3, sticky='w')

stop_after_label = tk.Label(parameterframe, text="Stop after nLabels")
stop_after_label.grid(row=8, column=0, sticky='e')
stop_after_combobox = ttk.Combobox(parameterframe, values=["1","2", "3", "4", "5", "Other"])
stop_after_combobox.set("1")
stop_after_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, stop_after_combobox))
stop_after_combobox.grid(row=8, column=1, sticky='w')
stop_after_addCMD_tick = tk.BooleanVar()
stop_after_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=stop_after_addCMD_tick, command=lambda: check_addtoCMD(message_label, stop_after_addCMD_tick, "--stop_after_labels ", stop_after_combobox.get()))
stop_after_addCMD_checkbutton.grid(row=8, column=3, sticky='w')

progressive_slice_height_label = tk.Label(parameterframe, text="Progressive Slice Height (Default: 256)")
progressive_slice_height_label.grid(row=9, column=0, sticky='e')
progressive_slice_height_combobox = ttk.Combobox(parameterframe, values=["256", "Other"])
progressive_slice_height_combobox.set("256")
progressive_slice_height_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, progressive_slice_height_combobox))
progressive_slice_height_combobox.grid(row=9, column=1, sticky='w')
progressive_slice_height_addCMD_tick = tk.BooleanVar()
progressive_slice_height_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=progressive_slice_height_addCMD_tick, command=lambda: check_addtoCMD(message_label, progressive_slice_height_addCMD_tick, "--progressive_slice_height ", progressive_slice_height_combobox.get()))
progressive_slice_height_addCMD_checkbutton.grid(row=9, column=3, sticky='w')

decode_timeout_label = tk.Label(parameterframe, text="Decode Timeout (Default: -1)")
decode_timeout_label.grid(row=10, column=0, sticky='e')
decode_timeout_combobox = ttk.Combobox(parameterframe, values=["100", "500", "1000", "Other"])
decode_timeout_combobox.set("-1")
decode_timeout_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, decode_timeout_combobox))
decode_timeout_combobox.grid(row=10, column=1, sticky='w')
decode_timeout_addCMD_tick = tk.BooleanVar()
decode_timeout_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=decode_timeout_addCMD_tick, command=lambda: check_addtoCMD(message_label, decode_timeout_addCMD_tick, "--decode_timeout ", decode_timeout_combobox.get()))
decode_timeout_addCMD_checkbutton.grid(row=10, column=3, sticky='w')

progressive_instances_number_label = tk.Label(parameterframe, text="Progressive Instances Number")
progressive_instances_number_label.grid(row=11, column=0, sticky='e')
progressive_instances_number_combobox = ttk.Combobox(parameterframe, values=["1", "2", "3", "Other"])
progressive_instances_number_combobox.set("1")
progressive_instances_number_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, progressive_instances_number_combobox))
progressive_instances_number_combobox.grid(row=11, column=1, sticky='w')
progressive_instances_number_addCMD_tick = tk.BooleanVar()
progressive_instances_number_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=progressive_instances_number_addCMD_tick, command=lambda: check_addtoCMD(message_label, progressive_instances_number_addCMD_tick, "--mip ", progressive_instances_number_combobox.get()))
progressive_instances_number_addCMD_checkbutton.grid(row=11, column=3, sticky='w')

repeat_label = tk.Label(parameterframe, text="Repeat (Default: 1)")
repeat_label.grid(row=12, column=0, sticky='e')
repeat_combobox = ttk.Combobox(parameterframe, values=["1", "2", "3", "Other"])
repeat_combobox.set("1")
repeat_combobox.bind("<<ComboboxSelected>>", lambda event: setstate_combobox(message_label, event, repeat_combobox))
repeat_combobox.grid(row=12, column=1, sticky='w')
repeat_addCMD_tick = tk.BooleanVar()
repeat_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=repeat_addCMD_tick, command=lambda: check_addtoCMD(message_label, repeat_addCMD_tick, "--repeat ", repeat_combobox.get()))
repeat_addCMD_checkbutton.grid(row=12, column=3, sticky='w')

verbose_tick = tk.IntVar()
verbose_button = tk.Checkbutton(parameterframe, text="Display Verbose", variable=verbose_tick, command=lambda: select_unselect(message_label, verbose_tick, "Verbose display is selected", "Verbose display is not selected"))
verbose_button.grid(row=13, column=0, sticky='e')
verbose_addCMD_tick = tk.BooleanVar()
verbose_addCMD_checkbutton = tk.Checkbutton(parameterframe, text="Add CMD", variable=verbose_addCMD_tick, command=lambda: check_addtoCMD(message_label, verbose_addCMD_tick, "-v ", ""))
verbose_addCMD_checkbutton.grid(row=13, column=3, sticky='w')

#######################MessageFrame#########################
messageframe = tk.Frame(root, borderwidth=0.5, relief="sunken", bg="#CCCCCC")
messageframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
message_label = tk.Label(messageframe, text=message, bg="#CCCCCC")
message_label.pack()

root.mainloop()
