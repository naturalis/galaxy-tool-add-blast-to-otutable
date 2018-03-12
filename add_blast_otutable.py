#!/usr/bin/env python
import sys, os, argparse
import glob
import tempfile
import subprocess

if __name__=="__main__":
    # blast result file
    blast = open(sys.argv[1])
    blastRows = {}
    for x in blast:
        row = x.split("\t")
        blastRows[row[0]] = x
    blast.close()

    with open(sys.argv[2], 'r') as otu, open(sys.argv[3], 'a') as output:
        for y in otu:
            row = y.split("\t")
            try:
                species = blastRows[row[0]].split("/")[-1]
                blastrow = blastRows[row[0]].strip()
                # del row[0]
                # output.write(species.strip()+"\t"+"\t".join(row).strip()+"\t"+blastrow.strip()+"\n")
                output.write("\t".join(row).strip() + "\t" + blastrow.strip() + "\n")
            except:
                output.write(y.strip() + "\n")

    


