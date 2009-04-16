#!/usr/bin/env bash
#
# PDF2Keynote - 'generate' a keynote presentation from a PDF file
# (tailored for LaTeX beamer PDF files)
#
# this script takes as input the beamer LaTeX-ed PDF and
# 1. generates a PDF of size 1024x768
# 2. decomposes the PDF into single-page PDF files
#
# prerequisites:
# - beamer-ready LaTeX
# - pdftk (http://www.accesspdf.com/pdftk/ - apt-gettable from fink)
#
# 
# @author egon w. stemle <egon.stemle@uos.de>
# @version june 2006
#
# History:
# 20060611 - es : initial version
#
PATH=/sw/bin:/usr/bin:/usr/local/bin

syntax() {
	echo "$0: [FILE]"
	exit 2
}

PDF2KEYNOTE_TEMPDIR=/tmp
PDF2KEYNOTE_TEMPFILE=$PDF2KEYNOTE_TEMPDIR/PDF2Keynote.tex
PDF2KEYNOTE_TEMPFILENAME=`basename $PDF2KEYNOTE_TEMPFILE`
PDF2KEYNOTE_TEXFILENAME="PDF2Keynote.tex"
PDF2KEYNOTE_TEXFILE="`dirname $0`/$PDF2KEYNOTE_TEXFILENAME"
PDF2KEYNOTE_FILE=$1
PDF2KEYNOTE_FILENAME=`basename $PDF2KEYNOTE_FILE`

# remember where to return at the end... 
MYDIR=`pwd`

# test whether the file exists
if ! [ -e $PDF2KEYNOTE_FILE ];then syntax; fi

#
# put together the TEX-file that will be rendered 1024x768 
#
#######
## BEGIN: TEX-file
##
cat > $PDF2KEYNOTE_TEMPFILE << "EOF" 

\documentclass{minimal}

\usepackage[paperwidth=1024pt,paperheight=768pt]{geometry}
\geometry{top=0cm,bottom=0cm,left=0cm,right=0cm,nohead,nofoot}

\usepackage{pdfpages}

\begin{document}
EOF

echo " \includepdf[pages=1-]{$PDF2KEYNOTE_FILENAME}" >> $PDF2KEYNOTE_TEMPFILE

cat >> $PDF2KEYNOTE_TEMPFILE << "EOF" 
\end{document}

EOF

##
## END: TEX-file
#######

cp $PDF2KEYNOTE_FILE $PDF2KEYNOTE_TEMPDIR/$PDF2KEYNOTE_FILENAME
cd $PDF2KEYNOTE_TEMPDIR

# delete old pictures
rm -r $PDF2KEYNOTE_TEMPDIR/PDF2Keynote

pdflatex $PDF2KEYNOTE_TEMPFILE 

mkdir PDF2Keynote
pdftk `basename $PDF2KEYNOTE_TEXFILENAME .tex`.pdf burst output PDF2Keynote/page_%04d.pdf

cd $MYDIR
