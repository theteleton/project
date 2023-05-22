import cv2
import numpy as np
class ImageProcessing:
    def __init__(self):
        pass

    def preprocess(self, image_path):

        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(gray.shape)
        print(gray[100:500, 900])
        
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if gray[i, j] != 247 and gray[i, j] != 255:
                    gray[i,j] = 255
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if gray[i, j] != 255:
                    gray[i,j] = 0

        ret,thresh = cv2.threshold(gray,50,255,0)
        cv2.imshow("Shapes", thresh)
        cv2.waitKey()
        contours,hierarchy = cv2.findContours(thresh, 1, 2)
        sol = gray

        for cnt in contours:
            x1,y1 = cnt[0][0]
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(cnt)
                
                if w * h <= 1000 or w*h >= 1000 * 1000:
                    continue
                print(x, y, w, h)
                ratio = float(w)/h
                
                cv2.putText(img, f'Rectangle{x1},{y1}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)

        cv2.imshow("Shapes", img)
        cv2.waitKey()
