import bs4

with  open('index.html', 'r') as f:
    html = f.read

html = bs4.BeautifulSoup(html, "html.parser")

print(html.title.text)