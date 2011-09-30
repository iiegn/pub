#!/usr/bin/env python

import mailbox
import re,os

for message in mailbox.mbox('foobar'):
    # Date: Jan 05 20:57:01 2011
    # date -d "Jan 05 2011" +%a
    def addAbbrWkdy(mo):
        abbrWkdy = os.popen('date -d "'+mo.group(2)+" "+mo.group(3)+" "+mo.group(5)+'" +%a').read().strip()
        return mo.group(1)+" "+abbrWkdy+" "+mo.group(2)+" "+mo.group(3)+" "+mo.group(4)+" "+mo.group(5)
    msg = re.sub('(Date:) (...) ([0-9][0-9]) (..:..:..) (20..)', addAbbrWkdy, str(message))

    date = None
    date_search = re.search('\nDate: ... ... [0-9][0-9] ..:..:.. 20..\n', msg, 1)
    if date_search:
        date = re.sub('Date: ','',msg[date_search.start():date_search.end()].strip())

    msg = re.sub('\n>From wammu@wammu.sms\n', '', msg)
    msg = re.sub('\nFrom: Wammu <wammu@wammu.sms>\n', '\nFrom: Egon W. Stemle <+491792259314@wammu.sms>\n', msg)

    if date:
        msg = re.sub('^From nobody ... ... .. ..:..:.. 20..\n','From +491792259314@wammu.sms '+date+'\n', msg)

    print msg
