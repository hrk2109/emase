===============================
Overview
===============================

.. image:: https://badge.fury.io/py/emase.png
    :target: http://badge.fury.io/py/emase

.. image:: https://anaconda.org/kbchoi/emase/badges/version.svg
    :target: https://anaconda.org/kbchoi/emase

.. image:: https://travis-ci.org/churchill-lab/emase.png?branch=master
    :target: https://travis-ci.org/churchill-lab/emase

.. image:: https://readthedocs.org/projects/emase/badge/?version=latest
    :target: http://emase.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/30134570.svg
    :target: https://zenodo.org/badge/latestdoi/30134570

EMASE: Expectation-Maximization algorithm for Allele Specific Expression 
------------------------------------------------------------------------
Narayanan Raghupathy, Kwangbom Choi, Steve Munger, and Gary Churchill

* Free software: GNU General Public License v3 (GPLv3)
* Documentation: https://emase.readthedocs.org.

Note: The documentation for EMASE is still under work.

What is EMASE?
~~~~~~~~~~~~~~

EMASE is a software program written in Python to quantify allele-specific
expression and gene expression simultaneously from RNA-seq data. EMASE takes in
the diploid transcriptome alignment BAM file and GTF file as inputs and
estimates expression abundance for each isoforms and each alleles using
Expectation Maxmization algorithm.

Why Use EMASE?
~~~~~~~~~~~~~~

Current RNA-seq analysis pipeline employ two steps to quantify gene expression
and allele-specific expression (ASE); gene expression is estimated from all
read alignments, while ASE is assessed separately by using only reads that
overlap known SNP locations.

Large-scale genome sequencing efforts have characterized millions of genetic
variants across in human and model organisms. However development of tools that
can effectively utilize this individual/strain-specific variation to inform
quantitation of gene expression abundance have lagged behind.

EMASE, together with g2gtools (https://github.com/churchill-lab/g2gtools), offers an integrated
solution to utilize known genetic variations in quantifying expression abundances at allele 
and gene/isoform level.

In F1 hybrids from model organisms, EMASE allows us to utilize parental
strain-specific genetic variation in RNA-seq analysis to quantify gene
expression and allele-specific expression (ASE) simultaneously

In humans, EMASE allows us to utilize the individual's genetic variation in
doing personalized RNA-seq analysis and quantify gene expression and
allele-specific expression (ASE) simultaneously

Briefly, EMASE: EM for allele-specific expression, uses individualized diploid
genomes/transcriptomes adjusted for known genetic variations and quantifies
allele-specific gene expression and total gene expressionsimultaneously. The EM
algorithm employed in EMASE models multi-reads at the level of gene, isoform,
and allele and apportions them probabilistically.

One can use g2gtools to create personalized diploid transcritpme and align RNA-seq reads
simultaneously to the diploid transcriptome and get alignment file in BAM format. 
This diploid BAM file can be used as input to EMASE.

Applications
~~~~~~~~~~~~

Allele-specific gene expression in F1 Hybrids from model organisms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we have F1 hybrids with parental genetic variants information, one can use
g2gtools to build strain specific genomes and extract diploid transcriptome.
RNA-seq alignment bam file obtained by aligning RNA-seq reads to the diploid
transcriptome is used as input for EMASE.

Personalized ASE analysis in Human
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

EMASE can be used to do personalized RNA-seq analysis in human. For this,  we use the phased genetic
variation (SNP and Indel) information to construct personalized diploid genome and align reads to the diploid transcriptome..

Allele-specific Binding using Chip-Seq in F1 Hybrids
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although we explained the use of EMASE to quantify Allele-Specific Expression
from RNA-seq data, the tool can be used with other types of sequencing data. We
have successfully used EMASE to quantify allele-specific binding from ChIP-seq
data. While useing ChIP-seq, one needs to use diploid binding target sequences
instead of diploid transcriptome for alignment target sequences.

Mining Diploid alignments and alignment probabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EMASE can be used to glean more information from the alignment, in addition to running EMASE and 
obtaining effective read counts for each allele and isoform. For example, we can use EMASE's count-alignment 
program to obtain unique reads at allele-level for every gene, gene unique reads but allele-level multireads, 
and the total number of reads aligned to every gene. Having these alignment statistics at for every isoform and gene 
can be useful in interpreting expression estimates from EMASE. 


References
~~~~~~~~~~

* [Hierarchical Analysis of Multi-mapping RNA-Seq Reads Improves the Accuracy of Allele-specific Expression](http://www.biorxiv.org/content/early/2017/07/22/166900). Narayanan Raghupathy, Kwangbom Choi, Matthew J Vincent, Glen L Beane, Keith Sheppard, Steven C Munger, Ron Korstanje, Fernando Pardo Manuel de Villena, Gary A Churchill, doi: https://doi.org/10.1101/166900

* [RNA-Seq Alignment to Individualized Genomes Improves Transcript Abundance Estimates in Multiparent Populations](http://www.genetics.org/content/198/1/59.short) Steven C. Munger, Narayanan Raghupathy,Kwangbom Choi, Allen K. Simons, Daniel M. Gatti, Douglas A. Hinerfeld, Karen L. Svenson, Mark P. Keller, Alan D. Attie, Matthew A. Hibbs, Joel H. Graber, Elissa J. Chesler and Gary A. Churchill. Genetics. 2014 Sep;198(1):59-73. doi: 10.1534/genetics.114.165886.

* [PRDM9 Drives Evolutionary Erosion of Hotspots in Mus musculus through Haplotype-Specific Initiation of Meiotic Recombination](http://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1004916) Christopher L. Baker, Shimpei Kajita, Michael Walker, Ruth L. Saxl, Narayanan Raghupathy, Kwangbom Choi, Petko M. Petkov, Kenneth Paigen PLOS Genetics: published 08 Jan 2015 | info:doi/10.1371/journal.pgen.1004916

