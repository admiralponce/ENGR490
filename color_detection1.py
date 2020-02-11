import cv2
import numpy as np
frame = cv2.imread('basictest2.png')
height, width = frame.shape[:2]
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
low = np.array([0, 42, 0])
high = np.array([179, 255, 255])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)
pos_x = int(width/2)
start_y = int(height/2)
end_y = height
colors = []
last_color = []
for pos_y in range(start_y, end_y):
    color = result[pos_y, pos_x]
    colors.append(color)
for out_color in colors:
    if out_color[0] != 0 and out_color[1] != 0 and out_color[2] != 0:
        last_color.append(out_color)
position = len(last_color)/2
print(last_color[int(position)])
cv2.waitKey(0)
