import subprocess
import os
import shutil
import csv
import tkinter as tk
from tkinter import ttk, filedialog
import xml.etree.ElementTree as ET
import re

################GenerateFunctions######################

# TẠO CSV TestSuite - Windows
def create_csv_testsuite(messagelabel):
	fileload = filedialog.askopenfilename(title="Choose file VL5.load").replace("/","\\")
	vlconfigfolder = filedialog.askdirectory(title="Choose VL configure folder").replace("/","\\")
	itcimagefolder = filedialog.askdirectory(title="Choose itc-imagefolder").replace("/","\\")
	savefolder = filedialog.askdirectory(title="Choose folder to save CSV testsuite").replace("/","\\")
	testresultfolder = filedialog.askdirectory(title="Choose folder contain test results").replace("/","\\")
	
	print(fileload)
	print(savefolder)
	print(vlconfigfolder)
	print(testresultfolder)
	print(itcimagefolder)

	if fileload != "" and savefolder != "" and vlconfigfolder != "" and testresultfolder != "" and itcimagefolder:
		messagelabel.config(text="Creating...")

		# Mở tệp XML
		tree = ET.parse(fileload)
		root = tree.getroot()

		# Tìm các thẻ cần sao chép dữ liệu
		for symbol in root.findall('.//symbology'):
			# Dùng regex định dạng lại tên file từ content thẻ Symbology
			codename = re.sub(r'[- \t\n]+', '_', symbol.text).rstrip("_")
			filename = savefolder + "\\" + codename + '.csv'

			content = ""
			for test_case in symbol.findall('.//TestCase'):
				VLC = test_case.find('VLC_Path').text
				TCID = test_case.find('ExpectResultID').text
				ITC = test_case.find('Img_Path').text
				
				VLC_Edit = VLC.replace("Functional_Testing\\VL5_Configuration", vlconfigfolder + "\\Functional_Testing\\VL5_Configuration")
				TCID_Edit = testresultfolder + "\\" + codename + "\\" + TCID 
				ITC_Edit =  itcimagefolder + "\\" + ITC.split("\\")[-1].replace(".itc","")

				row = VLC_Edit + "," + TCID_Edit + "," + ITC_Edit + "\n"
				content = content + row

			# Tạo tệp mới và ghi dữ liệu vào đó
			with open(filename, 'w') as f:
				f.write(content)
		messagelabel.config(text="Created CSV TestSuite successfully")

	else:
		messagelabel.config(text="Not enough input data to create CSV TestSuite")


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
		file_path = filedialog.asksaveasfilename(defaultextension=".bat")
		if file_path:
			with open(file_path, 'w') as file:
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

def save_settings(messagelabel, lightbeam, configfile, resultfolder, imagefolder):
	file_path = filedialog.asksaveasfilename(defaultextension=".csv")
	if file_path:
		with open(file_path, 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([lightbeam, configfile, resultfolder, imagefolder])
		messagelabel.config(text="Save Settings information")

def load_settings(messagelabel, lightbeam, configfile, resultfolder, imagefolder):
	file_path = filedialog.askopenfilename()
	if file_path:
		with open(file_path, 'r') as file:
			reader = csv.reader(file)
			for row in reader:
				lightbeam.config(text = row[0])
				configfile.config(text = row[1])
				resultfolder.config(text = row[2])
				imagefolder.config(text = row[3])
		messagelabel.config(text="Load Settings information")

def compare_results(messagelabel):
	file_path = filedialog.asksaveasfilename(defaultextension=".csv")
	messagelabel.config(text="Comparing...")
	if file_path:
		vl1_results_folder = filedialog.askdirectory(title="Choose TestResults folder of VL1").replace("/","\\")
		vl2_results_folder = filedialog.askdirectory(title="Choose TestResults folder of VL2").replace("/","\\")

		result_string = "CODE,TCID,ConfigureFile,Image,NumberOfDecoded1,NumberOfDecoded2,ProcessingTime1,ProcessingTime2,DecodeTime1,DecodeTime2,Symbology1,Symbology2,Content1,Content2,LabelIndex,ErrorType\n"

		# Thư mục và thư mục con chứa xml files
		for dirpath, dirnames, filenames in os.walk(vl1_results_folder):
			for filename in filenames:
				if filename.endswith('.xml'):
					code = dirpath.split("\\")[-1]
					TCID = filename.split(".")[0]
					# print(filename,dirpath,code,TCID)

					# Đọc dữ liệu từ 2 file XML
					tree1 = ET.parse(vl1_results_folder+"\\"+code+"\\"+filename)
					root1 = tree1.getroot()
					tree2 = ET.parse(vl2_results_folder+"\\"+code+"\\"+filename)
					root2 = tree2.getroot()

					for sequence_result1 in root1.findall('.//SequenceResult'):
						img_string1 = sequence_result1.find('.//string').text
						cfg_string1 = sequence_result1.find('ConfigurationFile').text
						num_result1 = len(sequence_result1.findall('.//Result'))
						num_result1_str = str(num_result1)
						for sequence_result2 in root2.findall('.//SequenceResult'):
							img_string2 = sequence_result2.find('.//string').text
							cfg_string2 = sequence_result2.find('ConfigurationFile').text
							num_result2 = len(sequence_result2.findall('.//Result'))
							num_result2_str = str(num_result2)

							# Kiểm tra nếu hình giống nhau ở 2 file thì so sánh các chỉ số
							if img_string2 == img_string1:
								if num_result1 == num_result2:
									if num_result1 > 0:
										for i in range(1,num_result1+1):
											label_index_str_tmp = str(i-1)
											# Khởi tạo kq rỗng1
											processing_time1_tmp = ""
											decode_time1_tmp = ""
											symbology1_tmp = ""
											content_in_hexadecimal1_tmp = ""
											# Khởi tạo kq rỗng2
											processing_time2_tmp = ""
											decode_time2_tmp = ""
											symbology2_tmp = ""
											content_in_hexadecimal2_tmp = ""

											# Lấy thông số từ file 1 để so sánh
											processing_time1 = sequence_result1.find('ProcessingTime').text
											decode_time1 = sequence_result1.find(f'.//Result[{i}]/DecodeTime').text
											symbology1 = sequence_result1.find(f'.//Result[{i}]/Symbology').text
											content_in_hexadecimal1 = sequence_result1.find(f'.//Result[{i}]/ContentInHexadecimal').text
											# Lấy thông số từ file 2 để so sánh
											processing_time2 = sequence_result2.find('ProcessingTime').text
											decode_time2 = sequence_result2.find(f'.//Result[{i}]/DecodeTime').text
											symbology2 = sequence_result2.find(f'.//Result[{i}]/Symbology').text
											content_in_hexadecimal2 = sequence_result2.find(f'.//Result[{i}]/ContentInHexadecimal').text

											note_tmp = ""

											# So sánh
											if (float(processing_time2)-float(processing_time1))/(float(processing_time1)+float(processing_time2)) > 0.2:
												processing_time1_tmp = str(round(float(processing_time1), 2))
												processing_time2_tmp = str(round(float(processing_time2), 2))
												note_tmp += "ProcessingTime."
											if (float(decode_time2)-float(decode_time1))/(float(decode_time1)+float(decode_time2)) > 0.2:
												decode_time1_tmp = str(round(float(decode_time1), 2))
												decode_time2_tmp = str(round(float(decode_time2), 2))
												note_tmp += "DecodeTime."
											if symbology1 != symbology2:
												symbology1_tmp = symbology1 
												symbology2_tmp = symbology2 
												note_tmp += "Symbology."
											if content_in_hexadecimal1 != content_in_hexadecimal2:
												content_in_hexadecimal1_tmp = content_in_hexadecimal1 
												content_in_hexadecimal2_tmp = content_in_hexadecimal2
												note_tmp += "Content."

											#Nối chuỗi kết quả
											if processing_time1_tmp != "" or processing_time2_tmp != "" or decode_time1_tmp != "" or decode_time2_tmp != "" or symbology1_tmp != "" or symbology2_tmp != "" or content_in_hexadecimal1_tmp != "" or content_in_hexadecimal2_tmp != "":
												result_string = result_string + code + "," + TCID + "," + cfg_string1 + ","+ img_string1 + ",,," + processing_time1_tmp + "," + processing_time2_tmp + "," + decode_time1_tmp + "," + decode_time2_tmp + "," + symbology1_tmp + "," + symbology2_tmp + "," + content_in_hexadecimal1_tmp + "," + content_in_hexadecimal2_tmp + "," + label_index_str_tmp + "," + note_tmp +"\n"
					
									else:
										processing_time1_tmp = ""
										processing_time2_tmp = ""

										# Lấy thông số để so sánh
										processing_time1 = sequence_result1.find('ProcessingTime').text
										processing_time2 = sequence_result2.find('ProcessingTime').text
										# So sánh
										if (float(processing_time2)-float(processing_time1))/(float(processing_time1)+float(processing_time2)) > 0.2:
											processing_time1_tmp = str(round(float(processing_time1), 2))
											processing_time2_tmp = str(round(float(processing_time2), 2))
										#Nối chuỗi kết quả
										if processing_time1_tmp != "" or processing_time2_tmp != "":
											result_string = result_string + code + "," + TCID + "," + cfg_string1 + ","+ img_string1 + ",,," + processing_time1_tmp + "," + processing_time2_tmp + ",,,,,,,,ProcessingTime\n"

								else:
									result_string = result_string + code + "," + TCID + "," + cfg_string1 + ","+ img_string1 + "," + num_result1_str + "," + num_result2_str + ",,,,,,,,,,NumberOfDecoded\n"
		# Tạo file kết quả và ghi dữ liệu vào đó
		with open(file_path, 'w') as f:
			f.write(result_string)
		messagelabel.config(text="Comparison completed")



