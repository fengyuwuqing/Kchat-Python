#!/usr/bin/env python
# coding=utf-8
"""
@author:'guoji'
@Email:guojie@xinfushe.com
@company:北京用友薪福社云科技有限公司
@createtime:2016/9/28--11:02
"""
import json
import urllib2
import sys
import base64

def deal_kf():
    username = 'XXXX'
    password = 'XXXX'
    base64string = base64.encodestring(
                    '%s:%s' % (username, password))[:-1]
    authheader =  "Basic %s" % base64string
    url = ['https://XXXXX.kf5.com/apiv2/chats.json']
    i = 1
    for theurl in url:
        print theurl
        req = urllib2.Request(theurl)
        req.add_header("Authorization", authheader)
        try:
            handle = urllib2.urlopen(req)
        except IOError, e:
            print "It looks like the username or password is wrong."
            sys.exit(1)
        thepage = handle.read()
        file = open('data_{0}.json'.format(i),'a')
        file.write(thepage)
        file.close()
        i+=1
        file_body = json.loads(thepage)

        if len(file_body['chats'])> 0:
            url.append(file_body['next_page'])


if __name__ == '__main__':
    deal_kf()