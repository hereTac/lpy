
# urllib  request
# it is not work

from urllib import request

h = open('../../snapshot/4request1.html', 'w')
with request.urlopen('https://pvp.qq.com/matchdata/heroData.html?league_id=20230001') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    h.write(data.decode('utf-8'))
    h.close()
