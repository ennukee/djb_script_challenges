import re
from urllib import request
from bs4 import BeautifulSoup

with open('./output.csv', 'w') as f:
  page = request.urlopen('http://www.tsinetwork.ca/keyword-index/')
  soup = BeautifulSoup(page.read().decode(), 'html.parser')

  for link in soup.findAll('a', class_=re.compile("tag-link-\d*")):
    form = "{},{},{}\n"
    f.write(form.format(link.get_text(), link.get('title').split()[0].replace(',',''), link.get('href')))