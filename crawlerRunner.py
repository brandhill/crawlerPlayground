# -*- coding: utf-8 -*-

import urllib2

from bs4 import BeautifulSoup
#
# url = "http://www.pythonforbeginners.com"
#
# content = urllib2.urlopen(url).read()
#
# soup = BeautifulSoup(content)
#
# # print soup.prettify()
#
# print 'hello 0'
# print soup.title.string


def getSomeThing():
    url = "http://www.pythonforbeginners.com"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    lis = []
    for li in soup.findAll('li'):
        if li.find('ul'):
            break
        lis.append(li)

    for li in lis:
        print li.text.encode("utf-8")


def saveToHtml():
    url = "http://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx"
    content = urllib2.urlopen(url).read()

    with open("Lotto649_history.html", "w") as f:
        f.write(content)


def getLotto649():

    soup = BeautifulSoup(open("Lotto649_history.html"))


    # for row in table_org.findAll("span", {"class": "html-attribute-value"}):
    #     print row
    #     # for ro1 in row.find("td",  {"class" : "td_org2"}):
    #     #     print ro1
    # table_org111 = soup.findAll("td", {"class": "td_w font_black14b_center"})
    # for t1t in table_org111:
    #     print t1t

    table_org = soup.findAll("table", {"class": "table_org td_hm"})
    for row in table_org:
        print row


        # td = row.findAll("td", {"class": "td_w font_black14b_center"})
        # print td
        # Lotto649Control_history_dlQuery_L649_DrawTerm_2

        # span = td.findAll('span')
        # print span
        print '\n<<<<<<<<<<<<\n'


