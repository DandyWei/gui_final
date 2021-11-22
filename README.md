"# Easy_Forest_GUI_py"
## 20211109

- Clone ffc and change cls

> fc_clean.py


- Conver tiff 2
> split_images.py

```python
img_split = tgp.read_raster(img_fp).data
image = cv2.cvtColor(img_split,cv2.COLOR_RGB2BGR)
cvuint8 = cv2.convertScaleAbs(image , alpha=(255.0/img_split.max()))
data = im.fromarray(cvuint8)
data.save(img_fp[:-3] + 'png')
```
### 邏輯
1. 先用TronGispy讀取圖片 (因為也是用TronGisPy切的)
2. CV轉成BGR (原本是RGB array)
3. normalize成Int8
> 這裡不能用 2^8 / 2^16 normalize
4. 存下來

# 211112
## Done:
#### 1.GUI for label images and save result
> #### fc_clean.py
#### 2.GUI for split、predict、combine
> #### first garbage.py

## Future works

#### 1. tif to png
#### 2. multi-label
#### 3. compare with npy and modify it
