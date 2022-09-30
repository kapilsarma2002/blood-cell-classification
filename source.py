import pandas as pd
import numpy as np
import json

# df = pd.read_json('./images/train/_annotations.coco.json')
category_id_map = {}
image_id_map = {}
required_data = []

category_id_map[0] = 'None'
category_id_map[1] = 'Platelets'
category_id_map[2] = 'RBC'
category_id_map[3] = 'WBC'

with open('./images/train/_annotations.coco.json') as f:
  data = json.load(f)

annotations = data['annotations']
images = data['images']

for image in images:
  image_id_map[image['id']] = image['file_name']

for a in annotations:
  l = []
  l.append(image_id_map[a['image_id']])
  l.append(a['bbox'])
  l.append(category_id_map[a['category_id']])
  required_data.append(l)
  # print(l)

df = pd.DataFrame(required_data)
df.to_csv('train_data.csv')
print(df.head())