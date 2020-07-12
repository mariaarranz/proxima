from selenium import webdriver
import pandas as pd
import time

url = "https://www.idealista.com/venta-viviendas/alicante-alacant/centro/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)


items = len(driver.find_elements_by_class_name("item-info-container"))-1

for item in range(items):
    quotes = driver.find_elements_by_class_name("item-info-container")
    for quote in quotes:
        descripcion = quote.find_element_by_class_name('item-link ').text
        print(descripcion)
        
        p = quote.find_element_by_class_name('item-price h2-simulated').text
        print(p)

        '''
        precios = quote.find_element_by_class_name('row price-row clearfix')
        for precio in precios:
            p = precio.find_element_by_class_name('item-price h2-simulated').text
            print(precio)
        '''
        
        #author = quote.find_element_by_class_name('author').text
        #new = ((quote_text,author))
        #total.append(new)

#df = pd.DataFrame(total,columns=['quote','author'])
#df.to_csv('quoted.csv')
driver.quit()


#driver.quit()
'''
print("Page Content:")
print(contenido)

#all_links = driver.find_elements_by_tag_name('a')
'''
