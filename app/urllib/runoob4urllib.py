from urllib import request, parse, error, robotparser
url = 'https://www.runoob.com'
# myURL = request.urlopen("https://www.runoob.com/")
f = open('../../snapshot/a.html', 'w')
# f.write(myURL.read().decode('utf-8'))
# f.close()

# encode and unencode url
encode_url = request.quote(url)
print(encode_url)
print('---')
unencode_url = request.unquote(encode_url)
print(unencode_url)

# s_url = url + '/?s='
# keyworda = 'Python'
# key_code = request.quote(keyworda)
# a_url = s_url + key_code
header = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36'
                        ' (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'}
# s_request = request.Request(a_url, headers=header)
# respone = request.urlopen(s_request).read().decode('utf-8')
# f.write(respone)
# f.close()

p_url = 'https://www.runoob.com/try/py3/py3_urllib_test.php'
data = {'name': 'sdf', 'tag': 'sdfs'}
data = parse.urlencode(data).encode('utf-8')
print(data)
p_request = request.Request(p_url, data, headers=header)
respone = request.urlopen(p_request).read().decode('utf-8')
f.write(respone)
f.close()

e_url = 'https://www.runoob.com/s.html'
print(request.urlopen(p_url).getcode())
try:
    request.urlopen(e_url)
except error.HTTPError as e:
    if e.code == 404:
        print('404')

d_url = 'https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B'
o = parse.urlparse(d_url)
print(o)
print(o.netloc)
print(o.query)

rr = robotparser.RobotFileParser()
# rr.set_url('https://steamdb.info/robots.txt')
rr.set_url('https://www.musi-cal.com/robots.txt')
rr.read()
rrr = rr.request_rate("*")
print(rr.crawl_delay("*"))
print(rr.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
print(rr.can_fetch("*", "http://www.musi-cal.com/"))
