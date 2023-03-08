 Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 
1. pull data out of HTML & XML
2. use parser let you navigate search and modify the parse tree.

- Tag 
  - Tag.name 
  - Tag.attribute
    - Multi-valued attributes
- NavigableString
- Beautifulsoup
- Comments and other special strings
- Navigating the tree
- Searching the tree 
  - Kinds of filters 
   - A string & regular expression & list & True & function
- Modifying the tree
---
1. 考虑到目标网站通过会不断维护迭代更新,所以 HTML 页面也是不断会被调整,所以 Scrape 通常会使用 Searching the tree 然后找到需要的
2. 通常会先使用 Searching the tree 然后找到需要的 tag 再进行数据解析获取

[beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
