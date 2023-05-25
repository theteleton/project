import cv2
import numpy as np
class ImageProcessing:
    def __init__(self):
        pass

    def preprocess(self, image_path):

        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("SHAPE")
        print(gray.shape)
        """
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if gray[i, j] < 240 and gray[i, j] != 255:
                    gray[i,j] = 255
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if gray[i, j] != 255:
                    gray[i,j] = 0
        """

        
        edged=cv2.Canny(gray,30, 31)
        #cv2.imshow('canny edges',edged)
        #cv2.waitKey(0)
        new_gray = gray
        contours,hierarchy = cv2.findContours(edged, 1, 2)
        

        list_of_tuples = []
        for cnt in contours:
            x1,y1 = cnt[0][0]
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            
            if len(approx) == 4:
                
                x, y, w, h = cv2.boundingRect(cnt)
                
                x_avg = approx[0][0][0] + approx[1][0][0] + approx[2][0][0] + approx[3][0][0]
                y_avg = approx[0][0][1] + approx[1][0][1] + approx[2][0][1] + approx[3][0][1]
                x_avg = x_avg / 4
                y_avg = y_avg / 4
                cnt1 = 0
                cnt2 = 0
                for i in range(4):
                    if approx[i][0][0] > x_avg:
                        cnt1 += 1
                    if approx[i][0][1] > y_avg:
                        cnt2 += 1
                if cnt1 != 2 or cnt2 != 2:
                    continue;
                list_of_tuples.append((-w * h, x, y, w, h))
                ratio = float(w)/h
                cv2.putText(img, f'Rectangle{x1},{y1}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
            
        list_of_tuples = sorted(list_of_tuples)
            
            

           
                
                
                
                
        cv2.imshow("picture", img)
        cv2.waitKey()
        return list_of_tuples
