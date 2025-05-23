from subprocess import check_output
import random
import datetime

videoFilePath = "D:\\myDirectory\\"
FrameOutputDirectory = "C:\\myDirectory\\"
amountOfFramesToGenerate = 10
videoLengthInSeconds = float(check_output(f"ffprobe -i \"{videoFilePath}\" -show_entries format=duration -v quiet -of csv=\"p=0\"", shell=True).decode())

for i in range(amountOfFramesToGenerate):
    # get random second from videoLengthInSeconds
    randomDecimal = random.uniform(0, videoLengthInSeconds)
    currentTimeForFileName = str(datetime.datetime.now()).replace(":", ".")
    # take screenShot at random second
    check_output(f"ffmpeg -ss {randomDecimal} -i \"{videoFilePath}\" -frames:v 1 -q:v 2 \"{FrameOutputDirectory}{currentTimeForFileName}.png\"", shell=True).decode()
