import cv2
import time

class Video:

    def __init__(self, videofile, level=0):
        self.videofile = videofile
        self.ascii_chars = ["@#$%&WMOo*+xv:.,' ", "@%#*+=-:. "]
        self.level = level
        self.cap = cv2.VideoCapture(self.videofile)

    def open(self):
        if not self.cap.isOpened():
            print(f"Failed to open the vide file {self.videofile}")
            return
        return True

    def read(self):
        running = True

        framecount = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / fps)
        loopdelay = 1 / fps
        # print(f"FPS: {delay}")
        while running:
            ret, frame = self.cap.read()

            if not ret:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            print("\033[H\033[J", end="")  # Clear terminal
            print(self.frameToAscii(gray))

            time.sleep(loopdelay)

            #cv2.imshow(self.videofile, gray)

            # Wait for 1ms for key press to continue or exit if 'q' is pressed
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                running = False

    def frameToAscii(self, gray, width=200):
        height, origwidth = gray.shape
        aspectRatio = height / origwidth
        nheight = int(aspectRatio * width * 0.5)
        rframe = cv2.resize(gray, (width, nheight))

        ascii_frame = ""
        for row in rframe:
            for pixel in row:
                # Map 0-255 to ascii characters
                index = int(pixel / 255 * (len(self.ascii_chars[self.level])-1))
                ascii_frame += self.ascii_chars[self.level][::-1][index]
            ascii_frame += '\n'
        return ascii_frame

    def release(self):
        cv2.destroyAllWindows()
        self.cap.release()
