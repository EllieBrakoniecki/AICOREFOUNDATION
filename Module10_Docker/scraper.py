#%%
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodedata
import numpy as np
import pandas as pd

class Scrape_Celebrity_IMDB:
    def __init__(self, url):
        self.url = url
        self.movies = {}
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url)        
        self.celebrity_name = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div/table/tbody/tr[1]/td/h1/span').text
        
    def scrape_movies(self):
        movies_web_object = self.driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[3]/div/div[3]/div[2]/div')
        for i, movie in enumerate(movies_web_object):
            movie_url_web_element = movie.find_element(By.XPATH, './b/a')
            # movie_url = movie_url_web_element.get_attribute('href')
            movie_name = movie_url_web_element.get_attribute('textContent')
            movie_date_web_element = movie.find_element(By.XPATH, './span')
            year = movie_date_web_element.get_attribute('textContent')
            year_cleaned = unicodedata.normalize("NFKD",year).strip('\n').strip()
            self.movies[i+1] = {'Name' : movie_name, 'Year' : year_cleaned}
        return self.movies

                    
if __name__ == '__main__':
    Samuel_scraper = Scrape_Celebrity_IMDB('https://www.imdb.com/name/nm0000168/?ref_=nv_sr_srsg_0')
    Samuel_movies = Samuel_scraper.scrape_movies()
    Samueldf= pd.DataFrame(Samuel_movies).transpose()
    print(Samueldf)

    # Tim_scraper = Scrape_Celebrity_IMDB('https://www.imdb.com/name/nm0000619/?ref_=nv_sr_srsg_0')
    # Tim_movies = Tim_scraper.scrape_movies()
# %%
