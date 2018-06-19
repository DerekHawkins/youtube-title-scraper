# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:48:26 2018

@author: Derek.Hawkins
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd


keywordInput = 'broadway play reviews' #Input what you would like to search on Youtube

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
df = pd.DataFrame()
youtube_data = []

#Validates the inquiry
try:
    myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "title-and-badge style-scope ytd-video-renderer")))
except TimeoutException:
    print('Error, element no longer found')
    browser.quit

#Loop needed to scroll the page
for scroll in range(8):
    body_elem.send_keys(Keys.END)
    time.sleep(3)
    body_elem.send_keys(Keys.HOME)
    time.sleep(3)

#Collects information on the page, stores into Dataframe   
titles_element = browser.find_elements_by_tag_name('h3')
youtube_titles = [x.text for x in titles_element]
meta_data = browser.find_elements_by_id('metadata')
meta_info = [x.text for x in meta_data]
df["Video Title"] = youtube_titles
df["Author"] = meta_info

#Dataframe manipulation and delimeter
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)
df[['Author','Views']] = df['Author'].str.split('•',expand=True)
df[['Views','Age of Video']] = df['Views'].str.split('views ',expand=True)

#Save to CSV
df.to_csv('C:\\Users\Derek.Hawkins\\Documents\\Python Training\\Test_Run_For_Marge.csv')
browser.quit


    
        
        
        
        