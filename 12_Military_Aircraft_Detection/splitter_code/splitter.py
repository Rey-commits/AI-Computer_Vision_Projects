import os
from glob import glob
import shutil
from sklearn.model_selection import train_test_split

# getting list of images
# must be the same as source_dir path below
image_files = glob(
    "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/splitted_dataset/valid+test/*jpg")

# replacing the extension
images = [name.replace(".jpg", "") for name in image_files]

# splitting the dataset
train_names, test_names = train_test_split(images, test_size=0.5)


def batch_move_files(file_list, source_path, destination_path):
    for file in file_list:
        # extracting only the name of the file and concatenating with extenions
        image = file.split('\\')[-1] + '.jpg'
        txt = file.split('\\')[-1] + '.txt'
        shutil.move(os.path.join(source_path, image), destination_path)
        shutil.move(os.path.join(source_path, txt), destination_path)
    return


source_dir = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/splitted_dataset/valid+test/"
train_dir = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/splitted_dataset/valid/"
test_dir = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/splitted_dataset/test/"

batch_move_files(train_names, source_dir, train_dir)
batch_move_files(test_names, source_dir, test_dir)
