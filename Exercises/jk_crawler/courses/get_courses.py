# encoding=utf-8

import requests
from bs4 import BeautifulSoup


def get_urls(base_url_, total_page):
    urls_ = []
    for i in range(1, total_page + 1):
        urls_.append(base_url_ + str(i))
    # print urls
    return urls_


base_url = "http://www.jikexueyuan.com/course/python/?pageNum="
urls = get_urls(base_url, 3)

for url in urls:
    print 'current url: ', url
    html = requests.get(url)
    # print html.text
    soup = BeautifulSoup(html.text, "html.parser")
    h2 = soup.find_all('h2', class_='lesson-info-h2')
    for title in h2:
        print title.text
