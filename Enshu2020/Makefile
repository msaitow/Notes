
LATEX    = platex
BIBTEX   = bibtex
DVIPDFMX = dvipdfmx
OPEN     = evince
HYD      = enshu-hydrogen-atom-electronic-configurations
PT       = enshu-pt-and-var
.PHONY: default

default: hydrogen

hydrogen:   

	${LATEX}    ${HYD}
	${LATEX}    ${HYD}
	${DVIPDFMX} ${HYD}
	${OPEN}     ${HYD}.pdf

pt:   

	${LATEX}    ${PT}
	${LATEX}    ${PT}
	${DVIPDFMX} ${PT}
	${OPEN}     ${PT}.pdf

clean:
	rm -f *.aux 
	rm -f *.bbl
	rm -f *.dvi
	rm -f *.log
