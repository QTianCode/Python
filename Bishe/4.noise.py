"""
  作者：LCQT
  日期：2023年05月19日15:35
  项目描述：
"""
"""
功能：添加噪声
"""
import cv2
import numpy as np
#读取图片
image = cv2.imread('test.jpg')

#给图片添加泊松噪声，lam的值越大，添加的噪声越多
noisy_type=np.random.poisson(lam=3,size=image.shape(arr)).astype(dtype='uint8')
noisy_img = noisy_type + image

imgs = np.hstack([image,noisy_img])
cv2.namedWindow('imgs', cv2.WINDOW_NORMAL)
cv2.imshow("imgs",imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()