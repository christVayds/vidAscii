import cv2
import sys

from video import Video

def main():
    args = sys.argv
    if len(args) > 1:
        video = Video(args[1])
        video.open()
        video.read()
        video.release()
    else:
        test = "/home/christian/Downloads/meme2.mp4"
        video = Video(test)
        video.open()
        video.read()
        video.release()

if __name__=='__main__':
    main()
