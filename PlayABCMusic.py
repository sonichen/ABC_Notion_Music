import  WaveAudio
import CalculateFrequence
import  ReadFile
import numpy as np
import FileWrite

def isLetter(current, next):
    return  (current.islower() or current.isupper()) and (next.islower() or next.isupper())
def isLetterWithNumber(current, next):
    return  (current.islower() or current.isupper()) and (next.isdigit())
def isSlashType(current,next):
    return (current.isupper() or current.islower()) and next=="/"
def dealWithStrs(i=0,item="",L="",waveform="",volume="",pitch=0,noiseType=""):
    list=[]
    while i < len(item):
        duration = ""
        sample=[]
        # 处理循环
        if (i + 1 == len(item)):
            if (item[i].islower()):
                duration = L
                #print(item[i], "--->", duration)
            if (item[i].isupper()):
                duration = L
                # print(item[i], "--->", duration)
            break;
        else:
            current = item[i]
            next = item[i + 1]

            if(next=="," or next=="'"):
                duration=L
                temp=current+next
                frequence = CalculateFrequence.findKey(temp)

                # print(temp, "--->", duration,frequence)
                sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                i=i+2
            elif isLetterWithNumber(current, next):
                duration = L * int(next)
                frequence=CalculateFrequence.findKey(current)+(float)(pitch)
                if(current.islower()):
                    # print(current, next, "--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                elif (current.isupper()):
                    # print(current, next, "--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                i = i + 2
            elif isLetter(current, next):
                if(current=="z"):
                    duration = L
                    # print(current, "rest--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, 0, 0,noiseType)
                elif (current.islower()):
                    duration = L
                    frequence = CalculateFrequence.findKey(current)+float(pitch)
                    # print(current, "--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                elif (current.isupper()):
                    duration = L
                    frequence = CalculateFrequence.findKey(current)+float(pitch)
                    # print(current, "--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                i = i + 1
            elif isSlashType(current,next):
                #检查是否是缩写
                if (i+1+1==len(item)-1):
                    # print(current,next)
                    p=1
                else:
                    third=item[i+2]
                    if(third.isdigit()):
                        duration = L/(int)(third)
                        frequence = CalculateFrequence.findKey(current) + float(pitch)
                        # print(current+next+third,"-->",duration)
                        sample = WaveAudio.playMusic(waveform, duration, frequence, volume, noiseType)
                        i=i+3
                    else:
                        duration=L/2
                        frequence = CalculateFrequence.findKey(current) + float(pitch)
                        sample = WaveAudio.playMusic(waveform, duration, frequence, volume, noiseType)
                        # print(current + next, "-->", duration)
                        i = i + 2
            else:
                if(current.islower()):
                    duration = L
                    frequence = CalculateFrequence.findKey(current)+float(pitch)
                    # print(current, "--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                if (current.isupper()):
                    duration = L
                    frequence = CalculateFrequence.findKey(current)+float(pitch)
                    # print(current, "--->", duration)
                    sample=WaveAudio.playMusic(waveform, duration, frequence,volume,noiseType)
                i = i + 1
        list=np.concatenate([list,sample])

    return  list

def playFile(waveform="",ABCFilePath="",BPM="",volume="",pitch=0,fileName="",noiseType=""):
    volume = (float)(volume)*0.01
    speed=0
    if(BPM=="1"):
        speed = 2
    elif(BPM=="2"):
        speed=1.75
    elif (BPM == "3"):
        speed =1.5
    elif (BPM == "4"):
        speed = 1
    elif (BPM == "5"):
        speed = 0.75
    elif (BPM == "6"):
        speed = 0.5
    elif (BPM == "7"):
        speed = 0.25
    else:
        speed=1
    notes, time = ReadFile.readFile(ABCFilePath)
    speed=time*speed
    playMusic(waveform,notes,speed,volume,pitch,fileName,noiseType)
def playMusic(waveform="",notes="",time="",volume="",pitch=0,fileName="",noiseType=""):

    notes = notes.replace(" ", "")
    notes = (notes.split("|"))

    loop = False
    L=time
    start = 0
    end = 0
    notesCount = 0
    list=[]
    totalDuration=0
    for item in notes:
        if (item == ""):
            empty = 0
        elif item[0] == ":":
            loop = True
            start = notesCount
        i = 0
        samples=dealWithStrs(i, item,L,waveform,volume,pitch,noiseType)
        if (item == ""):
            x=1#空白行
        elif item[len(item) - 1] == ":" and loop:
            loop = False
            end = notesCount
            #print(notes[start], notes[end])
            while (start <= end):
                i = 0
                samples=dealWithStrs(i, notes[start],L,waveform,volume,pitch,noiseType)
                start = start + 1

        notesCount = notesCount + 1
        list = np.concatenate([list, samples])
    
    FileWrite.generateMusicFile(list,fileName)
    print("Playing music......")

if __name__ == "__main__":

     # playFile("1","InputABCFile/demo.abc","1",50,0,"outp1111111111111ut.wav","white")
     playFile("1", "InputABCFile/demo3.abc", "1", 50, 0, "ceshi.wav", "white")

