import cv2
import sys

image = cv2.imread("carro.jpg")
width_original = image.shape[0]
height_original = image.shape[1]

val1 = round(width_original / int(sys.argv[1]))
val2 = round(height_original / int(sys.argv[1]))
desired_shape = [val1,val2]



y_min = 0
x_min = 0
y_max= desired_shape[0]
x_max= desired_shape[1]
predict_batch = []

nmbr = 0

while (x_max + desired_shape[1]) < height_original:
    while (y_max + desired_shape[0]) < width_original:
        crop = image[y_min:y_max, x_min:x_max]

        cv2.imwrite("imgs/" + str(nmbr) + ".jpg", crop)
        nmbr += 1

        y_min = y_min + desired_shape[0]
        y_max = y_max + desired_shape[1]

    y_min = 0 
    y_max = desired_shape[0]
    x_min = x_min + desired_shape[1]
    x_max = x_max + desired_shape[1]

    while (y_max + desired_shape[1]) < height_original:
        crop = image[y_min:y_max, x_min:width_original]
        cv2.imwrite("imgs/" + str(nmbr) + ".jpg", crop)
        nmbr += 1
        y_min = y_min + desired_shape[0]
        y_max = y_max + desired_shape[1]