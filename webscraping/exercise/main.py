import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
webpage = bs(r.content, 'lxml')
url = "https://keithgalli.github.io/web-scraping/"

# ways to get social links from webpage
links = webpage.select("ul.socials a")
actual_links = [link['href'] for link in links]
# print(actual_links)
# print(links)

ulist = webpage.find("ul", attrs={"class": "socials"})
links = ulist.find_all("a")
# actual_links = [link['href'] for link in links]
# print(actual_links)

# get data from tables
table = webpage.select("table.hockey-stats")[0]
columns = table.find("thead").find_all("th")
column_names = [c.string for c in columns]
# print(column_names)

table_rows = table.find("tbody").find_all("tr")
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)
# print(l[0])

df = pd.DataFrame(columns=column_names)
# print(df.head())
# print(df.loc[df['Team'] != "Did not play"].sum())
# print(df['GP'])

# find words in sections

facts = webpage.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile("is")) for fact in facts]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]
# print(facts_with_is)

# download images
images = webpage.select("div.row div.column img")
images_url = images[0]['src']
full_url = url + images_url
img_data = requests.get(full_url).content
# with open('lake_como.jpg', 'wb') as handler:
    # handler.write(img_data)

# download search files from links
files = webpage.select("div.block a")
relative_files = [f['href'] for f in files]
for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content, 'lxml')
    secret_word_elements = bs_page.find("p", attrs={"id": "secret-word"})
    secret_word = secret_word_elements.string
    print(secret_word)
