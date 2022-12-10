import requests as req
from bs4 import BeautifulSoup as bs4

# buscando o html do site
html = req.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/271/curitiba-pr').content

soup = bs4(html, 'html.parser')

# coletando temperaturas e resumo sobre o clima
print('Temperatura em Curitiba:')
tempMin = soup.find(id='min-temp-1')
print(f'minima de {tempMin.text}')

tempMax = soup.find(id='max-temp-1')
print(f'maxima de {tempMax.text}')

textTemp = soup.find(class_='-gray -line-height-24 _center')
print(textTemp.text)
