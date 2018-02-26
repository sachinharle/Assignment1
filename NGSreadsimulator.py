#NGSreadsimulator.py
import sys
from Bio import (SeqIO)
from random import randint
'''
NGS read simulator that randomly picks out reads from a genome and outputs them as a fastq file
(using dummy quality values; read length of 50 bp and generate 100,000 reads from the human genome)
With a uniform error rate of 0.01 (1% of the time a base is randomly replaced with another base) to the fastq file.
->To run NGS read simulator
python3 NGSreadsimulator.py NC_000021.fasta out.fastq    <-
'''
#SysIO-file read&write

inFile = sys.argv[1]
outFile = sys.argv[2]
readLength = 50
reads = 100000

#random position
def randomPos():
    return randint(0,readLength-1)
#random nucleotide
def randomNT():
    nucleotide = ['A','G','C','T']
    return nucleotide[randint(0,3)]
#a base is randomly replaced with another base
def mutSeq(a):
    return a.replace(a[randomPos()],randomNT())
#dummy quality values
def qualityVal():
    return chr(randint(33,126))
#sequence from dummy quality values
def seqDummyVal(readLength):
    seqDmyVal=''
    for j in range(1,readLength):
        seqDmyVal+=qualityVal()
    return seqDmyVal

with open(inFile,'r') as i:
    my_seq = SeqIO.read(i, "fasta")
#seq->txt
genome = str(my_seq.seq)

#Output file - .fastq
with open(outFile,'w') as o:
    #for line in my_seq:
    #o.write(genome)
    #randomly pick out reads from a genome
    for a in range(reads):
        chr_name = (my_seq.id)
        chr_size = len(my_seq)
        readStart = randint(0,chr_size - readLength)
        readEnd = readStart + readLength
        #print(chr_size)
        #a uniform error rate of 0.01
        seqRead = mutSeq(genome[readStart:readEnd])
        #print(genome[readStart:readEnd])
        o.write("@SEQ_ID:"+str(chr_name)+":"+str(readStart)+":"+str(readEnd)+"\n")
        o.write(str(seqRead)+"\n")
        o.write("+\n")
        o.write(str(seqDummyVal(readLength))+"\n")
