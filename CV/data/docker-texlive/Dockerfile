FROM fedora:latest
RUN dnf -y install \
    git \
    gpg \
    perl \
    perl-Getopt-Long \
    perl-Digest-MD5 \
    perl-Log-Log4perl \
    perl-YAML-Tiny \
    perl-Unicode-LineBreak \
    tar \
    wget \
    fontconfig \
    vim \
    ghostscript \
    which; \
    umask 002; \
    cd /usr/local/src \
&& \
    curl -sL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | tar zxf - \
&& \
    mv install-tl-20* install-tl \
&& \
    cd install-tl \
&& \
    echo "selected_scheme scheme-full" > profile \
&& \
    ./install-tl -profile profile

RUN dnf -y install \
    python-pygments \
    patch \
    libxcrypt-compat \
    ncurses-compat-libs \
    sharutils \
    libnsl \
&& \
    cd /tmp/; wget "ftp://ftp.gnu.org/gnu/ncurses/ncurses-5.9.tar.gz" \
&& \
    tar -xf ncurses-5.9.tar.gz \
&& \
    cd ncurses-5.9 \
&& \
    wget "https://invisible-mirror.net/archives/ncurses/5.9/patch-5.9-20141206.sh.gz" \
&& \
    gunzip patch-5.9-20141206.sh.gz \
&& \
    chmod +x ./patch-5.9-20141206.sh && ./patch-5.9-20141206.sh \
&& \
    ./configure --with-shared --without-normal --without-debug \
&& \
    make && make install 
    

ENV PATH /usr/local/texlive/2019/bin/x86_64-linux:$PATH
CMD ["tlmgr", "--version"]
