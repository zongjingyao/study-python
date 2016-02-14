# encoding=utf-8

import requests
from bs4 import BeautifulSoup

url = "http://ke.jikexueyuan.com/zhiye/cocos2d/"
print 'current url: ', url
html = requests.get(url)
# print html.text
soup = BeautifulSoup(html.text, "html.parser")
lesson_units = soup.find_all('section', class_='lesson-unit')

for lesson_unit in lesson_units:
    title = lesson_unit.find('header').find('h3').text
    print title

    lesson_steps = lesson_unit.find_all('table', class_='table lesson-step')
    for lesson_step in lesson_steps:
        step_name = lesson_step.find('thead').find("tr").find("th").text
        print '\t', step_name

        lessons = lesson_step.find("tbody").find_all("a")
        for lesson in lessons:
            print "\t\t", lesson.find("span").text
