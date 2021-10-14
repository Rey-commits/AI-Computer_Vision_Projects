import os
from tqdm import tqdm

src_dir = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/splitted_dataset"

dst_dir = "/home/reymond/Documents/3.Machine_DeepLearning_Projects/12_Military_Aircraft_Detection/Military_Aircraft_Dataset/data_lists"

dsets = ["train", "valid", "test"]

for dset in dsets:
    print(dset)
    from_dir = os.path.join(src_dir, dset)
    textfile_name = "aircraft_" + dset + ".txt"
    with open(os.path.join(dst_dir, textfile_name), 'w+') as opened_file:
        for fname in tqdm(sorted(os.listdir(from_dir))):
            if fname[-4:] == ".jpg":
                opened_file.write(os.path.join(from_dir, fname) + "\n")
