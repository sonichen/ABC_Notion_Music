#Read the abc file and calculate duration and get abc notes

#calculate duration
def dealWithData(content="",Q="",L="",notes=""):
    Q = (Q.split("\n")[0])
    Q_Beat= (int)(Q[int(Q.index("=")) + 1:len(Q)])
    Q_sign= (int)(Q[int(Q.index("/")) + 1:int(Q.index("=")) ])
    L = (L.split("\n")[0])
    L_sign =(int) (L[int(L.index("/")) + 1:len(L) ])
    duration = (1 / (Q_Beat / 60)) * (1 / L_sign) / (1 / Q_sign)
    return notes,duration
#Read File
def readFile(file_path):
    content = ""
    Q=""
    L=""
    notes=""
    with open(file_path, 'r') as f:
        line = f.readline()
        while line:
            content+=line
            if line[0]=="Q":
                    Q=line
            elif line[0] == "L":
                    L = line
            elif  line[0]!="X" and line[0]!="T" and (line[0]+line[1]!="C:") and line[0]!="Q" and line[0]!="M" and line[0]!="L" and line[0]!="K":
                line=line.strip("\n")
                notes += line
            line = f.readline()

    return dealWithData(content,Q,L,notes)

# testing
if __name__ == "__main__":
    notes,duration=readFile("demo.abc")
    print(notes)
    print(duration)



