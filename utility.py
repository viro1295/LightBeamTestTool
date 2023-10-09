import io
import base64
import subprocess
import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from base64img import *


################UtilityFunctions######################

def choosefile_insertinputbox(messagelabel, filepath, dialogname, inputbox, addCMD_checkbutton):
    messagelabel.config(text="Choose file from computer")
    filepath = filedialog.askopenfilename(title=dialogname)
    inputbox.delete(0, tk.END)
    inputbox.insert(0, filepath)
    if filepath != "":
        addCMD_checkbutton.config(state=tk.NORMAL)

def choosefile_insertwidget(messagelabel, filepath, dialogname, widget):
    messagelabel.config(text="Choose file from computer")
    filepath = filedialog.askopenfilename(title=dialogname)
    if isinstance(widget, tk.Label):
        widget.config(text=filepath)
    elif isinstance(widget, tk.Entry):
        widget.delete(0, tk.END)
        widget.insert(0, filepath)

def choosefile_singleimage(messagelabel, dialogname, imagefolderlabel):
    messagelabel.config(text="Choose file from computer")
    filepath = filedialog.askopenfilename(title=dialogname)
    current_dir = os.getcwd()
    OneImage_dir = os.path.join(current_dir, 'OneImage')
    if os.path.exists(OneImage_dir):
        shutil.rmtree(OneImage_dir)
        os.makedirs(OneImage_dir)
    else:
        os.makedirs(OneImage_dir)
    if filepath != "":
        shutil.copy(filepath, OneImage_dir)
        imagefolderlabel.config(text=OneImage_dir.replace("\\","/"))
    else:
        imagefolderlabel.config(text="")

def choosefolder_insertwidget(messagelabel, folderpath, dialogname, widget):
    messagelabel.config(text="Choose folder from computer")
    folderpath = filedialog.askdirectory(title=dialogname)
    widget.config(text=folderpath)

def action_on_combobox(messagelabel, event, combobox, label, default_value, addCMD_tick, addCMD_checkbutton):
    messagelabel.config(text="Set value for parameter")
    currentvalue_combobox = combobox.get()
    if combobox.get() != default_value and combobox.get() != "Other":
        combobox.set("")
        combobox.set(currentvalue_combobox)
        combobox.configure(state="readonly", foreground="blue")
        label.config(fg="blue")
        addCMD_checkbutton['fg'] = 'blue'
        addCMD_tick.set(True)
    elif combobox.get() != default_value and combobox.get() == "Other":
        combobox.set("")
        combobox.configure(state="normal", foreground="blue")
        label.config(fg="blue")
        addCMD_checkbutton['fg'] = 'blue'
        addCMD_tick.set(True)
    else:
        combobox.set("")
        combobox.set(currentvalue_combobox)
        combobox.configure(state="readonly", foreground="black")
        label.config(fg="black")
        addCMD_checkbutton['fg'] = 'black'
        addCMD_tick.set(False)
        
def action_on_choosefile_checkbutton(messagelabel, item_tick, item_checkbutton, entry_widget, button_widget, addCMD_tick, addCMD_checkbutton):
    if item_tick.get() == 1:
        messagelabel.config(text="NORMAL state has been set")
        item_checkbutton['fg'] = 'blue'
        entry_widget.config(state=tk.NORMAL, fg="blue")
        button_widget.config(state=tk.NORMAL)
    else:
        messagelabel.config(text="DISABLED state has been set")
        item_checkbutton['fg'] = 'black'
        entry_widget.delete(0, tk.END)
        entry_widget.config(state=tk.DISABLED, fg="black")
        button_widget.config(state=tk.DISABLED)
        addCMD_tick.set(False)
        addCMD_checkbutton.config(state=tk.DISABLED, fg="black")

def action_on_choosefile_entrybox(event, entrybox, addCMD_tick, addCMD_checkbutton):
    if entrybox.get() != "":
        addCMD_checkbutton.config(state=tk.NORMAL)
    else:
        addCMD_tick.set(False)
        addCMD_checkbutton['fg'] = 'black'
        addCMD_checkbutton.config(state=tk.DISABLED)

def select_unselect(messagelabel, item_tick, item_checkbutton, addCMD_tick, addCMD_checkbutton):
    if item_tick.get() == 1:
        messagelabel.config(text="Checked parameter")
        item_checkbutton['fg'] = 'blue'
        addCMD_checkbutton['fg'] = 'blue'
        addCMD_tick.set(True)
    else:
        messagelabel.config(text="Unchecked parameter")
        item_checkbutton['fg'] = 'black'
        addCMD_checkbutton['fg'] = 'black'
        addCMD_tick.set(False)

def document_function(messagelabel, window):
    messagelabel.config(text="Show command syntax usage")
    documentwindow = tk.Toplevel(window)
    documentwindow.title("Usage")
    documentwindow.iconphoto(False, ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(document_icon)))))
    documentwindow.geometry("600x400")
    document_label = tk.Label(documentwindow, text='''
    lightbeam decode [OPTION...] Images folder
    -h, --help Print usage
    -c, --config arg Configuration file (.vlc)
    -r, --results arg Results output file
    -t, --templates arg Hog templates file
    -l, --log_file arg Enable logging and save messages on target file
    --log_level arg Set the log level (default: 0)
    -m, --memory arg Heap memory (KB) (default: 10000)
    --stack arg Stack memory (KB) (default: 11000)
    -i, --iterations arg Profiling iterations (default: 1)
    --disable-shortcuts Disable performance shortcuts
    --threads arg Total number of threads used internally in the VL6
    --stop_after_labels arg Maximum number of labels present in the image, if reached decoding is stopped
    --progressive_slice_height arg Progressive decoding mode image slices height (default: 256)
    --decode_timeout arg Decode timeout (ms)(default: -1 that means disabled)
    --mip Set the number of intances that run the progressive modee
    --repeat Number of times each image is decoded. Useful to spot memory leaks
    -v, --verbose Verbose display (optional)
    ''', anchor="w", justify="left")
    document_label.pack()

def about_function(messagelabel, window):
    messagelabel.config(text="Show test tool information")
    aboutwindow = tk.Toplevel(window)
    aboutwindow.title("About")
    aboutwindow.iconphoto(False, ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(about_icon)))))
    aboutwindow.geometry("300x30")
    about_label = tk.Label(aboutwindow, text="LightBeam test tool v.1.0.1")
    about_label.pack()
    
def show_tooltip(event, window, button, content):
    button.tooltip = tk.Toplevel(window)
    button.tooltip.wm_overrideredirect(True)
    button.tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
    
    label = ttk.Label(button.tooltip, text=content, background="yellow")
    label.pack()

def hide_tooltip(event, button):
    button.tooltip.destroy()

def check_addtoCMD_entrybox(messagelabel, addCMD_tick, addCMD_checkbutton):
    if addCMD_tick.get() == 1:
        messagelabel.config(text="Added parameter to CMD")
        addCMD_checkbutton['fg'] = 'blue'
    else:
        messagelabel.config(text="Removed parameter from CMD")
        addCMD_checkbutton['fg'] = 'black'

def check_addtoCMD_combobox(messagelabel, addCMD_tick, addCMD_checkbutton, label, combobox, default_value):
    if addCMD_tick.get() == 1:
        messagelabel.config(text="Added parameter to CMD")
        addCMD_checkbutton['fg'] = 'blue'
    else:
        messagelabel.config(text="Removed parameter from CMD")
        combobox.set(default_value)
        combobox.configure(state="readonly", foreground="black")
        label.config(fg="black")
        addCMD_checkbutton['fg'] = 'black'
        
def check_addtoCMD_checkbutton(messagelabel, addCMD_tick, addCMD_checkbutton, item_tick, item_checkbutton):
    if addCMD_tick.get() == 1:
        messagelabel.config(text="Added parameter to CMD")
        item_tick.set(True)
        item_checkbutton['fg'] = 'blue'
        addCMD_checkbutton['fg'] = 'blue'
    else:
        messagelabel.config(text="Removed parameter from CMD")
        item_tick.set(False)
        item_checkbutton['fg'] = 'black'
        addCMD_checkbutton['fg'] = 'black'
        
def open_explorer(messagelabel, path):
    if path != "":
        subprocess.Popen(f'explorer {path}', shell=True)
        messagelabel.config(text="Open File Explorer")
    else:
        messagelabel.config(text="Not found Directory")

