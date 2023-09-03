import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

################ChildFunction######################

def choosefile_insertwidget(filepath, dialogname, widget):
    filepath = filedialog.askopenfilename(title=dialogname)
    if isinstance(widget, tk.Label):
        widget.config(text=filepath)
    elif isinstance(widget, tk.Entry):
        widget.delete(0, tk.END)
        widget.insert(0, filepath)

def setstate_combobox(event, combobox):
    if combobox.get() == "Other":
        combobox.set("")
        combobox.config(state="normal")
    else:
        combobox.config(state="readonly")

def toggle_widgetstate(tick, *widgets):
    if tick.get() == 1:
        for widget in widgets:
            widget.config(state=tk.NORMAL)
    else:
        widgets[0].delete(0, tk.END)
        for widget in widgets:
            widget.config(state=tk.DISABLED)

def select_unselect(tick, tickinfo, untickinfo):
    if tick.get() == 1:
        print(tickinfo)
    else:
        print(untickinfo)

def create_batch_file(StringA, StringB, StringC):
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

def create_single_cmd(lightbeam, configfile, resultfolder, imagefolder):
    single_cmd = ".\\" + lightbeam + " decode -c " + configfile + " -v -r " + resultfolder + " " + imagefolder
    print(single_cmd)

def add_string(*args):
    result_string = ''.join(args)
    print(result_string)
    # subprocess.Popen('start cmd', shell=True)



##################EndChildFunction####################

