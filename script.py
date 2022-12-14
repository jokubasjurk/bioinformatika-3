import matplotlib.pyplot as plt
from bioinfokit.analys import fastq
from Bio.Blast import NCBIXML, NCBIWWW

fastq_data = "reads.fastq";

# Pasiremta interneto šaltiniais
encodings_dictionary = dict({
    'Sanger Phred+33': (33, 73),
    'Solexa Solexa+64': (59, 104),
    'Illumina 1.3+ Phred+64': (64, 104),
    'Illumina 1.5+ Phred+64': (67, 105),
    'Illumina 1.8+ Phred+33': (33, 74)
})

def blast_search(seq):
    result_handle = NCBIWWW.qblast("blastn", "nt", seq, alignments=1, hitlist_size=1)
    records = NCBIXML.parse(result_handle)
    for rec in records:
        for alignment in rec.alignments:
            return alignment.hit_def

def plot_calculation():
    fastq_iterator = fastq.fastq_reader(file=fastq_data)
    quality_score_concat = ""
    gc_ratios = []
    ids = []
    sequences = []
    for entry in fastq_iterator:
        seq_id, sequence, _, quality_score = entry
        quality_score_concat = quality_score_concat + quality_score
        gc_ratios.append(round((sequence.count('G') + sequence.count('C')) / len(sequence), 2))
        ids.append(seq_id)
        sequences.append(sequence)
    unique_chars = set(quality_score_concat)

    for encoding in encodings_dictionary:
        characters_in_range = True
        for char in unique_chars:
            if ord(char) < encodings_dictionary[encoding][0] or ord(char) > encodings_dictionary[encoding][1]:
                characters_in_range = False
        if characters_in_range:
            print(encoding)

    x_axis = []
    y_axis = []
    for i in range(0, 100):
        x_axis.append(i / 100)
    for x in x_axis:
        y_axis.append(gc_ratios.count(x))
    plt.plot(x_axis, y_axis, color="black")
    plt.xlabel('C/G nucleotides')
    plt.ylabel('Amount of reads')
    plt.show()

    peak1_ids = []
    peak1_seq = []
    peak2_ids = []
    peak2_seq = []
    peak3_ids = []
    peak3_seq = []
    peak1_pos = [j for j, x in enumerate(gc_ratios) if x == 0.34][:5]
    peak2_pos = [j for j, x in enumerate(gc_ratios) if x == 0.54][:5]
    peak3_pos = [j for j, x in enumerate(gc_ratios) if x == 0.7][:5]
    for pos in peak1_pos:
        peak1_ids.append(ids[pos])
        peak1_seq.append(sequences[pos])
    for pos in peak2_pos:
        peak2_ids.append(ids[pos])
        peak2_seq.append(sequences[pos])
    for pos in peak3_pos:
        peak3_ids.append(ids[pos])
        peak3_seq.append(sequences[pos])
    print(peak1_seq)
    print(peak2_seq)
    print(peak3_seq)

    ids_c = []
    bacteria_c = []
    for seq_id in peak1_ids:
        ids_c.append(seq_id)
    for seq_id in peak2_ids:
        ids_c.append(seq_id)
    for seq_id in peak3_ids:
        ids_c.append(seq_id)

    for s in peak1_seq:
        bacteria_c.append(blast_search(s))
    for s in peak2_seq:
        bacteria_c.append(blast_search(s))
    for s in peak3_seq:
        bacteria_c.append(blast_search(s))

    print(ids_c)
    print(bacteria_c)

plot_calculation()