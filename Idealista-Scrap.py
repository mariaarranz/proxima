from selenium import webdriver
import pandas as pd
import time

url = "https://www.idealista.com/venta-viviendas/alicante-alacant/centro/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

items = len(driver.find_elements_by_class_name("item-info-container"))

total = []
quotes = driver.find_elements_by_class_name("item-info-container")
for quote in quotes:
    descripcion = quote.find_element_by_class_name('item-link ').text
    print(descripcion)
    
    precio = quote.find_element_by_class_name('item-price.h2-simulated').text
    precio = precio.replace('€', '')
    precio = precio.replace('.', '')
    print(precio)
    
    new = ((descripcion,precio))
    total.append(new)

df = pd.DataFrame(total,columns=['Descripcion','Precio'])
df.to_csv('Idealista.csv', index=False, encoding='utf-8-sig')
driver.quit()
