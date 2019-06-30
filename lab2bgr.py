#lab to bgr test
import numpy as np
import cv2



lab = cv2.cvtColor( np.uint8([[(0,0,0)]] ), cv2.COLOR_BGR2LAB)

rgb = cv2.cvtColor( lab , cv2.COLOR_LAB2BGR)[0][0]

print(rgb)







