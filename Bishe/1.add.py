# 开发者 : 晴天
# 开发日期 : 2023/4/17
import cv2
from imWatermark import WatermarkEncoder

bgr = cv2.imread('songyun.jpg')
wm = 'test'

encoder = WatermarkEncoder()
encoder.set_watermark('bytes', wm.encode('utf-8'))
bgr_encoded = encoder.encode(bgr, 'dwtDct')

cv2.imwrite('dddd_wm.png', bgr_encoded)