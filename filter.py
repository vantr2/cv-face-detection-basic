import cv2


# lọc trung bình
img_blur = cv2.imread('images/blur_test.png')
re_blur = cv2.blur(img_blur, (5, 5))
cv2.imshow("Blur", img_blur)
cv2.imshow("Blur Test", re_blur)

# lọc Gauss
img_gaussianblur = cv2.imread('images/gaussian_test.png')
re_gaussianblur = cv2.GaussianBlur(img_gaussianblur, (5, 5), 0)
cv2.imshow("Gaussian Blur", img_gaussianblur)
cv2.imshow("Gaussian Blur Test", re_gaussianblur)

# lọc trung bình
img_medianblur = cv2.imread('images/median_test.png')
re_medianblur = cv2.medianBlur(img_medianblur, 5)
cv2.imshow("Median Blur", img_medianblur)
cv2.imshow("Median Blur Test", re_medianblur)

# lọc song tuyến tính
img_bilaterialblur = cv2.imread('images/median_test.png')
re_bilaterialblur = cv2.bilateralFilter(img_bilaterialblur, 9, 75, 75)
cv2.imshow("Bilaterial Blur", img_bilaterialblur)
cv2.imshow("Bilaterial Blur Test", re_bilaterialblur)

#
cv2.waitKey()
