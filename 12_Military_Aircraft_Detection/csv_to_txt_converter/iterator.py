import glob
import csv_to_txt
import os
import sys
sys.path.insert(
    1, '/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/csv_to_txt_converter')

out_dir = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/output_txt"


path = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/cvs_files/*.csv"
for fname in glob.glob(path):
    csv_to_txt.csv_to_txt(fname, out_dir)
