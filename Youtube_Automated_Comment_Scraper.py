# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:38:47 2018

@author: Derek.Hawkins
"""

#import bs4 as BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import TimeoutException
#import pandas as pd
import time

keywordInput = 'goarmy' #Input what you would like to search on Youtube

browser = webdriver.Chrome('C:\\Webdriver\\chromedriver')
browser.get(('https://www.youtube.com/'))
time.sleep(3)
# fill in search bar and hits enter
username = browser.find_element_by_name('search_query')
username.send_keys(keywordInput)
username.send_keys(u'\ue007')
time.sleep(1)

#find element to send keys to
body_elem = browser.find_element_by_tag_name('body')
#creates DataFrame and dictonary for titles
#df = pd.DataFrame()
youtube_data = []

youtubeFilter = browser.find_element_by_class_name('yt-simple-endpoint style-scope ytd-toggle-button-renderer')
browser.click(youtubeFilter)
time.sleep(1)
