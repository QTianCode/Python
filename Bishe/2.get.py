# 开发者 : 晴天
# 开发日期 : 2023/4/18

import cv2
from imWatermark import WatermarkDecoder

bgr = cv2.imread('songyun_wm.png')

decoder = WatermarkDecoder('bytes', 32)
watermark = decoder.decode(bgr, 'dwtDct')
print(watermark.decode('utf-8'))
