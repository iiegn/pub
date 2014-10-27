PDF_TARGETS = CV_en.pdf CV_en-short.pdf CV_en-pubs.pdf
TEX_SRCS := $(patsubst %pdf,%tex,$(PDF_TARGETS)) $(wildcard bit-*.tex)
BIB_SRCS := $(wildcard *.bib)

TEX = xelatex -file-line-error -interaction=errorstopmode
LATEXMK_CE_OPTS = '$$cleanup_includes_cusdep_generated=1;'

.PHONY: init all clean cleanall cleanrealall github

all: init $(PDF_TARGETS)

init: moderncv.cls

moderncv.cls: moderncv/moderncv.cls
	ln -s moderncv/moderncv.cls . || true
	for cls in moderncv/*.sty; do ln -s $${cls} . || true; done

moderncv/moderncv.cls:
	bzr branch lp:moderncv
	# bzr diff moderncv/ --prefix moderncv/:moderncv/ > moderncv.patch
	patch -p0 < moderncv.patch

$(PDF_TARGETS): %.pdf:%.tex $(TEX_SRCS) $(BIB_SRCS)
	for AUX in $(wildcard *.aux); do echo $${AUX}; [ -s $${AUX} ] || rm $${AUX}; done
	latexmk -pdf -pdflatex="$(TEX)" -bibtex -use-make $<

pre.aux pub,aux: 
	$(TEX) CV_en.tex

clean:
	latexmk -c -bibtex -e $(LATEXMK_CE_OPTS)
	rm pre.bbl pub.bbl || true

cleanall:
	latexmk -C -bibtex -e $(LATEXMK_CE_OPTS)

cleanrealall: cleanall
	rm moderncv*.sty moderncv.cls tweaklist.sty || true
	rm -r moderncv || true

github: $(PDF_TARGETS)
	git checkout github 
	git cherry-pick master
	git checkout master -- $(wildcard CV_en*.tex) $(wildcard bit-*.tex)
	# for tex in CV_en*.tex bit-*.tex; do sed -i -r -e '/^[[:space:]]*%/ d' -e 's/([^\\])%.+$/\1/'  -e 's/\\endinput/%endinput/' -e '/%endinput/ q' ${tex}; done
	for tex in $(wildcard CV_en*.tex) $(wildcard bit-*.tex); do sed -i -r -e '/^[[:space:]]*%/ d' -e 's/([^\\])%.+$$/\1/'  -e 's/\\endinput/%endinput/' -e '/%endinput/ q' $${tex}; done
	#git commit "CV/ - sync with latest tex"
	#git push
	#git checkout master 

