# Assignment1
NGS
NGSreadsimulator.py randomly picks out reads from a genome and outputs them as a fastq file(using dummy quality values; read length of 50 bp and generate 100,000 reads from the human genome)
With a uniform error rate of 0.01 (1% of the time a base is randomly replaced with another base) to the fastq file.
->To run NGSreadsimulator.py execute
python3 NGSreadsimulator.py NC_000021.fasta out.fastq
-x-
Aligning the resulting fastq file with bwa
  bwa commands.
bwa index NC_000021.fasta
bwa aln NC_000021.fasta out.fastq > aln.sai
bwa samse NC_000021.fasta aln.sai out.fastq > chr21.sam
finding the error rate
(read aligned to a part of the genome other than where it originated from)
-> Run errorRateCal.py with:
python3 errorRateCal.py chr22.sam <-
-x-x-
