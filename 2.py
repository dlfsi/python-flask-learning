from urllib import request, error


req = request.Request('http://zs.fang.com')
try:
    page = request.urlopen(req)

except error.HTTPError as e:
    if hasattr(e,'code'):
        print(e.code)
    elif hasattr(e,'reason'):
        print(e.reason)
else:
    print('no error')
    print(page.info)
