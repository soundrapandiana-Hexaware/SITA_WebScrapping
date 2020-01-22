import bs4 as bs
from selenium import webdriver
import requests
import pandas as pd
#driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
#from requests.auth import HTTPBasicAuth
#headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}

browser = webdriver.Chrome(executable_path=r'/Users/bablu/Downloads/chromedriver')
url = "https://www.planespotters.net/production-list/index"
browser.get(url)

# username = browser.find_element_by_name('username')
# username.send_keys('vdkaza')

# password = browser.find_element_by_name('password')
# password.send_keys('qwerty72')

# submitButton = browser.find_element_by_xpath("//button[contains(text(),'Login')]")
# submitButton.click()
html_source = browser.page_source
browser.quit()
soup = bs.BeautifulSoup(html_source, "lxml")
sub_url=[]
for link in soup.find_all('a', href=True):
    sub_url_='https://www.planespotters.net/'+link['href']
    sub_url.append(sub_url_)
for url_ in sub_url[21:]:
    
    browser = webdriver.Chrome(executable_path=r'/Users/bablu/Downloads/chromedriver')
    browser.get(url_)
    html_source = browser.page_source
    browser.save_screenshot("screenshot1.png")
    browser.quit()
    sub_soup = bs.BeautifulSoup(html_source, "lxml")
    data_ = []
    max_page = 1
    for data in sub_soup.findAll("div", {"class": "pages"}):
        data_.append (data.get_text().replace('\n',',').strip())
        max_page = int(data_[-1].split(',')[-2])
        for i in range(0,max_page):
            browser = webdriver.Chrome(executable_path=r'/Users/bablu/Downloads/chromedriver')
            data_url=url_+'?p='+str(i)
            browser.get(data_url)
            html_source = browser.page_source
            browser.quit()
            resub_soup = bs.BeautifulSoup(html_source, "lxml")
            data_ = []
            delivery=[]
            aircraft_Airline=[]
            status=[]
            final_data=[]
            for data in soup.findAll("div", {"class": "datatable dt-outline dt-striped"}):

                for data1 in data.findAll("div", {"class": "dt-td text-right dt-td-nowrap dt-col-sortable"}):
                    delivery.append(data1.get_text().strip())
                for data1 in data.findAll("div", {"class": "dt-td dt-td-min150 dt-col-sortable"}):
                    aircraft_Airline.append(data1.get_text().strip())
                for data1 in data.findAll("div", {"class": "dt-td dt-td-nowrap dt-col-sortable"}):
                    status.append(data1.get_text().strip())
            new_row=[]
            for craft,line,date_,stat in zip(aircraft_Airline[1::2],aircraft_Airline[::2],delivery,status[1::2]):
                new_row.append([craft,line,date_,stat])
                print(new_row)