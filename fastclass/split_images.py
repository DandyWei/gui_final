
from pathlib import Path
# import TronGisPy as tgp
import numpy as np
from PIL import Image as im
import cv2
from matplotlib import cm

# splitedimages =   r'D:\Thinktron\fastclass\input_data\test_001_000_001.tif'



def tiff_2_png(img_fp):
    img_split = tgp.read_raster(img_fp).data
    image = cv2.cvtColor(img_split,cv2.COLOR_RGB2BGR)
    cvuint8 = cv2.convertScaleAbs(image , alpha=(255.0/img_split.max()))
    data = im.fromarray(cvuint8)
    data.save(img_fp[:-3] + 'png')

def read_npy(img_fp):
    x = np.load(img_fp)
    x = x[:, :2]



if __name__ == "__main__":
    path = Path('D:/Thinktron/gui/fastclass/npy_data/071022h_51_0375_957_031_027.npy')
    x = np.load(path)
    x = x[:, :, :3]
    norm_image = cv2.normalize(x, None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
    img = im.fromarray(norm_image.astype('uint8'), 'RGB')
    img.show()

    # img.thumbnail(size, Image.ANTIALIAS)

    # img = im.open(path)
