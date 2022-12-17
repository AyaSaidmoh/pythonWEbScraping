import requests
import bs4
import csv
from itertools import zip_longest

pages=0
while True:
        if(pages>62):
                break
        else:
                job_title = []
                company_name = []
                company_location = []
                Reqirimentjob = []
                date_job = []
                url = f'https://forasna.com/a/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D9%88%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA-%D9%81%D9%89-%D9%85%D8%B5%D8%B1?a%5Bref%5D=bpnav%3D%7Bpage_num%7D&start={pages}'
                page = requests.get(url)
                soup = bs4.BeautifulSoup(page.content, "html.parser")
                #print(page.content)
                job_titles = soup.find_all("h2", {"class":"job-title" })

                #for i in job_titles:
                ## print(i.get_text())
                company_names = soup.find_all("span",{"class":"company-name"})
                #for i in company_names:
                #print(i.get_text())import requests

                Reqiriment_job = soup.find_all("div", {"class": "job-details"})
                 #for i in Reqiriment_job:
                           # print(i.get_text())
                company_locations = soup.find_all("span", {"class": "location-mobile"})
                # for i in company_locations:
                # print(i.get_text())

                date_jobs=soup.find_all("div", {"class": "date-item"})
                    #for i in date_jobs:
                        #print(i.get_text())

                for i in range(len(job_titles)):
                        job_title.append(job_titles[i].text.replace("\n",""))

                        company_name.append(company_names[i].text.replace("\n",""))

                        company_location.append(company_locations[i].text.replace("\n",""))

                        Reqirimentjob.append((Reqiriment_job[i].text.replace("\n","").replace("      ","").replace("\u200e3","").replace("\u200e5","").replace("-\u200e10","").replace("3-\u200e4","").replace("-\u200e","")))

                        date_job.append(date_jobs[i].text.replace("\n","").replace(" ",""))
                        print(job_title[i],company_name[i],company_location[i],Reqirimentjob[i],date_job[i])

                        print(pages)
                pages += 20









