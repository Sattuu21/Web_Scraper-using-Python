from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering on the basis of {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=India&txtKeywords=software+developer+intern&txtLocation=India').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = job.find('span', class_="sim-posted").span.text
        if 'few' in published_date:
            name = job.find('h3', class_='joblist-comp-name').text.strip()
            company_name = name.replace("(More Jobs)", "").strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                with open('posts.txt', 'a') as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                    f.write(f"Timestamp: {datetime.now()}\n")
                    f.write('-' * 40 + '\n')
                print(f"Job posted by {company_name} saved.")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes..")
        time.sleep(time_wait * 60)
