from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link0">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link1">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link2">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, features='html.parser')
# print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.head)
print(soup.b)
print(soup.p)

markup = "<b><!--Hey, buddy. Want to buy a used parser?-->fff</b>"
soup1 = BeautifulSoup(markup, 'html.parser')
print(soup1.b.string)