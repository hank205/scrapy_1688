# scrapy_1688 Step 1

This script crawls the urls of shop contact pages on www.1688.com, with the keyword '农机' and save to [urls.json].  

### To change the keyword  
search with your desired keyword on www.1688.com, copy & paste the result url to [nongji1688_spider.py] and change  
line 12  
```python
start_urls = [
	"http://www.1688.com/chanpin/-C5A9BBFAC5E4BCFE.html?spm=a261b.2187593.1996074689.2.cPWaDw&beginPage=1/"
]
```
&  
line 33 
```python 
for id in range(2, 10):
 	id = "http://www.1688.com/chanpin/-C5A9BBFAC5E4BCFE.html?spm=a261b.2187593.1996074689.2.cPWaDw&beginPage=" + str(id)
 	yield Request(id, callback=self.parse)
```

### To increase crawling pages
change the loop bounds at line 32
```python
for id in range(2, 10):
```

### Known issues:  
Every result page is not fully displayed, and need to be scrolled down to display more in browser. I don't know how to handle this (maybe) javascript stuff. Thus, I only crawled the initial displayed shops(about 1/3 of fully displayed shops) in every result page. But since the result pages are listing products by shops, the shop name(& url) will repeat many times. As along as we increase the pages we crawl, we'll get a considerable amount of shop names.