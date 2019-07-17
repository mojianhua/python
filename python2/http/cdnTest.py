#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys,os
import urllib, urllib2
import base64
import hmac
import hashlib
from hashlib import sha1
import time
import uuid

class pushAliCdn:
    def __init__(self):
        self.cdn_server_address = 'http://cdn.aliyuncs.com'
        self.access_key_id = 'LTAIkRuM9CB7tPAs'
        self.access_key_secret = 'MnmnY1z7k1RWluzCtea2VaTT3k5fDD'

    def percent_encode(self, str):
        res = urllib.quote(str.decode(sys.stdin.encoding).encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def compute_signature(self, parameters, access_key_secret):
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k,v) in sortedParameters:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)
        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])
        h = hmac.new(access_key_secret + "&", stringToSign, sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature

    def compose_url(self, user_params):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        parameters = { \
                'Format'        : 'JSON', \
                'Version'       : '2014-11-11', \
                'AccessKeyId'   : self.access_key_id, \
                'SignatureVersion'  : '1.0', \
                'SignatureMethod'   : 'HMAC-SHA1', \
                'SignatureNonce'    : str(uuid.uuid1()), \
                'TimeStamp'         : timestamp, \
        }
        for key in user_params.keys():
            parameters[key] = user_params[key]
        signature = self.compute_signature(parameters, self.access_key_secret)
        parameters['Signature'] = signature
        url = self.cdn_server_address + "/?" + urllib.urlencode(parameters)
        return url

    def make_request(self, user_params, quiet=False):
        url = self.compose_url(user_params)
        #print url
        #刷新url
        try:
            req = urllib2.Request(url)
            res_data = urllib2.urlopen(req)
            res = res_data.read()
            return res
        except:
            return user_params['ObjectPath'] + ' refresh failed!'

if __name__ == '__main__':
    f = pushAliCdn()
    allUrl = ['http://www.food2china.com/','http://www.food2china.com/dist/','http://www.food2china.com/static/'];
    for val in allUrl:
        params = {'Action': 'RefreshObjectCaches', 'ObjectPath': val, 'ObjectType': 'directory'}
        res = f.make_request(params)
        print res

    # params = {'Action': 'RefreshObjectCaches', 'ObjectPath': 'http://www.food2china.com/api/fonts/iconfont.css', 'ObjectType': 'File'}
    # params = {'Action': 'RefreshObjectCaches', 'ObjectPath': 'http://www.food2china.com/', 'ObjectType': 'directory'}
    # res = f.make_request(params)
    # print res