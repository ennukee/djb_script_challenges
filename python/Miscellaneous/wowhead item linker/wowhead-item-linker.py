import re
import urllib.request
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time

def main(items = []):
  item_links = []
  url_base = 'http://www.wowhead.com/item={}&xml'
  for item in items:
    if not item:
      item_links.append(',')
      continue
    try:
      item = item.replace(' ','%20')
      url = url_base.format(item.lower())
      
      page = urllib.request.urlopen(url)
      with open('./input.xml','w') as f:
          f.write(page.read().decode())

      tree = ET.parse('./input.xml')
      root = tree.getroot()
      if 'error' in [x.tag for x in root]:
        item_links.append('{},error in search'.format(item))
      else:
        item_links.append('{},{}'.format(item.replace('%20',' '), root[0][-1].text))
    except Exception as e:
      item_links.append('{},failed'.format(item))
      print('{}: {}'.format(type(e).__name__, e))

  with open('./output.csv','w') as f:
    f.write('Item name,Link\n')
    f.write('\n'.join(item_links))

if __name__ == '__main__':
  items = []
  with open('./names.txt') as f:
    lines = f.readlines()
    for line in lines:
      items.append(line if line[-1] != '\n' else line[:-1])
  main(items)