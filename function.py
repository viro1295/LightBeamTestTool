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

def choosefolder_insertwidget(messagelabel, folderpath, dialogname, widget):
    messagelabel.config(text="Choose folder from computer")
    folderpath = filedialog.askdirectory(title=dialogname)
    widget.config(text=folderpath)
    
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
    
def show_tooltip(event, window, button, content):
    button.tooltip = tk.Toplevel(window)
    button.tooltip.wm_overrideredirect(True)
    button.tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
    
    label = ttk.Label(button.tooltip, text=content, background="yellow")
    label.pack()

def hide_tooltip(event, button):
    button.tooltip.destroy()

def create_batch_file(messagelabel, lightbeam, StringB, StringC):
    batch_content = '''@echo off
setlocal enabledelayedexpansion
set CSV_FILES=%1*.csv
for %%f in (%CSV_FILES%) do (
  for /f "tokens=1,2,3 delims=," %%a in (%%f) do (
    mkdir %%b
    rmdir /s /q %%b
    .\\{} decode -c %%a -r %%b %%c > %%b.txt
  )
)'''.format(lightbeam, StringB, StringC)
    with open('ExBatch.bat', 'w') as file:
        file.write(batch_content)
    messagelabel.config(text="Created ExBatch.bat file in current folder")
     

def create_single_cmd(messagelabel, lightbeam, configfile, resultfolder, imagefolder, log_tick, log, loglevel_tick, loglevel,  heap_memory_tick, heap_memory, stack_memory_tick, stack_memory, iteration_tick, iteration, disable_shortcuts_tick, threads_number_tick, threads_number, stop_after_tick, stop_after, slice_height_tick, slice_height, decode_timeout_tick, decode_timeout, instances_number_tick, instances_number, repeat_tick, repeat, verbose_tick):
    notify = ""
    if not lightbeam:
        notify += "Please choose LightBeam file!\n"
    if not configfile:
        notify += "Please choose configure file!\n"
    if not resultfolder:
        notify += "Please choose result folder!\n"
    if not imagefolder:
        notify += "Please choose image folder!\n"
    messagelabel.config(text=notify)

    if lightbeam and configfile and resultfolder and imagefolder:
        log_str = " -l " + log if log_tick.get() == 1 else ""
        loglevel_str = " --log_level " + loglevel if loglevel_tick.get() == 1 else ""
        heap_memory_str = " -m " + heap_memory if heap_memory_tick.get() == 1 else ""
        stack_memory_str = " --stack " + stack_memory if stack_memory_tick.get() == 1 else ""
        iteration_str = " -i " + iteration if iteration_tick.get() == 1 else ""
        disable_shortcuts_str = " --disable-shortcuts" if disable_shortcuts_tick.get() == 1 else ""
        threads_number_str = " --threads " + threads_number if threads_number_tick.get() == 1 else ""
        stop_after_str = " --stop_after_labels " + stop_after if stop_after_tick.get() == 1 else ""
        slice_height_str = " --progressive_slice_height " + slice_height if slice_height_tick.get() == 1 else ""
        decode_timeout_str = " --decode_timeout " + decode_timeout if decode_timeout_tick.get() == 1 else ""
        instances_number_str = " --mip " + instances_number if instances_number_tick.get() == 1 else ""
        repeat_str = " --repeat " + repeat if repeat_tick.get() == 1 else ""
        verbose_str = " -v" if verbose_tick.get() == 1 else ""

        single_cmd = ".\\" + lightbeam + " decode -c " + configfile + " -r " + resultfolder + log_str + loglevel_str + heap_memory_str + stack_memory_str + iteration_str + disable_shortcuts_str + threads_number_str + stop_after_str + slice_height_str + decode_timeout_str + instances_number_str + repeat_str + verbose_str + " " + imagefolder
        print(single_cmd)
        messagelabel.config(text="Created single CMD successfully")

def check_addtoCMD(messagelabel, tick, param_name, param_value):
    if tick.get() == 1:
        param_str = param_name + param_value 
        messagelabel.config(text="Added parameter to CMD")   
    else:
        param_str = ""
        messagelabel.config(text="Removed parameter from CMD")
    print(param_str)

##################EndChildFunction####################

