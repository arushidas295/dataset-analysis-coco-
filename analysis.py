import os
import json
import numpy as np
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from PIL import Image
import requests
from io import BytesIO

# Path to COCO annotation file
annotation_file = 'annotations/captions_val2017.json'

coco = COCO(annotation_file)

# 1️⃣ Number of Images
image_ids = coco.getImgIds()
print("Total Images:", len(image_ids))

# 2️⃣ Load Categories
categories = coco.loadCats(coco.getCatIds())
print("Total Categories:", len(categories))

# 3️⃣ Caption Length Analysis
caption_lengths = []
ann_ids = coco.getAnnIds()
annotations = coco.loadAnns(ann_ids)

for ann in annotations:
    caption_lengths.append(len(ann['caption'].split()))

print("Average Caption Length:", np.mean(caption_lengths))

# 4️⃣ Display Image + Captions
img_id = image_ids[0]
img_info = coco.loadImgs(img_id)[0]
img_url = img_info['coco_url']

response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

plt.imshow(img)
plt.axis('off')

ann_ids = coco.getAnnIds(imgIds=img_id)
anns = coco.loadAnns(ann_ids)

print("\nCaptions:")
for ann in anns:
    print("-", ann['caption'])

plt.show()
