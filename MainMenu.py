# Entry program
import os
from pickle import TRUE
import sys
# 引入波的选择
import  WaveAudio
import  PlayABCMusic
import  PlayWavFilePyAudio
import MixedFile
# 播放音乐
sys.path.append("menus/")



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Selecting a waveform
def option1():
    cls()
    print("Please select the type of the waveform")
    print("1) Sine wave")
    print("2) Square wave")
    print("3) Sawtooth wave")
    print("4) Triangle wave")
    inputText = input("Please select a number between 1 and 4: ")
    if inputText.isdigit()and (int)(inputText)>=1 and (int)(inputText)<=4:
         print("Successfully")
         return  inputText
    else:
        print("Fail")
        print("The input value is not valid. Please try again.")
        return "1"

# Setting the loudness
def option2():
    cls()
    print("Setting the loudness");
    inputText = input("Please set the loudness, the input value should be between 0 and 100 ")
    if (float)(inputText)>=0 and (float)(inputText)<=100:
         print("Successfully")
         return  inputText
    else:
        print("Fail")
        print("The input value is not valid. Please try again.")
        return "50"



# Indicating the ABC file path
def option3():
    cls()
    print("Indicating the ABC file path");
    inputText = input("Please input the  path of the ABC file")
    print("Successfully")
    return  inputText



# Changing speed(BPM)
def option4():
    cls()
    print("Please select a speed for playing music");
    print("1) X 0.25")
    print("2) X 0.5")
    print("3) X 0.75")
    print("4) X 1")
    print("5) X 1.25")
    print("6) X 1.5")
    print("7) X 2")
    inputText = input("Please select a number between 1 and 7: ")
    if inputText.isdigit()and (int)(inputText)>=1 and (int)(inputText)<=7:
         print("Successfully")
         return inputText
    else:
        print("Fail")
        print("The input value is not valid. Please try again.")
        return "4"

# Shifting pitch
def option5():
    cls()
    print("The notes will be shifted based on Hertz");
    inputText = input("Please select a number:")
    print("Successfully")
    return  inputText




# Adding background noise
def option6():
    cls()
    print("Adding background noise");
    print("1) white noise")
    print("2) pink noise")
    print("3) brown noise")
    print("If you do not want noise, do not enter any word");
    inputText = input("Please select a number between 1 and 3:")
    return inputText



def option7():
    cls()
    print("Mixing within an external WAVfile");
    print("Input the external file path:");
    print("If you do not want to mix with another file, do not enter any word");
    inputText = input("Input the external WAVfile path which will be mixed with this file")
    print("Successfully")
    return  inputText


def option8(waveform="1",ABCFilePath="",BPM="",volume="",pitch=0,mixedFilePath="",noiseType="",outPutFilePath=""):
    cls()
    print("Playing the file");
    PlayABCMusic.playFile(waveform,ABCFilePath,BPM,volume,pitch,outPutFilePath,noiseType)
    if mixedFilePath=="":
        PlayWavFilePyAudio.playMusicOnLine(outPutFilePath)
    else:
        MixedFile.mixFiles(mixedFilePath,outPutFilePath,outputFilePath)
        PlayWavFilePyAudio.playMusicOnLine(outPutFilePath)
    print("Successfully")
def option9(waveform="1",ABCFilePath="",BPM="",volume="",pitch=0,mixedFilePath="",noiseType="",outPutFilePath=""):
    cls()
    print("Saving the music as a WAV file");
    PlayABCMusic.playFile(waveform,ABCFilePath,BPM,volume,pitch,outPutFilePath,noiseType)
    if mixedFilePath=="":
        x=1
    else:
        MixedFile.mixFiles(mixedFilePath,outPutFilePath)
    print("Successfully! The file has been saved to "+"OutPutFiles/output.wav")

def option10():
    cls()
    yesNo = input("Are you sure you want to exit the program?(y=yes/n=no)")
    if yesNo == 'y':
        sys.exit()

def getNoiseName(noise):
    if noise=="1":
        return "white noise"
    elif noise=="2":
        return "pink noise"
    elif noise=="3":
        return "brown noise"
    else:
        return "no noise"
def getWaveformName(waveform):
    if waveform=="1":
        return "sine wave"
    elif waveform=="2":
        return "square wave"
    elif waveform=="3":
        return "sawtooth wave"
    elif waveform=="4":
        return "triangle wave"
def getChangeSpeedName(BPM):
    if BPM=="1":
        return "X 0.25"
    elif BPM=="2":
        return "X 0.5"
    elif BPM=="3":
        return "X 0.75"
    elif BPM=="4":
        return "X 1"
    elif BPM=="5":
        return "X 1.25"
    elif BPM=="6":
        return "X 1.5"
    elif BPM=="7":
        return "X 1.75"
    elif BPM == "8":
        return "X 2"
# entry program
if __name__ == "__main__":
    waveform="1"#1-Selecting a waveform
    volume="50"#2-Setting the loudness
    ABCFilePath="InputABCFile/demo.abc"#3- Indicating the ABC file path
    BPM="4"   #4- Changing speed (BPM)
    pitch=0
    mixedFilePath="ABCAudio/f1_row_spoken.wav"
    noiseType=""
    processFilePath="ProcessFile/process.wav"
    outputFilePath = "OutputFiles/output.wav"
    while (TRUE):
        cls()
        print("1) Selecting a waveform")
        print("2) Setting the loudness")
        print("3) Indicating the ABC file path")
        print("4) Changing speed (BPM)")
        print("5) Shifting pitch")
        print("6) Adding background noise")
        print("7) Mixing within an external WAVfile")
        print("8) Playing the file")
        print("9) Saving the music as a WAV file, the output path is "+outputFilePath)
        print("10) exit")
        print("-----------------------------------")
        print("Settings:")
        print("Waveform="+getWaveformName(waveform),"  ;  ","Volume="+volume+"%","  ;  ","ABCFilePath="+ABCFilePath,)
        print("Noise=" + getNoiseName(noiseType),"  ;  ","Times the speed="+getChangeSpeedName(BPM),"  ;  ","Change Pitch="+str(pitch)+"HZ")
        print("Mixed File Path="+mixedFilePath)
        print("-----------------------------------")

        inputText = input("Please select a number between 1 and 10: ")
        match inputText:
            case '1':
                waveform=option1()
            case '2':
                volume=option2()
            case '3':
                ABCFilePath=option3()
            case '4':
                BPM=option4()
            case '5':
                pitch=option5()
            case '6':
                noiseType=option6()
            case '7':
                mixedFilePath=option7()
            case '8':
                option8(waveform,ABCFilePath,BPM,volume,pitch,mixedFilePath,noiseType,outputFilePath)
            case '9':
                 option9(waveform, ABCFilePath, BPM, volume, pitch, mixedFilePath, noiseType, outputFilePath)
            case '10':
                option10()
            case _:
                cls()
                print("The input value is not valid. Please try again.")
                input()
