import re

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import  Noise2
import  Noise
import colorednoise as cn
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import acoustics
import decimal
from decimal import Decimal
from decimal import Decimal, ROUND_HALF_UP

def sine_wave(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    # print(frequency,duration)
    return (np.sin(2*np.pi*np.arange(sample_rate*duration)*frequency/sample_rate)).astype(np.float32)*amplitude

def square_wave(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    samples= sine_wave(frequency, duration, sample_rate, amplitude)
    for i in range(0,len(samples)):
        if samples[i] > 0:
            samples[i]= amplitude
        elif samples[i] < 0:
            samples[i] = -amplitude
        else:
            samples[i] = 0.0
    return samples;

# def sawtooth(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
#     t = np.linspace(0, duration, sample_rate)
#     x= signal.sawtooth(2 * np.pi * frequency * t)
#     x = x * amplitude;
#     return x
def sawtooth(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    num_samples = duration * sample_rate
    num_samples = int(Decimal(str(duration * sample_rate)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
    t = np.linspace(0, duration, num_samples)
    x= signal.sawtooth(2 * np.pi * frequency * t)
    x = x * amplitude;
    return x

def triangle(frequency=440.0, duration =1.0, sample_rate=44100, amplitude=0.5):
    return np.abs(sawtooth(frequency=frequency, duration =duration, sample_rate=sample_rate, amplitude=amplitude))

def combineWaves(waves):
    complexWave = waves[0]
    for i in range(1,len(waves)):
        complexWave += waves[i]
    return complexWave

def playMusicWithNoise(waveform="1",duration="",f="",volume="",noiseType="white"):


    type=waveform
    fs = 44100  # sampling rate, Hz, must be an integer
    noiseParam=(float)(fs) * (float)(duration)
    print(fs*duration)
    noiseParam = round(((fs * duration)))

    if noiseParam==5512:
        noiseParam=5513
    print(noiseParam)
    noise = acoustics.generator.noise(noiseParam, color=noiseType, state=None)

    if type=="1":
        samples = sine_wave(frequency=f, duration=duration, sample_rate=fs, amplitude=volume)
    elif type=="2":
        samples = square_wave(frequency=f, duration=duration, sample_rate=fs, amplitude=volume)
    elif type=="3":
        samples = sawtooth(frequency=f, duration = duration,sample_rate=fs, amplitude=volume)
    elif type=="4":
        samples = triangle(frequency=f, duration = duration,sample_rate=fs, amplitude=volume)
    else:
        return
    final = combineWaves([samples, noise])
    return final


def playMusicWithoutNoise(waveform="1",duration="",f="",volume=""):
    type=waveform
    fs = 44100  # sampling rate, Hz, must be an integer
    if type=="1":
        samples = sine_wave(frequency=f, duration=duration, sample_rate=fs, amplitude=volume)
    elif type=="2":
        samples = square_wave(frequency=f, duration=duration, sample_rate=fs, amplitude=volume)
    elif type=="3":
        samples = sawtooth(frequency=f, duration = duration,sample_rate=fs, amplitude=volume)
    elif type=="4":
        samples = triangle(frequency=f, duration = duration,sample_rate=fs, amplitude=volume)
    else:
        return
    return samples

def playMusic(waveform="1",duration="",f="",volume="",noiseType=""):
    print(noiseType)
    if noiseType=="1":
        return playMusicWithNoise(waveform, duration, f, volume, "white")
    elif noiseType=="2":
        return playMusicWithNoise(waveform, duration, f, volume, "pink")
    elif noiseType=="3":
        return playMusicWithNoise(waveform, duration, f, volume, "brown")
    else:
        return playMusicWithoutNoise(waveform, duration, f, volume)
def playMusicWithNoise2(waveform="1",duration="",f="",volume="",noiseType="white"):


    type=waveform
    fs = 44100  # sampling rate, Hz, must be an integer
    # noiseParam=(float)(fs) * (float)(duration)
    # print(fs*duration)
    # noiseParam = round(((fs * duration)))
    #
    # if noiseParam==5512:
    #     noiseParam=5513
    # print(noiseParam)
    # noise = acoustics.generator.noise(noiseParam, color=noiseType, state=None)
    sh=(re.search("\d+",str(samples.shape)))
    noise=cn.powerlaw_psd_gaussian(noiseType,int(sh))
    if type=="1":
        samples = sine_wave(frequency=f, duration=duration, sample_rate=fs, amplitude=volume)
    elif type=="2":
        samples = square_wave(frequency=f, duration=duration, sample_rate=fs, amplitude=volume)
    elif type=="3":
        samples = sawtooth(frequency=f, duration = duration,sample_rate=fs, amplitude=volume)
    elif type=="4":
        samples = triangle(frequency=f, duration = duration,sample_rate=fs, amplitude=volume)
    else:
        return
    final = combineWaves([samples, noise])
    return final


if __name__ == "__main__":
    sample = playMusic("1", 4, 530, 30)
