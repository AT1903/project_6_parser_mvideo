from fake_useragent import UserAgent
import requests

ua1 = UserAgent()

print(ua1.random)

url = 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search'
#url = 'http://free-proxy.cz/ru/'
#url = 'https://selenium-python.com/'
url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%B1%D0%B5%D1%82%D1%82%D0%B5'

headers = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }


# headers = {
#     'user-agent': ua1.random
#
# }

res = requests.get(url, headers=headers, allow_redirects=False)

print(res.text)