
LATEX    = platex
BIBTEX   = bibtex
DVIPDFMX = dvipdfmx
OPEN     = open
.PHONY: default

default: all

all:   

	${LATEX}    ./note-nevpt
	${BIBTEX}   ./note-nevpt
	${LATEX}    ./note-nevpt
	${LATEX}    ./note-nevpt

	${DVIPDFMX} ./note-nevpt

open:
	${OPEN}     ./note-nevpt.pdf

clean:
	rm -f *.aux 
	rm -f *.bbl
	rm -f *.dvi
	rm -f *.log
