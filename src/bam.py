#!/usr/bin/env python



import pysam
import os
import sys
import re
import pickle
import itertools
import collections
import math


##updating the library look up path
dir = os.path.dirname(__file__)
sys.path.append(os.path.join(dir,'../lib'));
import bamUtils
import utils


#bed_file = sys.argv[1]
#bam_files = sys.argv[2:]
#bamUtils.feature_cov_in_bam(bed_file,bam_files,stranded=True,min_map_qual=0,lib_protocol='second-strand')

#chr_size_file = sys.argv[2]


bam_file = sys.argv[1]
#split bam assuming input is small RNA second stranded library
#bamUtils.split_RNASeq_reads_bam_by_strand(bam_file,library_protocol='first-strand')


#bam_file = sys.argv[1]
#creating the bedgraph file
bamUtils.bam_to_bedGraph(bam_file)


#bamUtils.create_detailed_insert_size_plot(bam_file)
#bamUtils.plot_bamCoverage(bam_file)






#
#bamFile_name_sorted = bamUtils.name_sort_bam(bam_file)
#(bamfile_handle,bamfile_prefix) = bamUtils.get_apt_file_handle_for_mapped_file(bamFile_name_sorted)
#
#bag = collections.Counter()
#insert_size = []
#
#for counter,read1,read2 in itertools.izip(itertools.count(1),bamfile_handle,bamfile_handle):
#    
#    if counter % 1000 == 0:
#        #print bag
#        #print insert_size
#        pass
#    
#    if not bamUtils.is_a_sequencing_readPair(read1, read2):
#        continue
#        pass
#    
#    #insert_size.append(abs(read1.isize))
#    
#    bag[bamUtils.get_readPair_type(read1,read2)] += 1
#    
#
#print bag    
#    
    





#generate AlignStats
#bamUtils.bamStats(bam_file,force_run=True)


#generate the bam coverage
#bamUtils.plot_bamCoverage(bam_file)











        
            
    
    
    






