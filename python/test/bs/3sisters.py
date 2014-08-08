from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_doc2 = """<b class="boldest" id="1">boldest text</b>"""

soup = BeautifulSoup(html_doc)
head_tag = soup.head
title_tag = head_tag.contents[0]


soup2 = BeautifulSoup(html_doc2)
tag2 = soup2.b
head2_tag = soup2.head

