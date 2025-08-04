import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8)
cv2.line(canvas, (0,0), (511,511), (25,255,0),5) #(x,y), (b,g,r), thickness
cv2.rectangle(canvas, (384,0),(510,128),(255,0,0),-1)
cv2.putText(canvas,"OpenCV Text Addition",(10,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow("Work of Art", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
