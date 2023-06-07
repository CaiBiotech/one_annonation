#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__cmddoc__ = """

rnaann.py - Merge trinotate result and eggnog result to one annotation table
#Contact: haiming_cai@hotmail.com - 2022 - CHINA-VMI

Basic usage: 
conda activate base
python rnaann.py -t trinotate_annotation_report.xls -e trinity_eggnog.emapper.annotations.xlsx -o one.annotation.csv

""" 

import os
import pandas as pd
import numpy as np
import sys, getopt


def readtable(file):
   if file.endswith("csv") or file.endswith("xls"):
      data = pd.read_csv(file, delimiter="\t")
   elif file.endswith("xlsx"):
      data = pd.read_excel(file, header=2, skipfooter=3)
   return data   

def mergeann(tndata, endata):
   totaldf = pd.DataFrame()
   head = ["Gene_ID", \
           "Transcript_ID", \
           "Protein_ID", \
           "Gene_Name", \
           "Description", \
           "RNAMMER", \
           "SignalP", \
           "TmHMM", \
           "Pfam_PF", \
           "Pfam_Description", \
           "ECs", \
           "KEGG_ko", \
           "KEGG_Pathway", \
           "KEGG_Module", \
           "KEGG_Reaction", \
           "KEGG_rclass", \
           "BRITE", \
           "GOs", \
           "GO_Description"]

   for idx,row in tndata.iterrows():
      key1 = row['#gene_id']
      key2 = row['transcript_id']
      key3 = row['prot_id']
      key6 = row['RNAMMER']
      key7 = row['SignalP']
      key8 = row['TmHMM']
      if row['Pfam'] != ".":
          key9 = ",".join([i.split("^")[0] for i in row['Pfam'].split("`")])
          key10 = ";".join([i.split("^")[2] for i in row['Pfam'].split("`")])
      else:
          key9 = row['Pfam']
          key10 = row['Pfam']
      if key3 in endata["query"].values:
          #print(key3)
          key11 = endata[endata["query"]==key3]["EC"].values
      else:
          key11 = ["."]




      key8 = row['TmHMM']
      key8 = row['TmHMM']
      key8 = row['TmHMM']      
      print(key11) 


#df.loc[(df[¡®column¡¯] == some_value) & df[¡®other_column¡¯].isin(some_values)]




def main(argv):
   inputtn = ''
   inputen = ''
   outputfile = ''

   try:
      opts, args = getopt.getopt(argv, "ht:e:o:", ["tnfile=","enfile=", "ofile="])
   except getopt.GetoptError:
      print('rnaann.py -t <inputtn> -e <inputen> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('rnaann.py -t <inputtn> -e <inputen> -o <outputfile>')
         sys.exit()
      elif opt in ("-t", "--tnfile"):
         inputtn = arg
      elif opt in ("-e", "--enfile"):
         inputen = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   #print('The input file for trinotate is', inputtn)
   #print('The input file for emapper is', inputen)
   #print('The final annotation result is', outputfile)
   dataset1 = readtable(inputtn)
   dataset2 = readtable(inputen)
   dataset3 = mergeann(dataset1, dataset2)
   #print(dataset1)
   #print(dataset2)

if __name__ == "__main__":
   main(sys.argv[1:])

