import subprocess
import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog

################ChildFunction######################

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

def create_batch_file(messagelabel, lightbeam, hog_tick, hog, log_tick, log, loglevel_tick, loglevel,  heap_memory_tick, heap_memory, stack_memory_tick, stack_memory, iteration_tick, iteration, disable_shortcuts_tick, threads_number_tick, threads_number, stop_after_tick, stop_after, slice_height_tick, slice_height, decode_timeout_tick, decode_timeout, instances_number_tick, instances_number, repeat_tick, repeat, verbose_tick):
    if not lightbeam:
        messagelabel.config(text="Please choose LightBeam file!")
    else:
        hog_str = " -t " + hog if hog_tick.get() == 1 else ""
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
        sub_param_str = hog_str + log_str + loglevel_str + heap_memory_str + stack_memory_str + iteration_str + disable_shortcuts_str + threads_number_str + stop_after_str + slice_height_str + decode_timeout_str + instances_number_str + repeat_str + verbose_str

        batch_content = '''@echo off
setlocal enabledelayedexpansion
set CSV_FILES=%1*.csv
for %%f in (%CSV_FILES%) do (
  for /f "tokens=1,2,3 delims=," %%a in (%%f) do (
    mkdir %%b
    rmdir /s /q %%b
    .\\{} decode -c %%a -r %%b{} %%c > %%b.txt
  )
)'''.format(lightbeam, sub_param_str)
        with open('ExBatch.bat', 'w') as file:
            file.write(batch_content)
        messagelabel.config(text="Created ExBatch.bat file in current folder")
     

def execute_single_cmd(messagelabel, lightbeam, configfile, resultfolder, imagefolder, hog_tick, hog, log_tick, log, loglevel_tick, loglevel,  heap_memory_tick, heap_memory, stack_memory_tick, stack_memory, iteration_tick, iteration, disable_shortcuts_tick, threads_number_tick, threads_number, stop_after_tick, stop_after, slice_height_tick, slice_height, decode_timeout_tick, decode_timeout, instances_number_tick, instances_number, repeat_tick, repeat, verbose_tick):
    lightbeam_exceptname = lightbeam.rsplit("/", 1)[0] + "/"
    lightbeam_name = lightbeam.split("/")[-1]
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
        hog_str = " -t " + hog if hog_tick.get() == 1 else ""
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
        sub_param_str = hog_str + log_str + loglevel_str + heap_memory_str + stack_memory_str + iteration_str + disable_shortcuts_str + threads_number_str + stop_after_str + slice_height_str + decode_timeout_str + instances_number_str + repeat_str + verbose_str

        single_cmd = ".\\" + lightbeam_name + " decode -c " + configfile + " -r " + resultfolder + sub_param_str + " " + imagefolder + " >> cmd_output.txt"
        print(single_cmd)
        directory = lightbeam_exceptname.replace("/","\\")

        with open(lightbeam_exceptname + 'cmd_output.txt', 'w') as file:
            file.write(single_cmd + "\n")

        subprocess.call(single_cmd, cwd=directory, shell=True)
        messagelabel.config(text="Run single CMD successfully")

def save_settings(messagelabel, lightbeam, configfile, resultfolder, imagefolder, hog_tick, hog, log_tick, log, loglevel_tick, loglevel,  heap_memory_tick, heap_memory, stack_memory_tick, stack_memory, iteration_tick, iteration, disable_shortcuts_tick, threads_number_tick, threads_number, stop_after_tick, stop_after, slice_height_tick, slice_height, decode_timeout_tick, decode_timeout, instances_number_tick, instances_number, repeat_tick, repeat, verbose_tick):
    hog_str = " -t " + hog if hog_tick.get() == 1 else ""
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
    sub_param_str = hog_str + log_str + loglevel_str + heap_memory_str + stack_memory_str + iteration_str + disable_shortcuts_str + threads_number_str + stop_after_str + slice_height_str + decode_timeout_str + instances_number_str + repeat_str + verbose_str
    settings_str = lightbeam + configfile + resultfolder + sub_param_str + " " + imagefolder  
    with open('Settings.txt', 'w') as file:
        file.write(settings_str)
    print(settings_str)
    messagelabel.config(text="Save all settings in Settings.txt file")

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
        

##################EndChildFunction####################

