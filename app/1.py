# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from urllib import request, error

'''
data = {}

data['name']='WHY'
data['location']= 'SDU'
data['language']= 'Python'

url_values=urllib.parse.urlencode(data)
print(url_values)

'''
req = request.Request('http://www.pythodn.org/a')

try:
    request.urlopen(req)

except error.URLError as e:
    if hasattr(e,'code'):
        print('Errcode',e.code)
    elif hasattr(e,'reason'):
        print('reason:',e.reason)
else:
    print('no error')
    #print(e.read())
    
    '''
    
try: response = urllib.request.urlopen('http://www.badidu.com/')

except urllib.error.URLError as e:
    print(e.reason)
    '''
