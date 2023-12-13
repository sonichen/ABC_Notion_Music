# 噪音
# reference: https://stackoverflow.com/questions/67085963/generate-colors-of-noise-in-python
from random import sample
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def white_noise1(duration=1.0, sample_rate=44100, amplitude=0.5):
    mean = 0
    std = 1
    num_samples = duration * sample_rate
    samples = np.random.normal(mean, std, size=num_samples)
    samples = samples * amplitude
    return samples


def noise_psd(N, psd=lambda f: 1):
    X_white = np.fft.rfft(np.random.randn(N));
    S = psd(np.fft.rfftfreq(N))
    # Normalize S
    S = S / np.sqrt(np.mean(S ** 2))
    X_shaped = X_white * S;
    return np.fft.irfft(X_shaped);


def PSDGenerator(f):
    return lambda N: noise_psd(N, f)


@PSDGenerator
def white_noise(f):
    return 1;


@PSDGenerator
def blue_noise(f):
    return np.sqrt(f);


@PSDGenerator
def violet_noise(f):
    return f;


@PSDGenerator
def brownian_noise(f):
    return 1 / np.where(f == 0, float('inf'), f)


@PSDGenerator
def pink_noise(f):
    return 1 / np.where(f == 0, float('inf'), np.sqrt(f))

# def makeNoise(type=""):


if __name__ == "__main__":
    fs = 44100  # sampling rate, Hz, must be an integer
    duration = 15  # in seconds, may be float

    # samples = white_noise1(duration = duration,sample_rate=fs, amplitude=volume)
    # samples = white_noise(duration*fs)
    # samples = pink_noise(duration*fs)
    samples = white_noise(duration * fs)

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

    pd_series = pd.Series(samples)

    # pd_series.plot()
    # plt.show()
