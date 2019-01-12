import re
from Bio import SeqIO

# load full COI file and fix TH error
full = open("COI_dataset.fasta", "r")
outfile = open("COI_fixed.fasta", "w")
search_tex = r'TH_'
replace_tex = r'TH'
for line in full:
    line = line.strip()
    if ">" in line:
        line = re.sub(search_tex, replace_tex, line)
        outfile.write(line + "\n")
    else:
        outfile.write(line + "\n")
outfile.close()


def dummy_seq(full_fasta, partial_fasta, new_filename):
    # load partial fasta file
    h3 = open(partial_fasta, "r")
    outfile = open("tmp.fasta", "w")

    # remove header from mompha taxa (H3_ from H3 fasta)
    search_tex = r"GAPDH_|H3_|DDC_|Ef1a_|CAD_"
    replace_tex = r""
    for line in h3:
        line = line.strip()
        if ">" in line:
            line = re.sub(search_tex, replace_tex, line)
            outfile.write(line + "\n")
        else:
            outfile.write(line + "\n")
    outfile.close()

    # this should be thefull fasta
    full = open(full_fasta,"r")

    # calc max length of file
    max_len = 0
    max_description = ""
    for record in SeqIO.parse("tmp.fasta", "fasta"):
        if len(record) > max_len:
            max_len = len(record)
            max_description = record.description
    print(max_description)
    print(max_len)

    # string of Ns equal to max length
    string_val = "N" * max_len
    print string_val


    # load hits dict with h3 headers as keys and sequences as values.
    h3_prune = open("tmp.fasta", "r")

    hits_dict = {}

    for line in h3_prune:
        line = line.strip()
        if ">" in line:
            tax_key = line
            hits_dict[tax_key] = 1
        else:
            tax_value = line
            hits_dict[tax_key] = tax_value

    # fill coi dict
    coi_dict = {}
    for line in full:
        line = line.strip()
        if ">" in line:
            coi_tax = line
            coi_dict[coi_tax] = string_val

    print "sweaty ballz"

    # find common keys and new keys
    A = list(hits_dict.keys())
    B = list(coi_dict.keys())
    commonKeys = set(A) - (set(A) - set(B))
    new_key = (set(B) - set(A))

    print commonKeys
    print new_key

    # remove common keys from coi dict
    for key in commonKeys:
        if key in coi_dict:
            del coi_dict[key]

    # write to outfile
    # this is the new filename
    outfile = open(new_filename, "w")

    for i in hits_dict:
        outfile.write(i + "\n" + hits_dict[i] + "\n")

    # print coi fasta files
    for i in coi_dict:
        outfile.write( i + "\n" + coi_dict[i] + "\n")

dummy_seq("COI_fixed.fasta", "6-gene_dataset_GAPDH_aligned.fasta", "GAPDH.fasta")
dummy_seq("COI_fixed.fasta", "6-gene_dataset_H3_aligned.fasta", "H3.fasta")
dummy_seq("COI_fixed.fasta", "6-gene_dataset_EF1a_aligned.fasta", "EF1a.fasta")
dummy_seq("COI_fixed.fasta", "6-gene_dataset_DDC_aligned.fasta", "DDC.fasta")
dummy_seq("COI_fixed.fasta", "6-gene_dataset_CAD_aligned.fasta", "CAD.fasta")


