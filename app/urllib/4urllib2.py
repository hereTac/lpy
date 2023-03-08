# urllib  request
# it is not work

from urllib import request
req = request.Request('https://pvp.qq.com/matchdata/heroData.html?league_id=20230001')
req.add_header('user-agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
