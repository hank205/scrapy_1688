# scrapy_1688 Step 2

This script utilizes the [url.json] file generated from Step 1 to crawl the detail info of shops, which is saved to [nongji1688.json].   

Because some of the fields(like mobile phone number) in the contact info page can only be seen after log in the website, this script uses Cookies to imitate login.(I do not know how to write login code in python, so I seek help from Cookie :no_mouth:)  
1. First, we need to log in in the browser normally as a user.  
2. Then open the **Developer Tools** and click the **Network** tab.  
3. Choose a file and find the Headers and Cookie of your session.  
4. Copy them to [settings.py] and fill in the HEADER and COOKIES in [settings.py] with format given in the example in the code:
```python
HEADER = {
	......
}
```
```python
COOKIES = {
	......
}
```
