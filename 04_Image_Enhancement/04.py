# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# %matplotlib inline
from IPython.display import Image

# img_bgr = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
#
# # Display 18x18 pixel image.
# Image(filename='New_Zealand_Coast.jpg')
#
# matrix = np.ones(img_rgb.shape, dtype="uint8") * 50
#
# img_rgb_brighter = cv2.add(img_rgb, matrix)
# img_rgb_darker = cv2.subtract(img_rgb, matrix)
#
# # Show the images
# plt.figure(figsize=[18, 5])
# plt.subplot(131);
# plt.imshow(img_rgb_darker);
# plt.title("Darker");
# plt.subplot(132);
# plt.imshow(img_rgb);
# plt.title("Original");
# plt.subplot(133);
# plt.imshow(img_rgb_brighter);
# plt.title("Brighter");
# plt.show()
#
# #
#
# matrix1 = np.ones(img_rgb.shape) * .8
# matrix2 = np.ones(img_rgb.shape) * 1.2
#
# img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))
#
# img_rgb_brighter = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix2), 0, 255))
#
# # Show the images
# plt.figure(figsize=[18,5])
# plt.subplot(131); plt.imshow(img_rgb_darker);  plt.title("Lower Contrast");
#
# plt.subplot(132); plt.imshow(img_rgb);         plt.title("Original");
#
# plt.subplot(133); plt.imshow(img_rgb_brighter);plt.title("Higher Contrast");
# plt.show()
#
#
# #
#
# img_read = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)
# retval, img_thresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)
#
# # Show the images
# plt.figure(figsize=[18,5])
# plt.subplot(121); plt.imshow(img_read, cmap="gray");         plt.title("Original");
# plt.subplot(122); plt.imshow(img_thresh, cmap="gray");       plt.title("Thresholded");
# plt.show()
#
# print(img_thresh.shape)
#
# #
#
# img_music = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)
#
# _music = cv2.adaptiveThreshold(img_music, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                                cv2.THRESH_BINARY, 11, 7)
#
# plt.figure(figsize=[18,5])
# plt.subplot(121); plt.imshow(img_music); plt.title("OG")
# plt.subplot(122); plt.imshow(_music);    plt.title("Modified")
# plt.show()
#

# Bitwise Operation
#
# img_rec = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
#
# img_cir = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)
#
# plt.figure(figsize=[20,5])
# plt.subplot(121);plt.imshow(img_rec,cmap='gray')
# plt.subplot(122);plt.imshow(img_cir,cmap='gray')
# print(img_rec.shape)
#
# result = cv2.bitwise_and(img_rec, img_cir, mask = None)
# plt.imshow(result,cmap='gray')
#
# result = cv2.bitwise_or(img_rec, img_cir, mask = None)
# plt.imshow(result,cmap='gray')
#
# result = cv2.bitwise_xor(img_rec, img_cir, mask = None)
# plt.imshow(result,cmap='gray')

img_front = cv2.imread("coca-cola-logo.png")

img_back = cv2.imread("checkerboard_color.png")

img_back = cv2.resize(img_back, (700, 700))

mask = cv2.cvtColor(img_front, cv2.COLOR_RGB2GRAY)

retval, mask = cv2.threshold(mask, 45,  255, cv2.THRESH_BINARY)


maskINV = cv2.bitwise_not(mask)

img_back = cv2.bitwise_and(img_back, img_back, mask=mask)

img_back = cv2.bitwise_not(img_back)

result = cv2.bitwise_and(img_back, img_front)



# d = cv2.bitwise_and(img_front, img_back, mask=mask)


cv2.imshow("front", result)
cv2.imshow("PICTURE", img_front)
cv2.imshow("back", img_back)

cv2.waitKey()


result = cv2.add(mask, img_back)

