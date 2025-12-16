import cv2
import sys

from video import Video

def main():
    args = sys.argv
    if len(args) > 1:
        filename = args[1]
        level = args[2]

        # check if level is valid value
        if not level.isnumeric():
            print(f"Invalid value {level}")
            return

        # filename level
        video = Video(filename, int(level))
        if video.open():
            video.read()
            video.release()
    else:
        test = "/home/christian/Downloads/meme2.mp4"
        video = Video(test)
        if video.open():
            video.read()
            video.release()

if __name__=='__main__':
    main()
