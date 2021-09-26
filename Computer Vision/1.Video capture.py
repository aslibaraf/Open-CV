import cv2
#Videocapture is class
#0 for default cam. we can use multiple number as well.
vid=cv2.VideoCapture(0)
#fourcc code
fourcc=cv2.VideoWriter_fourcc(*'XVID')
#to write out video, use videowriter class
op=cv2.VideoWriter('OP.avi',fourcc,30.00,(640,480))
print("camera open",vid.isOpened())
while(vid.isOpened()):
    rat,frame = vid.read()
    if rat == True:
    #to get properies of video, use get function
        print(vid.get(cv2.CAP_PROP_FRAME_WIDTH),
        vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        op.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('o'):
          break
    else:
        break
vid.release()
op.release()
cv2.destroyWindow()

