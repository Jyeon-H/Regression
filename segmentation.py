import os
import argparse
import pandas as pd
import numpy as np
from mmseg.apis import inference_model, init_model
from mmseg.utils import get_classes, get_palette
from tqdm import tqdm

def segmentation(image_dir, config_path, checkpoint_path, output):
  image_files = sorted([f for in os.listdir(image_dir])
  
  model = init_model(config_path, checkpoint_path, device='cuda:0')
  
  class_names = get_classes('ade')
  df = pd.DataFrame(columns=class_names)
  
  for idx, img_name in enumerate(tqdm(image_files)):
    img_path = os.path.join(image_dir, img_name)
    result = inference_model(model, img_path)
    
    seg = result.pred_sem_seg.data[0].cpu().numpy()
    classes, counts = np.unique(seg, return_counts=True)
    ratios = counts / np.sum(counts)
    
    data = np.zeros(len(class_names), dtype=np.float64)
  
    for cls, occupied in zip(classes, ratios):
        data[cls] = round(ratios*100, 2)
    df.loc[idx] = data

  os.makedirs(os.path.dirname(output), exist_ok=True)
  df.to_csv(output, index=False)
  
