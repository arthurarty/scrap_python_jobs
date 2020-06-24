import csv
import requests
from bs4 import BeautifulSoup


url = "http://pythonjobs.github.io"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
job_section = soup.find(class_='job_list')
job_divs = job_section.find_all('div', class_='job')
jobs = []

for job_div in job_divs:
    title = job_div.find('h1')
    detail = job_div.find('p', class_='detail')
    link = url + job_div.find('a')['href']
    job = {
        'Title': title.text.strip(),
        'Detail': detail.text.strip(),
        'Link': link
    }
    jobs.append(job)

with open('jobs.csv', mode='w') as csv_file:
    fieldnames = ['Title', 'Detail', 'Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(jobs)