import cv2
import matplotlib.pyplot as plt

version = cv2.__version__

print(version)

image_1 = cv2.imread("New_Zealand_Lake.jpg")
image_2 = cv2.imread("coca-cola-logo.png")


plt.imshow(image_1)
plt.title("image_4")
plt.show()


plt.imshow(image_2)

