import os
import sys
import cv2
import numpy as np
from scipy import misc
import glob
from tqdm import tqdm

img_list = glob.glob(os.path.join("images", "*.{}".format("jpg")))
mask_list = glob.glob(os.path.join("masks", "*.{}".format("png")))
sorted(img_list)
sorted(mask_list)
MAX_DIM = 1536

print(len(img_list))
for i in tqdm(range(len(img_list))):
	org_I = cv2.imread(img_list[i])
	name = os.path.basename(img_list[i]).split(".")[0]
	maskP = "masks/"+name+".png"
	print(img_list[i])
	print(maskP)
	org_M = cv2.imread(maskP)
	orgH = org_I.shape[0]
	orgW = org_I.shape[1]
	org_M = cv2.resize(org_M, (int(orgW), int(orgH)))
	
	cv2.imwrite(maskP,org_M)

	# ratio = orgH/orgW
	# if (orgW > orgH):
	# 	if (orgW > MAX_DIM):
	# 		print(img_list[i])
	# 		newW = MAX_DIM
	# 		newH = MAX_DIM * orgH / orgW
	# 		org_I = cv2.resize(org_I, (int(newW), int(newH)))
	# 		org_M = cv2.resize(org_M, (int(newW), int(newH)))
	# 		cv2.imwrite(img_list[i],org_I)
	# 		cv2.imwrite(mask_list[i],org_M)
	# else:
	# 	if (orgH > MAX_DIM):
	# 		newH = MAX_DIM
	# 		newW = MAX_DIM * orgW / orgH
	# 		org_I = cv2.resize(org_I, (int(newW), int(newH)))
	# 		org_M = cv2.resize(org_M, (int(newW), int(newH)))
	# 		cv2.imwrite(img_list[i],org_I)
	#		cv2.imwrite(mask_list[i],org_M)

