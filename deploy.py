import os
import sys

original_stdout = sys.stdout
original_stderr = sys.stderr

sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')
from ultralytics import YOLO
model=YOLO('cc.pt')
pred=model.predict(source="0", save=True,show=True,conf=0.5,save_txt=True)
