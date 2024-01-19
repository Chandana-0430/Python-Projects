from bs4 import BeautifulSoup
import requests

while True:
      print('Skill you are familiar with')
      familiar_skill = input('>>')
      print(f"Filtering out {familiar_skill}")
      print()


      html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
      soup = BeautifulSoup(html_text,'lxml')
      jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

      for job in jobs:
            date_posted = job.find('span',class_='sim-posted').span.text
            if 'few' in date_posted:

               company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
               skills = job.find('span',class_='srp-skills').text.replace(' ','')
               more_info = job.header.h2.a['href']

               if familiar_skill in skills:

                    print(f"company name: {company_name.strip()}")
                    print(f"required skills: {skills.strip()}")
                    print(f"More Info: {more_info}")
                    print("")