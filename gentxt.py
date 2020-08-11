import os
import sys
import cv2
import numpy as np
from scipy import misc
import glob
from tqdm import tqdm

img_list = glob.glob(os.path.join("images", "*.{}".format("jpg")))
print(len(img_list))
trainval = open('segmentation/trainval.txt', 'w')
train = open('segmentation/train.txt', 'w')
val = open('segmentation/val.txt', 'w')
for i in tqdm(range(len(img_list))):
  name = os.path.basename(img_list[i]).split(".")[0]
  trainval.write("%s\n" % name)

for i in tqdm(range(len(img_list) - 200)):
  name = os.path.basename(img_list[i]).split(".")[0]
  train.write("%s\n" % name)

for i in tqdm(range(len(img_list) - 200, len(img_list))):
  name = os.path.basename(img_list[i]).split(".")[0]
  val.write("%s\n" % name)
