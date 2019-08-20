
LATEX    = pdflatex
BIBTEX   = bibtex
DVIPDFMX = dvipdfm
OPEN     = cp 
masa     = cept-manuscript # latest my version
.PHONY: default

default: all

all:   

	${LATEX}  ${masa}
	${BIBTEX} ${masa}
	${LATEX}  ${masa}
	${LATEX}  ${masa}

#	${DVIPDFMX} ./paper
#	pdflatex ./paper 
#	${OPEN}     ./paper.pdf

open:
	${OPEN}     ./cept-manuscript.pdf ~/G-Drive

clean:
	rm -f *.aux 
	rm -f *.bbl
	rm -f *.dvi
	rm -f *.log
