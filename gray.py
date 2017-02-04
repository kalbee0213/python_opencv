import cv2
import sys

class grayer:
    def __init__(self,colorimgname):
        self.colorimgname = colorimgname

    def makegrayscaleimg(self):
        self.grayimg = cv2.imread(self.colorimgname,0)


    def writegrayimg(self):
        cv2.imwrite("./result.png",self.grayimg)
        cv2.imshow("result",self.grayimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

args = sys.argv
g = grayer(args[1])
g.makegrayscaleimg()
g.writegrayimg()