import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import acoustics
import soundfile as sf
import cv2
from moviepy.editor import VideoFileClip
def makeNoise(type="white",duration=5):
    fs = 44100  # sampling rate, Hz, must be an integer
    # duration = 3  # in seconds, may be float

    # color can be white, pink, brown, blue, violet
    samples = acoustics.generator.noise(fs * duration, color=type, state=None)
    sf.write("noise.wav", samples, fs)
    return
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play.
    stream.write(samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

    # pd_series = pd.Series(samples)

    # pd_series.plot()
    # plt.show()



def get_duration_from_cv2(filename):
  cap = cv2.VideoCapture(filename)
  if cap.isOpened():
    rate = cap.get(5)
    frame_num =cap.get(7)
    duration = frame_num/rate
    return duration
  return -1

if __name__ == "__main__":
    clip = get_duration_from_cv2("output.wav")
    print(clip)  # seconds
