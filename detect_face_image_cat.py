import cv2

# khai báo file .xml để phát hiện khuôn mặt
cascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

# đọc ảnh
img = cv2.imread("manycat.jpg")
# cascade chỉ phát hiện được với ảnh xám nên convert -> ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# hàm này để detect (phát hiện trên ảnh xám)
faces = cascade.detectMultiScale(gray, 1.1, 5)

# vẽ 1 hcn với tọa độ trên, tọa độ dưới, màu, và stroke của hcn (vẽ trên ảnh màu)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


# đưa ảnh đã đọc ra màn hình
cv2.imshow("Bill Gates", img)


# chờ user phẩn hỏi bằng bàn phím
cv2.waitKey()
# dóng hết cửa sổ
cv2.destroyAllWindows()
