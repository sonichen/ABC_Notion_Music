"""PyAudio Example: Play a wave file."""
""" Reference: https://people.csail.mit.edu/hubert/pyaudio/docs/"""
# Play the audio
import pyaudio
import wave
# Play the audio
def playMusicOnLine(file_path):
    CHUNK = 1024
    wf = wave.open(file_path, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data):
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()
    print("Finish")
# testing
if __name__ == "__main__":
    file_path = r"f1_row_spoken.wav"
    playMusicOnLine(file_path)
    print("hello1")