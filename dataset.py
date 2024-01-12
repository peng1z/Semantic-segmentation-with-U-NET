import os
from PIL import Image
from torch.utils.data import Dataset
import numpy as np

class MyDataset(Dataset):
    def __init__(self, img_dir, mask_dir, transforms=None):
        self.img_dir = img_dir
        self.mask_dir = mask_dir
        self.transforms = transforms
        self.imgs = os.listdir(img_dir)
    
    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, index):
        img_path = os.path.join(self.img_dir, self.imgs[index])
        mask_path = os.path.join(self.mask_dir, self.imgs[index].replace(".jpg", "_mask.gif"))
        img = np.array(Image.open(img_path).convert("RGB"))
        mask = np.array(Image.open(mask_path).convert("L"), dtype=np.float32)
        mask[mask == 255.0] = 1.0

        if self.transforms is not None:
            augmentations = self.transforms(image=img, mask=mask)
            img = augmentations["image"]
            mask = augmentations["mask"]

        return img, mask