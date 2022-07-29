import re
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from requests import get


class GetSongLinks:
    def __enter__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get('https://www.letras.mus.br/')
        return self
        
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.driver.close()


    def get_link(self, song: str, artist: str):
        input_search = self.driver.find_element(By.ID, 'main_suggest')
        input_search.clear()
        input_search.send_keys(f'{song} {artist}')
        sleep(3)
        input_search.send_keys(Keys.ENTER)
        sleep(2)
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        first_link = list(filter( lambda item: item.get_attribute('class') == 'gs-title' , links))[0]

        return first_link.get_attribute('href')
    
    
def get_lyrics(link):
    soup = BeautifulSoup(get(link).text, 'html.parser')
    
    head = soup.find('div', {'class': 'cnt-head_title'})
    songname = head.find('h1').text
    artistname = head.find('span').text
    
    lyrics = re.findall(r'<p>.*?</p>', str(soup.find('div', {'class': 'cnt-letra p402_premium'})))
    lyrics = '\n\n'.join(
        paragraph
        .replace('<p>', '')
        .replace('</p>', '')
        .replace('<br>', '\n')
        .replace('</br>', '\n')
        .replace('<br/>', '\n')
        .strip()
        for paragraph in lyrics
    )
    
    return {
        'name': songname,
        'artist': artistname,
        'lyrics': lyrics
    }
        
        

# __all__ = ['get_song']


if __name__ == '__main__':
    with GetSongLinks() as driver:
        # print(driver.get_lyrics(driver.get_link('segura minha mão', 'davidson silva'))['lyrics'])
        print(driver.get_lyrics('https://www.letras.mus.br/davidson-silva/1737587/')['lyrics'])
    