def get_contents(doc):
    soup = BeautifulSoup(doc, "lxml")
    contents = soup.text
    contents = contents.lower()
    return contents
