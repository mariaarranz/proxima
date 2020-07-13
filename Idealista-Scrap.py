from selenium import webdriver
import pandas as pd
import time

url = "https://www.idealista.com/venta-viviendas/alicante-alacant/centro/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

x = 1
total = []
quotes = driver.find_elements_by_class_name("item-info-container")
for quote in quotes:
    descripcion = quote.find_element_by_class_name('item-link ').text
    #print(descripcion)
    
    precio = quote.find_element_by_class_name('item-price.h2-simulated').text
    precio = precio.replace('€', '')
    precio = precio.replace('.', '')
    #print(precio)

    count = len(driver.find_elements_by_css_selector("span.item-detail"))
    habitaciones = ''
    metros = ''
    planta = ''
    
    for i in range(1, (count + 1)):
        txt = "(//span[@class='item-detail'])[{num}]".format(num = x)
        detail = quote.find_element_by_xpath(txt).text

        word = "hab"
        if (word in detail) and (habitaciones == ''):
            habitaciones = detail
            x += 1
        else:
            habitaciones = ''
        
        if habitaciones != '':
            break
    #print(habitaciones)

    for i in range(1, (count + 1)):
        txt = "(//span[@class='item-detail'])[{num}]".format(num = x)
        detail = quote.find_element_by_xpath(txt).text

        word = "m²"
        if (word in detail) and (metros == ''):
            metros = detail
            x += 1
        else:
            metros = ''
        
        if metros != '':
            break
    #print(metros)

    for i in range(1, (count + 1)):
        txt = "(//span[@class='item-detail'])[{num}]".format(num = x)
        detail = quote.find_element_by_xpath(txt).text

        word = "planta"
        if (word in detail) and (planta == ''):
            planta = detail
            x += 1
        else:
            planta = 'NA'
        
        if planta != '':
            break
    #print(planta)

    new = ((descripcion,precio,habitaciones,metros,planta))
    total.append(new)

driver.quit()
df = pd.DataFrame(total,columns=['Descripcion','Precio','Habitaciones','Metros','Planta'])
print(df)
df.to_csv('Idealista.csv', index=False, encoding='utf-8-sig')
