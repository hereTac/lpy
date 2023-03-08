1. 为了方便查看 scrape 的内容,通常选择保存写入文本,文本操作记得 decode('utf-8') & close()
2. request 打开和读取 URL
3. encode & unencode url 
4. 简单搜索场景可通过 url 拼接,即 url/?q= 等拼接 url 即可实现搜索数据操作
5. 大部分场景通常需要自定义 ua 可在 request.Request 里设置 headers
6. 表单数据提交,通常用于登陆的场景, 可先构造好所需 data, 然后在 request.Request 里设置 data 
7. error.HTTPError 用于处理 request 抛出来的异常 e.code 获取返回码判断成功失败
8. parse.urlparse 用于解析处理 URL 
9. robotpasrser.RobotFileParser 解析 robots.txt 文件,用于抓取网站允许抓取的网页(通常用的较少)
10. [Python urllib、urllib2、urllib3用法及区别](https://www.cnblogs.com/onefine/p/10499342.html)
