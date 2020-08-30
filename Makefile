latexfile = notebook


all: 
	while (pdflatex -shell-escape $(latexfile) ; \
	grep -q "Rerun to get cross" $(latexfile).log ) do true ; \
	done

rebuild: clean all

clean: # should make a function for all of these.
	[ ! -e *.log ] || rm *.log
	[ ! -e *.aux ] || rm *.aux
	[ ! -e *.toc ] || rm *.toc
	[ ! -e a.out ] || rm a.out
	[ ! -e *.class ] || rm *.class
	[ ! -e _minted-main ] || rm -r _minted-main
	[ ! -e main.pdf ] || rm main.pdf
