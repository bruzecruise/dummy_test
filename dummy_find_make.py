import re

# load full COI file
full = open("COI_dataset.fasta", "r")

# load partial H3 file
h3 = open("6-gene_dataset_H3_aligned.fasta", "r")

search_tex = r'H3_'
replace_tex = r''

# remove header from mompha taxa (H3_ from H3 fasta)
for line in h3:
    line = line.strip()
    if ">" in line:
        line = re.sub(search_tex, replace_tex, line)
        print(line)
    else:
        print(line)




        #line = re.sub(search_tex, replace_tex, line)
        #line = re.sub(search_tex2, replace_tex2, line)
        #outfile.write( line + "\n")
#outfile.close()
#File.close()





#File = open("H3_subset.fasta","r")
#outfile = open("H3_subset2.fasta", "w")

#search_tex = r'^N+'
#replace_tex = r''

#search_tex2 = r'(N+)$'
#replace_tex2 = r''

#for line in File:
   # line = line.strip()
   # if ">" in line:
       # outfile.write( line + "\n")
    #else:
   #     line = re.sub(search_tex, replace_tex, line)
        #line = re.sub(search_tex2, replace_tex2, line)
        #outfile.write( line + "\n")
#outfile.close()
#File.close()