# Import libraries
import cv2
# %matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = (9.0, 9.0)

img = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
#
# plt.imshow(img[:,:,::-1])
plt.imshow(img)
plt.show()

img_line = img.copy()

cv2.line(img_line, (200, 100), (400, 100), (0, 0, 0),
         thickness=5, lineType=cv2.LINE_AA)

plt.imshow(img_line)

plt.show()
img_circle = img.copy()

cv2.circle(img_circle, (300, 300), 200, (0,0,0),
           thickness=5, lineType=cv2.LINE_AA)

plt.imshow(img_circle)

plt.show()

img_rect = img.copy()

cv2.rectangle(img_rect, (500, 100), (700,600),
              (255, 0, 255), thickness=5, lineType=cv2.LINE_8);

plt.imshow(img_rect)

plt.show()
imageText = img.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);

# Display the image
plt.imshow(imageText[:,:,::-1])

plt.show()
