import cv2

video = cv2.VideoCapture(0)
name = 'camera'
cv2.namedWindow(name, cv2.WINDOW_NORMAL)

bool = True


while cv2.waitKey(1) != 27 and bool:
    frame_b, frame = video.read()
    if not frame_b:
        break
    cv2.imshow(name, frame)
    if not input() == '':
        break

video.release()
cv2.destroyWindow(name)

