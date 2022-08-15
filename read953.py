import cv2


rtsp2 = "rtsp://admin:123456@192.168.0.95:6003/media/video1"

cap2 = cv2.VideoCapture(rtsp2)
cv2.namedWindow("frame953", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
cv2.resizeWindow("frame953", 700, 400)  # 设置长和宽
while cap2.isOpened():

    ret, frame = cap2.read()
    if frame is None:
        continue
    # 调整窗口大小
    # print(ret,frame.shape)
    cv2.imshow('frame953', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap2.release()
cv2.destroyAllWindows()