import subprocess
import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog

################GenerateFunctions######################

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