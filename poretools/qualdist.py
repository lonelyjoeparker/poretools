import Fast5File
from collections import Counter

def run(parser, args):

	qual_count = Counter()
	total_nucs = 0

	for fast5 in Fast5File.Fast5FileSet(args.files):
		fq = fast5.get_fastq()
		if fq is not None:
			qual_sum = 0
			this_nucs = 0
			for q in fq.qual:
				qual_count[ord(q)-33] += 1
				total_nucs += 1
				this_nucs += 1
				qual_sum += ord(q)-33
			mean_q = float(qual_sum) / float(this_nucs)
			print fast5.filename+'\t'+str(mean_q)
		fast5.close()

	for q in qual_count:
		print '\t'.join(str(s) for s in [chr(q+33), q, qual_count[q], 
			total_nucs, float(qual_count[q]) / float(total_nucs)])