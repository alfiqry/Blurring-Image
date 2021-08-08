# importing opencv CV2 module
import cv2

# image.
img = cv2.imread('Gambar.jpg')
cv2.imshow("Original Image", img)
# make sure that you have saved it in the same folder
# Averaging
# You can change the kernel size as you want
avging = cv2.blur(img,(10,10))
cv2.imshow('Averaging',avging)

# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow('Gaussian Blurring', gausBlur)

# Median blurring
medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)

# Bilateral Filtering
bilFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
