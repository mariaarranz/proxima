from bs4 import BeautifulSoup
import requests
import scrapy
from urllib.request import Request, urlopen
from selenium import webdriver
import pandas as pd

url = "https://www.idealista.com/venta-viviendas/alicante-alacant/centro/"

driver = webdriver.Chrome()
driver.get(url)

