import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

lightbeam = ""
configure = ""
image = ""
hog_file = ""
cmd = ""

###Functions###
def select_lightbeam():
    global lightbeam
    lightbeam = filedialog.askopenfilename(title="Choose LightBeam version")
    lightbeam_label.config(text=lightbeam)  
    print(lightbeam)

def set_configure():
    global configure
    configure = filedialog.askopenfilename(title="Choose configure file")
    configure_label.config(text=configure)
    print(configure)

def image_folder():
    global image 
    image = filedialog.askopenfilename(title="Choose image folder")
    image_label.config(text=image)
    print(image)

def select_hog_file():
    global hog_file 
    hog_file = filedialog.askopenfilename(title="Choose Hog file")
    hog_label.config(text=hog_file)
    print(hog_file)


def toggle_input_log():
    if log_tick.get() == 1:
        log_inputbox.config(state=tk.NORMAL)
        log_browsebutton.config(state=tk.NORMAL)
    else:
        log_inputbox.config(state=tk.DISABLED)
        log_browsebutton.config(state=tk.DISABLED)
        log_inputbox_value = ""

def log_browse():
    global log_file, log_inputbox
    log_file = filedialog.askopenfilename(title="Choose Log file")
    log_inputbox.insert(0, log_file)
    print(log_file)

def select_loglevel(event):
    global loglevel_value
    loglevel_value = loglevel_combobox.get()
    loglevel_combobox.config(state="readonly")

def select_heap_memory(event):
    global heap_memory_value
    heap_memory_value = heap_memory_combobox.get()
    if heap_memory_value == "Other":
        # heap_memory_combobox.config(state="readonly")
        heap_memory_combobox.set("")
        heap_memory_combobox.config(state="normal")
    else:
        heap_memory_combobox.config(state="readonly")

def select_stack_memory(event):
    global stack_memory_value
    stack_memory_value = stack_memory_combobox.get()
    if stack_memory_value == "Other":
        stack_memory_combobox.set("")
        stack_memory_combobox.config(state="normal")
    else:
        stack_memory_combobox.config(state="readonly")

def select_iteration(event):
    global iteration_value
    iteration_value = iteration_combobox.get()
    if iteration_value == "Other":
        iteration_combobox.set("")
        iteration_combobox.config(state="normal")
    else:
        iteration_combobox.config(state="readonly")

def disable_shortcuts():
    if disable_shortcuts_tick.get() == 1:
        print("Disable performance shortcuts is selected.")
    else:
        print("Disable performance shortcuts is not selected.")

def select_threads_number(event):
    global threads_number_value
    threads_number_value = threads_number_combobox.get()
    if threads_number_value == "Other":
        threads_number_combobox.set("")
        threads_number_combobox.config(state="normal")
    else:
        threads_number_combobox.config(state="readonly")

def select_stop_after(event):
    global stop_after_value
    stop_after_value = stop_after_combobox.get()
    if stop_after_value == "Other":
        stop_after_combobox.set("")
        stop_after_combobox.config(state="normal")
    else:
        stop_after_combobox.config(state="readonly")

def select_progressive_slice_height(event):
    global progressive_slice_height_value
    progressive_slice_height_value = progressive_slice_height_combobox.get()
    if progressive_slice_height_value == "Other":
        progressive_slice_height_combobox.set("")
        progressive_slice_height_combobox.config(state="normal")
    else:
        progressive_slice_height_combobox.config(state="readonly")

def select_decode_timeout(event):
    global decode_timeout_value
    decode_timeout_value = decode_timeout_combobox.get()
    if decode_timeout_value == "Other":
        decode_timeout_combobox.set("")
        decode_timeout_combobox.config(state="normal")
    else:
        decode_timeout_combobox.config(state="readonly")

def select_progressive_instances_number(event):
    global progressive_instances_number_value
    progressive_instances_number_value = progressive_instances_number_combobox.get()
    if progressive_instances_number_value == "Other":
        progressive_instances_number_combobox.set("")
        progressive_instances_number_combobox.config(state="normal")
    else:
        progressive_instances_number_combobox.config(state="readonly")

def select_repeat(event):
    global repeat_value
    repeat_value = repeat_combobox.get()
    if repeat_value == "Other":
        repeat_combobox.set("")
        repeat_combobox.config(state="normal")
    else:
        repeat_combobox.config(state="readonly")

def verbose_display():
    if verbose_tick.get() == 1:
        print("Verbose display is selected.")
    else:
        print("Verbose display is not selected.")

def run_function():
    heap_memory_value = heap_memory_combobox.get()
    log_inputbox_value = log_inputbox.get()
    loglevel_value = loglevel_combobox.get()
    cmd = lightbeam + configure + image + heap_memory_value + log_inputbox_value +  loglevel_value
    print(cmd)
    # subprocess.Popen('start cmd', shell=True)


###GUI###
root = tk.Tk()
root.geometry("800x800")

selectfile_label = tk.Label(root, text="Select Files",font=("Arial", 11), anchor="w", fg="blue")
selectfile_label.grid(row=0, column=0)

lightbeam_button = tk.Button(root, text="LightBeam", command=select_lightbeam)
lightbeam_button.grid(row=1, column=0)
lightbeam_label = tk.Label(root, text=lightbeam)
lightbeam_label.grid(row=1, column=1)


configure_button = tk.Button(root, text="ConfigureFile", command=set_configure)
configure_button.grid(row=2, column=0)
configure_label = tk.Label(root, text=configure)
configure_label.grid(row=2, column=1)

image_button = tk.Button(root, text="ImageFolder", command=image_folder)
image_button.grid(row=3, column=0)
image_label = tk.Label(root, text=image)
image_label.grid(row=3, column=1)

hog_button = tk.Button(root, text="HogFile", command=select_hog_file)
hog_button.grid(row=4, column=0)
hog_label = tk.Label(root, text=hog_file)
hog_label.grid(row=4, column=1)

setparameter_label = tk.Label(root, text="Setting Parameters",font=("Arial", 11), anchor="w", fg="blue")
setparameter_label.grid(row=5, column=0)

log_tick = tk.BooleanVar()
log_checkbutton = tk.Checkbutton(root, text="Enable Logging (Default: Disabled)", variable=log_tick, command=toggle_input_log)
log_checkbutton.grid(row=6, column=0)
log_inputbox = tk.Entry(root, state=tk.DISABLED)
log_inputbox.grid(row=6, column=1)
log_browsebutton = tk.Button(root, text="Browse", state=tk.DISABLED, command= log_browse )
log_browsebutton.grid(row=6, column=2)

loglevel_label = tk.Label(root, text="Log Level (Default: 0)")
loglevel_label.grid(row=7, column=0)
loglevel_combobox = ttk.Combobox(root, values=["0", "1", "2", "3"])
loglevel_combobox.set("0")
loglevel_combobox.bind("<<ComboboxSelected>>", select_loglevel)
loglevel_combobox.grid(row=7, column=1)

heap_memory_label = tk.Label(root, text="Heap Memory (Default: 10000)")
heap_memory_label.grid(row=8, column=0)
heap_memory_combobox = ttk.Combobox(root, values=["10000","100000", "200000", "Other"])
heap_memory_combobox.set("10000")
heap_memory_combobox.bind("<<ComboboxSelected>>", select_heap_memory)
heap_memory_combobox.grid(row=8, column=1)

stack_memory_label = tk.Label(root, text="Stack Memory (Default: 11000)")
stack_memory_label.grid(row=9, column=0)
stack_memory_combobox = ttk.Combobox(root, values=["11000","20000", "50000", "Other"])
stack_memory_combobox.set("11000")
stack_memory_combobox.bind("<<ComboboxSelected>>", select_stack_memory)
stack_memory_combobox.grid(row=9, column=1)

iteration_label = tk.Label(root, text="Iteration (Default: 1)")
iteration_label.grid(row=10, column=0)
iteration_combobox = ttk.Combobox(root, values=["1","5", "10", "Other"])
iteration_combobox.set("1")
iteration_combobox.bind("<<ComboboxSelected>>", select_iteration)
iteration_combobox.grid(row=10, column=1)

disable_shortcuts_tick = tk.IntVar()
disable_shortcuts_button = tk.Checkbutton(root, text="Disable Shortcuts", variable=disable_shortcuts_tick, command=disable_shortcuts)
disable_shortcuts_button.grid(row=11, column=0)

threads_number_label = tk.Label(root, text="Threads Number")
threads_number_label.grid(row=12, column=0)
threads_number_combobox = ttk.Combobox(root, values=["1","2", "3", "Other"])
threads_number_combobox.set("1")
threads_number_combobox.bind("<<ComboboxSelected>>", select_threads_number)
threads_number_combobox.grid(row=12, column=1)

stop_after_label = tk.Label(root, text="Stop after nLabels")
stop_after_label.grid(row=13, column=0)
stop_after_combobox = ttk.Combobox(root, values=["1","2", "3", "4", "5", "Other"])
stop_after_combobox.set("1")
stop_after_combobox.bind("<<ComboboxSelected>>", select_stop_after)
stop_after_combobox.grid(row=13, column=1)

progressive_slice_height_label = tk.Label(root, text="Progressive Slice Height (Default: 256)")
progressive_slice_height_label.grid(row=14, column=0)
progressive_slice_height_combobox = ttk.Combobox(root, values=["256", "Other"])
progressive_slice_height_combobox.set("256")
progressive_slice_height_combobox.bind("<<ComboboxSelected>>", select_progressive_slice_height)
progressive_slice_height_combobox.grid(row=14, column=1)

decode_timeout_label = tk.Label(root, text="Decode Timeout (Default: -1)")
decode_timeout_label.grid(row=15, column=0)
decode_timeout_combobox = ttk.Combobox(root, values=["100", "500", "1000", "Other"])
decode_timeout_combobox.set("-1")
decode_timeout_combobox.bind("<<ComboboxSelected>>", select_decode_timeout)
decode_timeout_combobox.grid(row=15, column=1)

progressive_instances_number_label = tk.Label(root, text="Progressive Instances Number")
progressive_instances_number_label.grid(row=16, column=0)
progressive_instances_number_combobox = ttk.Combobox(root, values=["1", "2", "3", "Other"])
progressive_instances_number_combobox.set("1")
progressive_instances_number_combobox.bind("<<ComboboxSelected>>", select_progressive_instances_number)
progressive_instances_number_combobox.grid(row=16, column=1)

repeat_label = tk.Label(root, text="Repeat (Default: 1)")
repeat_label.grid(row=17, column=0)
repeat_combobox = ttk.Combobox(root, values=["1", "2", "3", "Other"])
repeat_combobox.set("1")
repeat_combobox.bind("<<ComboboxSelected>>", select_repeat)
repeat_combobox.grid(row=17, column=1)

verbose_tick = tk.IntVar()
verbose_button = tk.Checkbutton(root, text="Display Verbose", variable=verbose_tick, command=verbose_display)
verbose_button.grid(row=18, column=0)

run_button = tk.Button(root, text="Run", command=run_function)
run_button.grid(row=20, column=0)

root.mainloop()
