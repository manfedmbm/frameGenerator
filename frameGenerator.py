from subprocess import check_output
import random
import datetime
import os

def generateFrame(sourceVideoFilePath, frameOutputDirectory, positionInSeconds) :
    currentTimeForFileName = str(datetime.datetime.now()).replace(":", ".")
    check_output(
        f"ffmpeg -ss {positionInSeconds} -i \"{sourceVideoFilePath}\" -vf \"scale=iw*sar:ih\" -frames:v 1 -q:v 2 \"{frameOutputDirectory}{currentTimeForFileName}.png\"",
        shell=True
    ).decode()

def generateFrameForDirectory(sourceDirectory, targetDirectory, interval) :
    filesInPath = os.listdir(sourceDirectory)
    for file in filesInPath :
        fullFilePath = os.path.join(sourceDirectory, file)
        videoLengthInSeconds = float(check_output(f"ffprobe -i \"{fullFilePath}\" -show_entries format=duration -v quiet -of csv=\"p=0\"", shell=True).decode())
        frameOutputDirectory = targetDirectory + os.path.basename(fullFilePath) + "\\"
        if not os.path.isdir(frameOutputDirectory):
            os.mkdir(frameOutputDirectory)
        step = 0
        while step < videoLengthInSeconds :
            generateFrame(fullFilePath, frameOutputDirectory, step)
            step += interval

sourceDirectory = "L:\\myDirectory\\"
targetDirectory = "C:\\myDirectory\\"
generateFrameForDirectory(sourceDirectory, targetDirectory, 5)