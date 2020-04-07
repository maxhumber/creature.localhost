from gazpacho import get, Soup

url = "http://localhost:5000/page"
html = get(url)

soup = Soup(html)

creatures = soup.find("div").find("li")
gorgons = creatures[2].find("ul")

[g.text for g in gorgons.find("a")]
