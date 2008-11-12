#!/usr/bin/env bash
#
# to render the html try:
#
# 1. line 23: comment-out the photo part
# 2. htlatex CV_en.tex - on linux...
#
# afterwards use GoLive to 'clean' the output!
#
##
grep -v -E "^.photo.*$" ../CV_en.tex | sed -e "s/.cvcomputer\({.*}\)\({.*}\)\({.*}\)\({.*}\)/\\\cvitem\1\2\n\\\cvitem\3\4/" -e "s/.url\({[^}]*}\)/\\\weblink[Link]{\1}/g" -e "s/\\\LaTeX/LaTeX/" > CV_en.tex
htlatex CV_en.tex

ORG_FILENAME=CV_en.html
MOD_FILENAME=CV_en.sed.html
MODTMP_FILENAME=/tmp/CV_en.sed.html

CSS_FILENAME=CV_en.css
TMP_FILENAME=/tmp/sed.tmp

grep -v -e "^/\*.*\*/$" -e "^$" $CSS_FILENAME | grep -e "^.ec-lm*" | sed -e "s/{/\" \\/style=\"/" -e "s/}/\"/" -e "s/^\./class=\"/" -e "s/\ \"/\"/g" -e "s/\"\ /\"/g" -e "s/^/{s\//" -e "s/$/\/g}/" > $TMP_FILENAME

cat << EOF >> $TMP_FILENAME
{s/(ongoing/<BR>(ongoing/}
{s/>(every/><BR>(every/}
{s/<img src=".*\.png" alt="~ " class="tilde">/~/}
{s/<\/table>.nbsp./<\/table>/}
{s/class=\"td00\">$/valign=\"top\" class=\"td00\">/}
{s/^\ *<!--.*-->//}
{s/<p class=\"noindent\"><span style=\"font-size:109\(.*\)<\/p>/<span style="font-size:109\1/}
{s/\ *<p class=\"noindent\">\([^<>]*\)<\/p>/<span>\1<\/span>/}
{s/<p class=\"noindent\">PD Petra Ludewig and PD Helmar Gust<\/p>/PD Petra Ludewig and PD Helmar Gust/}
{s/<p class=\"noindent\">\(.*\)\(The basic computational linguistic processing stages from raw text documents towards a.*linguistically enriched annotation for documents are presented.*\)<\/p>/\1\2/}
EOF

tidy -i -wrap 1024 -o $MODTMP_FILENAME $ORG_FILENAME  
sed -i -f $TMP_FILENAME $MODTMP_FILENAME 

grep -v \
-e "^$" \
-e "link rel=\"stylesheet\"" \
-e "class=\"td00\">.nbsp.<.td>" \
$MODTMP_FILENAME > $MOD_FILENAME 
