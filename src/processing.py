import cv2
import numpy as np
class ImageProcessing:
    def __init__(self):
        pass

    def preprocess(self, image_path):

        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if gray[i, j] < 240 and gray[i, j] != 255:
                    gray[i,j] = 255
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if gray[i, j] != 255:
                    gray[i,j] = 0
        #cv2.imshow("picture", gray)
        #cv2.waitKey()
        ret,thresh = cv2.threshold(gray,50,255,0)
        contours,hierarchy = cv2.findContours(thresh, 1, 2)
        sol = gray

        list_of_tuples = []
        for cnt in contours:
            x1,y1 = cnt[0][0]
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            
            if len(approx) == 4:
                
                x, y, w, h = cv2.boundingRect(cnt)
                
                if w * h <= 1000 or x < 200 or y < 100 or x > 1500:
                    continue
               
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
                list_of_tuples.append((x, y, w, h))
                ratio = float(w)/h
                
                cv2.putText(img, f'Rectangle{x1},{y1}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
        #cv2.imshow("picture", img)
        #cv2.waitKey()
        return list_of_tuples
