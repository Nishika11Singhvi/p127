import bs4 
from selenium import webdriver 
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["name", "distance", "mass", "radius"]
    star_data=[]

    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parcel")
        for ui_tag in soup.find_all("ui",attrs={"class":"expostar"}):
            li_tag=ui_tag.find_all("li")
            temp_list=[]
            for index,li_tag in numerate(li_tag):
                if index==0:
                    temp_list.append(li_tag.find_all("a"[0].contents[0]))
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath("").click()
    with open("scraper.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()
