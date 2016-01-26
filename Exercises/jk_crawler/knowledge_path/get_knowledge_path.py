# encoding=utf-8

import requests
from bs4 import BeautifulSoup

url = "http://www.jikexueyuan.com/path/python/"
print 'current url: ', url
html = requests.get(url)
# print html.text
soup = BeautifulSoup(html.text, "html.parser")
path_stages = soup.find_all('div', class_='pathstage mar-t30')

for stage in path_stages:
    title = stage.find('div', class_='pathstage-txt').find('h2').text
    print title
    lessons = stage.find_all('h2', class_='lesson-info-h2')
    for lesson in lessons:
        lesson_name = lesson.find('a').text
        print '\t', lesson_name
