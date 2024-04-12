import os
import glob
import time

directory = "runs/detect"

while True:
    dirs = glob.glob(os.path.join(directory, "*"))
    if dirs:
        latest_dir = max(dirs, key=os.path.getctime)
        labels_dir = os.path.join(latest_dir, "labels")
        files = glob.glob(os.path.join(labels_dir, "*.txt"))
        if files:
            latest_file = max(files, key=os.path.getmtime)
            count = 0
            with open(latest_file, "r") as file:
                for line in file:
                    if line.strip():
                        if line[0] == '1' or line[0] == '0':
                            count += 1
            if count == 9:
                print("chdoula ya m3alem")
            else:
                print("chdoula ya m3alem ama mch 7aba")
            for f in files[:-1]:
                os.remove(f)
    time.sleep(1)
