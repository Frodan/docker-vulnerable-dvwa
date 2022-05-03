import requests

burp0_url = "http://project.local:80/setup.php"
burp0_cookies = {"PHPSESSID": "o0mgji18fsts2ihgvgmigor6r6", "security": "low"}
burp0_headers = {"Cache-Control": "max-age=0", "Origin": "http://project.local", "Upgrade-Insecure-Requests": "1", "DNT": "1", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://project.local/setup.php", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7", "sec-gpc": "1", "Connection": "close"}
burp0_data = {"create_db": "Create / Reset Database", "user_token": "82d506974a736e8f3f9a3a13e0f638fc"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)