import requests

# HTTP GET
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)

proxies = {
    "http": "http://192.168.181.101:7890",
    "https": "http://192.168.181.101:7890"
}
url = 'https://pvp.qq.com/matchdata/heroData.html?league_id=20230001'
r = requests.get(url, timeout=3, proxies=proxies)
# print(r.text)
print(r.headers)
print(r.request)
print(r.status_code)

# HTTP POST
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
# print(r.text)

# url params
url = 'http://httpbin.org/get'
payload = {'wd': 'python'}
rq = requests.get(url, params=payload)
print(rq.url)

w_url = 'https://pvp.qq.com/matchdata/heroData.html?league_id=20230001'
u_url = 'https://www.cnblogs.com/gl1573/p/9480022.html'
rqu = requests.get(u_url)
f = open('../../snapshot/a.html', 'wb')
f.write(rqu.content)
f.close()
