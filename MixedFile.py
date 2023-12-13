from pydub import AudioSegment
# Mixing audio files
def mixFiles(fileName="",mixedFileName="",outFileName="OutputFiles/MixedOutput.wav"):
    sound1 = AudioSegment.from_wav(mixedFileName)
    sound2 = AudioSegment.from_wav(fileName)

    output = sound1.overlay(sound2)
    output.export(outFileName, format="wav")  # save

if __name__ == "__main__":
    sound1 = AudioSegment.from_wav("OutputFiles/Output.wav")
    sound2 = AudioSegment.from_wav("ABCAudio/f1_row_spoken.wav")
    print(len(sound1))
    print(len(sound2))