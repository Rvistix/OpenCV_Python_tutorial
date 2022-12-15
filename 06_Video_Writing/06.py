# import the library
import cv2
import matplotlib.pyplot as plt


source = './race_car.mp4'  # source = 0 for webcam

cap = cv2.VideoCapture(source)
if cap.isOpened()== False:
    print("Error opening video stream or file")
ret, frame = cap.read()
plt.imshow(frame)
# from IPython.display import HTML
# HTML("""
# <video width=1024 controls>
#   <source src="race_car.mp4" type="video/mp4">
# </video>
# """)
# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.
out_avi = cv2.VideoWriter('race_car_out.avi',
                          cv2.VideoWriter_fourcc('M','J','P','G'),
                          10, (frame_width,frame_height))

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Write the frame to the output files
        out_avi.write(frame)

    # Break the loop
    else:
        break
plt.imshow(out_avi)
# When everything done, release the VideoCapture and VideoWriter objects
cap.release()
out_avi.release()
