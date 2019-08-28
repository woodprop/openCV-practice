import cv2

url = 'http://morgoth.ru/images/2016/11/10/1ba3710929969c93f7f3e489eec32bef.jpg'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    # frame = cv2.resize(frame, (800, 600))  # приводим разрешение к выходному, иначе на выходе пустой файл

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    if ret:
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # для завершения записи нажать 'q' на клаве

# cv2.imwrite('face.png', img)

