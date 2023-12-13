# Export audio in wav format
import WaveAudio
import numpy as np
import soundfile as sf
# Export audio in wav format
def generateMusicFile(list=[],filename="",fs=44100):
    data = []
    sf.write(filename,list,fs)
# testing
if __name__ == "__main__":
    volume=0.9
    fs=44100
    duration=1
    f=400
    sample1=WaveAudio.sine_wave(frequency=130.81, duration =duration, sample_rate=fs, amplitude=volume)
    sample2=WaveAudio.sine_wave(frequency=146.83, duration =duration, sample_rate=fs, amplitude=volume)
    sample3=WaveAudio.sine_wave(frequency=164.81, duration =duration, sample_rate=fs, amplitude=volume)
    sample4=WaveAudio.sine_wave(frequency=174.61, duration =duration, sample_rate=fs, amplitude=volume)
    sample5=WaveAudio.sine_wave(frequency=196, duration =duration, sample_rate=fs, amplitude=volume)
    list=[sample1,sample2,sample3,sample4,sample5]
    generateMusicFile(list,"final.wav")



