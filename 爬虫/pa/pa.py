import urllib.request
request = urllib.request.Request('http://www.baidu.com')
request.add_header('User-Agent','Mozilla/5.0')
response = urllib.request.urlopen(request)
print(response)