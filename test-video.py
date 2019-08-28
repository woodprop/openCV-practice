import cv2
# cap = cv2.VideoCapture(0)     # Для записи с usb-камеры
cap = cv2.VideoCapture('http://192.168.0.211:8080/video')
# cap = cv2.VideoCapture('protocol://username:password@IP:port')  # Шаблон на память

fourcc = cv2.VideoWriter_fourcc(*'X264')    # кодек
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (800, 600))   # параметры выходного файла
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv2.flip(frame, 0) # переворот кадра
        frame = cv2.resize(frame, (800, 600))   # приводим разрешение к выходному, иначе на выходе пустой файл
        out.write(frame)    # Запись кадра в 'out'
        cv2.imshow('frame', frame)  # окошко
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # для завершения записи нажать 'q' на клаве

    else:
        break
# закрываем потоки
cap.release()
out.release()
cv2.destroyAllWindows()
