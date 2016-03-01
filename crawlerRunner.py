# -*- coding: utf-8 -*-

import urllib2
import re
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

    # url = "http://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx"
    # content = urllib2.urlopen(url).read()
    # soup = BeautifulSoup(content)

    # for row in table_org.findAll("span", {"class": "html-attribute-value"}):
    #     print row
    #     # for ro1 in row.find("td",  {"class" : "td_org2"}):
    #     #     print ro1
    # table_org111 = soup.findAll("td", {"class": "td_w font_black14b_center"})
    # for t1t in table_org111:
    #     print t1t

    # Lotto649Control_history_dlQuery_L649_DrawTerm_0

    table_org = soup.findAll("table", {"class": "td_hm"})
    # table_org = soup.findAll("table", attrs={'class':re.compile(r'(^td_hm$)')})
    for row in table_org:
        # print row


        # td = row.findAll("td", {"class": "td_w font_black14b_center"})
        # print td
        # Lotto649Control_history_dlQuery_L649_DrawTerm_2

        # span = td.findAll('span')
        # print span

        drawTerms = row.find_all('span', attrs={'id': re.compile(r'(^Lotto649Control_history_dlQuery_L649_DrawTerm)')})
        drawDates = row.find_all('span', attrs={'id': re.compile(r'(^Lotto649Control_history_dlQuery_L649_DDate)')})
        drawSequences = row.find_all('span', attrs={'id': re.compile(r'(^Lotto649Control_history_dlQuery_SNo)')})
        # specialNumber = row.find_all('span', attrs={'id': re.compile(r'(^SuperLotto638Control_history1_dlQuery_SNo)')})

        for item in drawTerms:
            print item.string

        for item in drawDates:
            print item.string

        for item in drawSequences:
            print item.string


        # print specialNumber[0].string

        print '\n<<<<<<<<<<<<\n'

    # drawTerms = soup.find_all('span', attrs={'id':re.compile(r'(^Lotto649Control_history_dlQuery_L649_DrawTerm)')})
    # drawDates = soup.find_all('span', attrs={'id':re.compile(r'(^Lotto649Control_history_dlQuery_L649_DDate)')})
    # drawSequences = soup.find_all('span', attrs={'id':re.compile(r'(^Lotto649Control_history_dlQuery_SNo)')})
    # # SuperLotto638Control_history1_dlQuery_SNo7_0
    #
    #
    # # Lotto649Control_history_dlQuery_SNo1_0
    #
    #
    # for item in drawTerms:
    #     print item.string
    #
    # for item in drawDates:
    #     print item.string
    #
    # for item in drawSequences:
    #     print item.string



