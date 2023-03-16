1. 通常目前的 Web 主要分为静态和动态,且目前大部分较有数据价值信息的网站通常会维护更新,且技术采用的是动态页面,部分老旧且较低频率维护的网站采用的是静态页面,基于此当我们使用 Python 去获取一些有价值的网站数据时,往往面对的都是动态页面.
2. 目前动态页面的数据获取主要分为两种
   1. 分析页面的数据接口,找到数据接口,请求数据接口方式去获取数据 
   2. 通过 Selenium(C#/RubyJava/Python/JavaScript) Playwright(JavaScript/Python/.NET/ Java) Puppeteer(Node.js) Cypress(JavaScript) 等 Web 自动化测试软件,即通过模拟启动浏览器来访问目的网站并获取数据
3. 针对上述两种方式优缺点分析
   1. 2.1 缺点: 有些网站不希望被外部直接找到接口,所以有时候接口参数较多,且参数名取名含义不太清晰的,逆向探索过程会耗费比较多的时间.
   2. 2.1 优点: 通过分析页面数据接口方式,因为考虑到接口的变动是较为低频的,所以这是比较"直截了当"的方式.
   3. 2.2 缺点: 此方式的内存占用会更大且目标页面一般会比较频繁的迭代更新,所以爬虫代码也通常需要跟进更新.
   4. 2.2 优点: 通过模拟浏览器方式去获取数据，可以免除逆向去探索数据接口的过程,尤其是目前有价值的网站数据(各方面包括接口)通常会做一定的防护,逆向过程(探索接口含义的这个过程)通常较为繁琐且耗时
4. 实践 2.1
   - 无痕模式下打开 https://pvp.qq.com/matchdata/heroData.html?league_id=20230001
   - F12 -> Network -> Fetch/XHR -> Preview -> 寻找合适的请求,重点关注有 data 返回的请求 -> 确定 X 请求,打开 Headers 找到 Request URL  
   - Done  https://prod.comp.smoba.qq.com/leaguesite/league/hero/settle_list/open?league_id=20230001
    4.2 
5. 实践 2.2
   - X TODO

