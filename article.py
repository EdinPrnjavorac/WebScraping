def LoadData(Link):
    page = requests.get(Link)

    website = BeautifulSoup(page.content, 'html.parser')
    for link in website.find_all('a'):
        try:
            if ('msn.com/article' in link['href']):
                with open(RawLinksPath, 'a') as RawLinksFile:
                    RawLinksFile.write(link['href'] + "\n")
            else:
                if ('/article/' in link['href']):
                    with open(RawLinksPath, 'a') as RawLinksFile:
                        RawLinksFile.write('http://www.msn.com' + link['href'] + "\n")
        except:
            pass

    article_title = website.find("h1", {"class": "article-headline"}).text
    article_author = website.find("span", {"class": "author"}).find('a').text
    article_timestamp_html = website.find("span", {"class": "timestamp"}).text
    article_timestamp = article_timestamp_html
    article_content_html = website.find("span", {"id": "article-text"})
    paragraphs = article_content_html.findAll('p')
    article_content = ''
    for paragraph in paragraphs:
        article_content += paragraph.text

    JSON_Website = {}
    JSON_Website['Link'] = Link
    JSON_Website['Title'] = article_title.strip()
    JSON_Website['Author'] = article_author.strip()
    JSON_Website['Timestamp'] = article_timestamp.strip()
    JSON_Website['Content'] = article_content.strip()