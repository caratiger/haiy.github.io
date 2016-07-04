---
layout: post
---

{{ page.title }}
================
<p class="meta">04 July 2015 </p>
将kaggle上的[超声波识别比赛](https://www.kaggle.com/c/ultrasound-nerve-segmentation)的神经组织mask合并到原始的
超声波图片上。
原始的图片如下：

<img src="{{site.url}}/images/1_1.png"  height="200px" width="200px">

'''python
import matplotlib.pyplot as plt
import cv2
import numpy as np

img = plt.imread("1_1.tif")
mask = plt.imread("1_1_mask.tif")
img_color = np.dstack([img, img, img])
mask_pix = cv2.Canny(mask,200,100) > 0
img_color[mask_pix, 0] = 255
img_color[mask_pix, 1] = 255
img_color[mask_pix, 2] = 255
plt.imshow(img_color)
plt.show()
'''



