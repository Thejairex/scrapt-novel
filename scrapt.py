from bs4 import BeautifulSoup
import requests


class Scrapt():
    def __init__(self, url) -> None:
        self.soup = self.getSoup(url)

    def getSoup(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        html_content = response.content
        return BeautifulSoup(html_content, 'html.parser')

    def getText(self):
        list_text = []
        cont = self.soup.find('div', attrs={'class': 'text-left'})
        texts = cont.find_all('p')
        for text in texts:
            list_text.append(text.text)

        return list_text

    def change_url(self, url):
        self.soup = self.getSoup(url)

    def getTitle(self):
        return self.soup.find('h1').text

    def getNext(self) -> str:
        link = self.soup.find('a', attrs={'class': 'btn next_page'})
        if link:
            return link['href']
        
        else:
            return ''


    def getPrev(self):
        link = self.soup.find('a', attrs={'class': 'btn prev_page'})
        if link:
            return link['href']
        
        else:
            return ''


if __name__ == '__main__':
    app = Scrapt('https://luminarynovels.com/novel/is-it-funny-that-the-dragon-slayer-failed-and-became-the-dragon-princess/volume-1-chapter-2/')

    print(app.getNext())
    print(app.getPrev())