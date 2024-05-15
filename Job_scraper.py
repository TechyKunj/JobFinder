import requests
from bs4 import BeautifulSoup
import time

known_skills = input('Provide your Familiar skill sets in comma-separated way: ')
known_skills = known_skills.split(",")

def scrap_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=").text

    soup = BeautifulSoup(html_text,'lxml')

    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        date_posted = job.find("span",class_="sim-posted").text.strip()
        skills = job.find("span",class_="srp-skills").text.replace(" ","").strip().split(",")

        if 'few' in date_posted and set(known_skills) & set(skills):
            company_name = job.find("h3",class_="joblist-comp-name").text.replace(" ","").strip()
            apply_link = job.header.h2.a['href']

            print(f'''
    Company name : {company_name}
    Skills needed : {skills}
    Apply link : {apply_link}
    ''')
            print("#############")

if __name__=="__main__":
    while True:
        scrap_jobs()
        print("waiting for 5 seconds")
        time.sleep(5)









    

   

