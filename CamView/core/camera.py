from imutils.video import VideoStream
import cv2


class CamView(object):

    def __init__(self, usuario, senha, ip):
        self.url = cv2.VideoCapture("rtsp://"+usuario+":"+senha+"@"+ip+":554/live/0/MAIN")

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        success, imgNp = self.url.read()
        resize = cv2.resize(imgNp, (640, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()
