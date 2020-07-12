from selenium import webdriver
import pandas as pd
import time

url = "https://www.idealista.com/venta-viviendas/alicante-alacant/centro/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

items = len(driver.find_elements_by_class_name("item-info-container"))

total = []
quotes = driver.find_elements_by_class_name("items-container")
for quote in quotes:
    descripcion = quote.find_element_by_class_name('item-link ').text
    print(descripcion)
    
    precio = quote.find_element_by_class_name('item-price.h2-simulated').text
    precio = precio.replace('€', '')
    precio = precio.replace('.', '')
    print(precio)

    detail1 = quote.find_element_by_xpath("(//span[@class='item-detail'])[1]").text
    print(detail1)

    detail2 = quote.find_element_by_xpath("(//span[@class='item-detail'])[2]").text
    print(detail2)

    detail3 = quote.find_element_by_xpath("(//span[@class='item-detail'])[3]").text
    print(detail3)

    detail4 = quote.find_element_by_xpath("(//span[@class='item-detail'])[4]").text
    print(detail4)

    new = ((descripcion,precio,detail1,detail2,detail3))
    total.append(new)

df = pd.DataFrame(total,columns=['Descripcion','Precio','Habitaciones','Metros','Planta'])
df.to_csv('Idealista.csv', index=False, encoding='utf-8-sig')
driver.quit()
