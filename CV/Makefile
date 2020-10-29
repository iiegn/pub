PDF_TARGETS = CV_en.pdf CV_en-short.pdf CV_en-pubs.pdf CV_en-eu.pdf
TEX_SRCS := $(patsubst %pdf,%tex,$(PDF_TARGETS))
TEX_XTRA_SRCS := $(wildcard bit-*.tex)
BIB_SRCS := $(wildcard *.bib)
OTR_SRCS := myplainyr.bst

#TEX = xelatex -file-line-error -interaction=errorstopmode
PATH := ./docker-texlive/bin/:$(PATH)
LATEXMK := latexmk
LATEXMK_PDFLATEX_OPTS ?= -file-line-error -interaction=nonstopmode
LATEXMK_CE_OPTS = '$$cleanup_includes_cusdep_generated=1;'

.PHONY: init all clean cleanall cleanrealall github

all: init $(PDF_TARGETS)

#init: moderncv.cls
init:

moderncv.cls: moderncv/moderncv.cls
	ln -s moderncv/moderncv.cls . || true
	for cls in moderncv/*.sty; do ln -s $${cls} . || true; done

moderncv/moderncv.cls:
	bzr branch lp:moderncv
	# bzr diff moderncv/ --prefix moderncv/:moderncv/ > moderncv.patch
	# patch -p0 < moderncv.patch

$(PDF_TARGETS): %.pdf:%.tex $(TEX_XTRA_SRCS) $(BIB_SRCS) $(OTR_SRCS)
	for AUX in $(wildcard *.aux); do echo $${AUX}; [ -s $${AUX} ] || rm $${AUX}; done
	$(LATEXMK) -pdf -pdflatex="lualatex $(LATEXMK_PDFLATEX_OPTS)" -dvi- -ps- -bibtex -use-make $<

pre.aux pub,aux: 
	$(LATEXMK) -pdf -pdflatex="lualatex $(LATEXMK_PDFLATEX_OPTS)" -dvi- -ps- -bibtex -use-make CV_en.tex

clean:
	$(LATEXMK) -c -bibtex -e $(LATEXMK_CE_OPTS) $(TEX_SRCS)
	-rm pre.bbl pub.bbl *.run.xml

cleanall:
	$(LATEXMK) -C -bibtex -e $(LATEXMK_CE_OPTS) $(TEX_SRCS)

cleanrealall: cleanall
	rm moderncv*.sty moderncv.cls tweaklist.sty || true
	rm -r moderncv || true

github:
	git checkout github 
	# may need more than just the latest commit
	# git cherry-pick master
	git checkout master -- Makefile $(PDF_TARGETS) $(TEX_SRCS) $(TEX_XTRA_SRCS) $(BIB_SRCS) $(OTR_SRCS)
	# for tex in CV_en*.tex bit-*.tex; do sed -i -r -e '/^[[:space:]]*%/ d' -e 's/([^\\])%.+$/\1/'  -e 's/\\endinput/%endinput/' -e '/%endinput/ q' ${tex}; done
	for tex in $(TEX_SRCS) $(TEX_XTRA_SRCS); do sed -i -r -e '/^[[:space:]]*%/ d' -e 's/([^\\])%.+$$/\1/'  -e 's/\\endinput/%endinput/' -e '/%endinput/ q' $${tex}; done
	sed -i '/\(file = \)\|\(mendeley-groups =\)\|\(mendeley-tags =\)/d' $(BIB_SRCS)
	git add Makefile $(PDF_TARGETS) $(TEX_SRCS) $(TEX_XTRA_SRCS) $(BIB_SRCS) $(OTR_SRCS)
	#git commit -m "CV/ - sync with master"
	#git push
	#git checkout master 

