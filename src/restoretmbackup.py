#!/usr/bin/python

# crude helper to restore a 'Time Machine.app' backup on a linux system 
# (well, a non-OSX system...)
#
# starting from "How to access Time Machine files from Linux" at:
# http://www.macosxhints.com/article.php?story=20080623213342356
# here the steps are somewhat automated.
#
# ARG1: directory from where to descend and restore files
# ARG2: destination directory
# ARG3: directory whith the dir_* files
#
# eg.: 
# sudo this.py /media/osxbackup/Backups.backupdb/nikki/Latest/nikki foo/ /media/osxbackup/.HFS+\ Private\ Directory\ Data^M
# (you might not need to sudo...)

import os,sys,subprocess

strtdir = sys.argv[1]
dstdir = sys.argv[2]
hlnkdir = sys.argv[3]

def mkdir(dir):
    try:
        os.mkdir(dir)
        print "mkdir",dir
    except OSError:
        pass

def rsync(src,dst):
    execstrng = ['-lptgoD',src,dst]
    process = subprocess.Popen(execstrng, shell=True, executable='rsync', stdout=subprocess.PIPE)
    process.communicate()
    retcode = process.poll()
    print "rsync",src,"to",dst

def traverse(snode,dstnode):

    for root, dirs, files in os.walk(snode):

        ddir = os.path.join(dstdir,dstnode,root[len(snode)+1:])
        print "#>",snode,ddir

        for dir in dirs:
            mkdir( os.path.join(ddir,dir) )

        for name in files:
            try:
                statinfo = os.stat(os.path.join(root, name))
                link = statinfo.st_nlink
                linkdir = os.path.join(hlnkdir,"dir_"+str(link))
            
                if (os.path.isdir(linkdir)):
                    print "#l:",root,name,":",str(link)
                    mkdir( os.path.join(dstdir,dstnode,root[len(snode)+1:],name) )
                    traverse(linkdir,os.path.join(dstnode,root[len(snode)+1:],name))
                else:
                    src = os.path.join(snode,root[len(snode)+1:],name)
                    dst = os.path.join(dstdir,dstnode,root[len(snode)+1:],name)
                    rsync(src,dst)

            except OSError:
                print "#!",name,"did not work."

traverse(strtdir,"")
