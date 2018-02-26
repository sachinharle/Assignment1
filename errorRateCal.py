import sys, re
from Bio import (SeqIO)
'''
finding the error rate (read aligned to a part of the genome other than where it originated from)
-> Run errorRateCal.py with:
python3 errorRateCal.py chr22.sam <-
'''
inFile = sys.argv[1]
i = open(inFile,'r')
next(i)
tot=0
unaln=0
for line in i :
    p = re.compile(r'\w+')
    #readStart ==position-> aligned
    if p.findall(line)[2] != p.findall(line)[6] :
        unaln += 1
    tot += 1
print("Total unaligned reads: "+str(unaln)+"\n")
print("Total reads: "+str(tot)+"\n")
print("Error rate: "+str((unaln/tot)*100)+"\n")
