import os
import sys
import cv2
import numpy as np
import glob
from tqdm import tqdm
import os.path
from os import path

img_list = glob.glob(os.path.join("images", "*.{}".format("jpg")))

for i in tqdm(range(len(img_list))):
	#print(os.path.basename(img_list[i]).split(".")[0])
	if (path.exists('masks/'+os.path.basename(img_list[i]).split(".")[0]+".png") == False):
		print(img_list[i])
		os.remove(img_list[i])
		print(path.exists('masks/'+os.path.basename(img_list[i]).split(".")[0]+".png"))


img_list = glob.glob(os.path.join("masks", "*.{}".format("png")))

for i in tqdm(range(len(img_list))):
	#print(os.path.basename(img_list[i]).split(".")[0])
	if (path.exists('images/'+os.path.basename(img_list[i]).split(".")[0]+".jpg") == False):
		print(img_list[i])
		os.remove(img_list[i])
		print(path.exists('images/'+os.path.basename(img_list[i]).split(".")[0]+".jpg"))		