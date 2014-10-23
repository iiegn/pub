PDF_TARGETS = CV_en.pdf CV_en-short.pdf CV_en-pubs.pdf
TEX_SRCS := $(patsubst %pdf,%tex,$(PDF_TARGETS))

ROOT_DIR=$(shell pwd)
BUILD_DIR=$(ROOT_DIR)/.build
TEX = xelatex -file-line-error -interaction=errorstopmode
BIB = bibtex
LATEXMK_CE_OPTS = '$$cleanup_includes_cusdep_generated=1;\
				  $$clean_ext .= " bbl";\
				  $$clean_full_ext .= " bbl"' 

.PHONY: init all clean cleanall

all: init $(PDF_TARGETS)

init: moderncv.cls

moderncv.cls: moderncv/moderncv.cls
	ln -s moderncv/moderncv.cls . || true
	for cls in moderncv/*.sty; do ln -s $${cls} . || true; done

moderncv/moderncv.cls:
	bzr branch lp:moderncv
	# bzr diff moderncv/ --prefix moderncv/:moderncv/ > moderncv.patch
	patch -p0 < moderncv.patch

$(PDF_TARGETS): %.pdf:%.tex $(wildcard bit-*.tex) publications.bib
	latexmk -pdf -pdflatex="$(TEX)" -bibtex -use-make $<

clean:
	latexmk -c -e $(LATEXMK_CE_OPTS) $(TEX_SRCS)
	rm comment.cut || true

cleanall:
	latexmk -C -e $(LATEXMK_CE_OPTS) $(TEX_SRCS)
	rm comment.cut || true

cleanrealall: cleanall
	rm moderncv*.sty moderncv.cls tweaklist.sty || true
	rm -r moderncv || true
