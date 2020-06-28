# import cv2
# cap = cv2.VideoCapture('001.mp4')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fps =cap.get(cv2.CAP_PROP_FPS)
# #fps=30
# size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# #size=(960,544)
# i=0
# while(cap.isOpened()):
#     i=i+1
#     ret, frame = cap.read()
#     if ret==True:
#         cv2.imwrite('D:/bs/call'+str(i)+'.jpg',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
#
# cv2.destroyAllWindows()

import cv2
import math
# 使用opencv按一定间隔截取视频帧，并保存为图片
vc = cv2.VideoCapture('111.mp4')  # 读取视频文件
c = 0
d=0
# d = 1114*3
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
 rval = False
timeF = 1 # 视频帧计数间隔频率
while rval:  # 循环读取视频帧
 rval,frame = vc.read()
 if (c % timeF == 0):#每隔timeF帧进行存储操作
  cv2.imwrite('D:/bs/ceshi/'+str(int(d/3))+"_"+str(d%3)+'.jpg',frame)  # 存储为图像
  d = d + 1
 c = c + 1
 cv2.waitKey(1)
vc.release()
