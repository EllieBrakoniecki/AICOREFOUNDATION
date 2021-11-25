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

                    
# %%
Samuel_scraper = Scrape_Celebrity_IMDB('https://www.imdb.com/name/nm0000168/?ref_=nv_sr_srsg_0')
Samuel_movies = Samuel_scraper.scrape_movies()

Tim_scraper = Scrape_Celebrity_IMDB('https://www.imdb.com/name/nm0000619/?ref_=nv_sr_srsg_0')
Tim_movies = Tim_scraper.scrape_movies()
#%%
Samueldf= pd.DataFrame(Samuel_movies).transpose()
Timdf = pd.DataFrame(Tim_movies).transpose()

# %%
import sqlalchemy
import pandas as pd
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'halopancake6'
DATABASE = 'IMDB'
PORT = 5432
engine = sqlalchemy.create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# %%
from sqlalchemy.types import Integer, Text, String, DateTime

table_name = 'samuel'

Samueldf.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=True,
    chunksize=500,
    dtype={
        "Name": Text,
        "Year": Text,
          }
)

# %%
from sqlalchemy.types import Integer, Text, String, DateTime

table_name = 'tim'

Timdf.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=True,
    chunksize=500,
    dtype={
        "Name": Text,
        "Year": Text,
          }
)
# %%
engine.execute('''SELECT * FROM samuel''').fetchall()
Samuel = pd.read_sql_table('samuel', engine)
Samuel.head(10)

# %%
# Answers
# CREATE TABLE common AS 
# 	(SELECT s."Name" FROM samuel s
# 	 INNER JOIN tim t
# 	 ON s."Name" = t."Name");

# CREATE TABLE only_samuel AS 
# 	(SELECT s."Name" FROM samuel s
# 	 LEFT JOIN tim t
# 	 ON s."Name" = t."Name"
# 	 WHERE t."Name" is NULL);

# CREATE TABLE only_tim AS 
# 	(SELECT s."Name" FROM samuel s
# 	 RIGHT JOIN tim t
# 	 ON s."Name" = t."Name"
# 	 WHERE s."Name" is NULL);
