#!/usr/bin/env python
import sys
import getopt
from emase.AlignmentPropertyMatrix import AlignmentPropertyMatrix as APM

help_message = '''

    Usage:
        combine_h5files.py -i <h5_list> -c <comp_lib> -o <out_file>

    Input:
        <h5_list>  : comma(,) separated list of PyTables files
        <comp_lib> : compression library for saving PyTables
        <out_file> : output file name

    Note:

'''

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hi:c:o:", ["help"])
        except getopt.error, msg:
            raise Usage(msg)

        # Default values of vars
        flist = None
        complib = 'zlib'
        outfile = 'alignments.combined.h5'

        # option processing (change this later with optparse)
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option == '-i':
                flist = value.split(',')
            if option == '-c':
                complib = value
            if option == '-o':
                outfile = value

        # Check if the required options are given
        if flist is None or len(flist) < 2:
            raise Usage(help_message)

        #
        # Main body
        #

        aln_list = list()
        for f in flist:
            aln_list.append(APM(h5file=f))
        combined_aln = aln_list[0].copy()
        for aln in aln_list[1:]:
            combined_aln = combined_aln.combine(aln)
        combined_aln.save(h5file=outfile, complib=complib)

        #
        # End of main body
        #

    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        return 2


if __name__ == "__main__":
	sys.exit(main())
