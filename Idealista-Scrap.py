from selenium import webdriver
import pandas as pd
import time

url = "https://www.idealista.com/venta-viviendas/alicante-alacant/centro/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)


items = len(driver.find_elements_by_class_name("item-price.h2-simulated"))-1

#p2 = len(driver.find_elements_by_css_selector('span.item-price.h2-simulated'))


precios = driver.find_elements_by_class_name("item-price.h2-simulated")

for precio in precios:
    p = precio.text
    p = p.replace("€","")
    print(p)

drive.close()
