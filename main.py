import cv2


# пустая функция
def empty(a):
    pass


# распознает лица в кадре и в цикле рисует вокруг них прямоугольник
def detect_face(img_gray, img, scale_factor, min_neighbors):
    faces = face_cascade.detectMultiScale(img_gray, scale_factor, min_neighbors)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# распознает глаза в кадре и в цикле рисует вокруг них прямоугольник
def decect_eye():
    # TODO
    pass


# создаем модель для распознавания лиц
face_cascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

# поиск лиц на изображениях
# for i in range(5):
#     img_name = f"test-img{i}.jfif"
#     img = cv2.imread("Resources/" + img_name)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     cv2.imshow(img_name, img)
#     cv2.waitKey(0)

# название главного окна
title_window = "WEB Cam"
# данные о ползунках
# которые используются для управления значениями ScaleFactor и minNeighbors
# которые передаются в функцию detectMultiScale для распознавания лиц
trackbar1_name = "ScaleFactor TrackBar"
tb1_default_value = 11
tb1_max_value = 100
trackbar2_name = "minNeighbors TrackBar"
tb2_default_value = 3
tb2_max_value = 5

# получаем видео из камеры (0- значит основная)
cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

# создаем новое окно отображения
cv2.namedWindow(title_window)
# создаем ползунки
cv2.createTrackbar(trackbar1_name, title_window, tb1_default_value, tb1_max_value, empty)
cv2.createTrackbar(trackbar2_name, title_window, tb2_default_value, tb2_max_value, empty)

while True:
    # получаем один кадр из видео потока
    ret, frame = cap.read()
    # считываем текущие значения ползунков
    tb1_value = cv2.getTrackbarPos(trackbar1_name, title_window) / 10
    tb2_value = cv2.getTrackbarPos(trackbar2_name, title_window)
    print(tb1_value, tb2_value)

    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    # распознаем лица на текущем кадре изображения и рисуем квадраты вокруг них
    detect_face(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), frame, tb1_value if tb1_value > 1 else 1.1, tb2_value)
    # detect_face(frame, frame, tb1_value if tb1_value > 1 else 1.1, tb2_value)
    # отображаем текущий кадр в окне
    cv2.imshow(title_window, frame)

    # для завершения нужно нажать q
    if cv2.waitKey(10) == ord("q"):
        print("STOP")
        break
# освобождает оперативную память
cap.release()
# уничтожаем все окна
cv2.destroyAllWindows()
