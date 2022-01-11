import requests
from bs4 import BeautifulSoup   
from PIL import Image  
from io import BytesIO  

def parse(ex):
	try:
		#Сюда вставляется ссылка на сайт который будет парсится.
		URL = 'https://gdz.ru/class-10/algebra/alimov-15/{0}-nom/'.format(ex)
		#Здесь указываются заголовки для браузера, чтобы он не принял нас за бота и не ограничил доступ.
		HEADERS = {
			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		}

		#Получаем содержимое страницы в html виде
		response = requests.get(URL, headers = HEADERS)
		soup = BeautifulSoup(response.content, 'html.parser')
		
		#Находим тег изображения img и извлекаем оттуда ссылку.
		item = soup.findAll('div', class_='task-img-container')

		img = "https:"+item[0].find('img')['src']
		# print(soup)

		p = requests.get(img, headers = HEADERS)
		#Тут мы с помощью библиотек IO и PIL преобразуем изображение из байтового кода в нормальный формат jpeg. 
		#p.content - получает содержимое страницы в байтовом виде
		img = Image.open(BytesIO(p.content))
		url = 'assets/GDZ/10/algebra/{0}.jpg'.format(ex)
		img.save(url, 'jpeg')

		print('parse number {0} complete'.format(ex))
	except:
		print('download error')


i = 400
while i < 1625:
	parse(i)
	i+=1