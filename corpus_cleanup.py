f = open("kor.txt", "r")
wf = open("korCorpus.txt", "w")

for line in f:
    line = line[0:line.index("CC-BY")]

    wf.write(line + "\n")