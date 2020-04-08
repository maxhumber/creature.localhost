from gazpacho import get, Soup

url = "http://localhost:5000/table"
html = get(url)

soup = Soup(html)

soup.find("td", {'class': "creature-name"})

table = soup.find("table")
trs = table.find("tr")[1:]

tr = trs[0]

name = tr.find("td", {"class": "creature"}, strict=False).text
habitat = tr.find("td")[-1].text

def parse_tr(tr):
    name = tr.find("td", {"class": "creature"}, strict=False).text
    habitat = tr.find("td")[-1].text
    return name, habitat

[parse_tr(tr) for tr in trs]
