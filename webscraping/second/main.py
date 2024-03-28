from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
soup = bs(r.content, 'lxml')

# first_header = soup.find_all(["h1", "h2"])
# headers = soup.find_all("h2")
# paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# body = soup.find('body')
# div = body.find('div')
# header = div.find('h1')
# paragraphs = soup.find_all("h2", string=re.compile("(H|h)eader"))
# bold_text = soup.select("paragraph-id b")
#
# content = soup.select("div p")
# paragraphs = soup.select("body > p")
#
# for paragraph in paragraphs:
#     paragraph.select("i")
    # print(paragraph)

# print(soup.body.prettify())
# print(content)
# print(header.prettify())
# print(div.prettify())
# print(paragraph)
# print(body.prettify())

# header = soup.find("h2")
# header.string
# print(header.prettify())
#
# div = soup.find("div")
# print(div.prettify())
# print(div.get_text())

link = soup.find("a")
print(link['href'])

paragraphs = soup.select('p#paragraph-id')
print(paragraphs[0]['id'])

print(soup.body.find("div").find_next_siblings())
