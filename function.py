# import subprocess
import tkinter as tk
from tkinter import ttk, filedialog

################ChildFunction######################


def choosefile_insertwidget(messagelabel, filepath, dialogname, widget):
    messagelabel.config(text="Choose file from computer")
    filepath = filedialog.askopenfilename(title=dialogname)
    if isinstance(widget, tk.Label):
        widget.config(text=filepath)
    elif isinstance(widget, tk.Entry):
        widget.delete(0, tk.END)
        widget.insert(0, filepath)

def setstate_combobox(messagelabel, event, combobox):
    messagelabel.config(text="Set value for parameter")
    if combobox.get() == "Other":
        combobox.set("")
        combobox.config(state="normal")
    else:
        combobox.config(state="readonly")
        
def toggle_widgetstate(messagelabel, tick, *widgets):
    if tick.get() == 1:
        messagelabel.config(text="NORMAL state has been set")
        for widget in widgets:
            widget.config(state=tk.NORMAL)
    else:
        messagelabel.config(text="DISABLED state has been set")
        widgets[0].delete(0, tk.END)
        for widget in widgets:
            widget.config(state=tk.DISABLED)

def select_unselect(messagelabel, tick, tickinfo, untickinfo):
    if tick.get() == 1:
        messagelabel.config(text="Checked parameter")
        print(tickinfo)
    else:
        messagelabel.config(text="Unchecked parameter")
        print(untickinfo)

def create_batch_file(messagelabel, StringA, StringB, StringC):
    batch_content = '''@echo off
setlocal enabledelayedexpansion
set CSV_FILES=%1*.csv
for %%f in (%CSV_FILES%) do (
  for /f "tokens=1,2,3 delims=," %%a in (%%f) do (
    mkdir %%b
    rmdir /s /q %%b
    .\\Lightbeam.exe {} -c %%a -v -r %%b -l %%b.json {} {} %%c > %%b.txt
  )
)'''.format(StringA, StringB, StringC)
    with open('ExBatch.bat', 'w') as file:
        file.write(batch_content)
    messagelabel.config(text="Created ExBatch.bat file in current folder")

def add_string(messagelabel, *args):
    result_string = ''.join(args)
    messagelabel.config(text="Added to result string")
    print(result_string)
    # subprocess.Popen('start cmd', shell=True)

def document_function(messagelabel, window):
    messagelabel.config(text="Show command syntax usage")
    documentwindow = tk.Toplevel(window)
    documentwindow.title("Usage")
    documentwindow.iconbitmap(".\\icon\\document_icon.ico")
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
    aboutwindow.iconbitmap(".\\icon\\about_icon.ico")
    aboutwindow.geometry("300x30")
    about_label = tk.Label(aboutwindow, text="LightBeam test tool v.1.0.1")
    about_label.pack()
    

##################EndChildFunction####################

