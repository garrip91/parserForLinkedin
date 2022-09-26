import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib
import fake_useragent

#HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36', 'accept': '*/*'}
session = requests.Session()
#HOST = 'http://mir-priaji.ru/'
HOST = 'https://www.linkedin.com/'
#link = 'http://mir-priaji.ru/auth/?login=yes'
link = 'https://www.linkedin.com/checkpoint/lg/login-submit'
user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

# data = {
	# "backurl": "/auth/",
	# "AUTH_FORM": "Y",
	# "TYPE": "AUTH",
	# "POPUP_AUTH": "N",
	# "USER_LOGIN": "nikolay.4everr@mail.ru",
	# "USER_PASSWORD": "123123",
	# "Login": [
		# "Войти",
		# "Войти"
	# ]
# }
data = {
    "csrfToken": "ajax:8888583087548089321",
    "session_key": "volodimir180886@gmail.com",
    "ac": "0",
    "sIdString": "cfa0ab33-874b-47b7-b688-30abe6d17741",
    "parentPageKey": "d_checkpoint_lg_consumerLogin",
    "pageInstance": "urn:li:page:d_checkpoint_lg_consumerLogin;2lfgoQzBRCWJa6qXNZ/A/g==",
    "trk": "",
    "authUUID": "",
    "session_redirect": "",
    "loginCsrfParam": "202bdce1-b67f-4ce7-83d8-5d7c5d3cd2f3",
    "fp_data": "default",
    "apfc": "{\"df\":{\"a\":\"LI+2my+6AZoRXNkTOTzO/g==\",\"b\":\"qQmF+ppWgxGsAIyGPy6o/7dB1toZ+Zf5RDvMhyjvRpNuoPXsceSgELZx5IrCjQH29EaqiEs49AYKd1XfzLAHAKBxQqxEWTRHupiRsRqobJPtibSiXa/ApzqohMQ7+0Sh73ESRExxL9Djb+4Eq+I2+bFYM0TBXscTmEyJg0Jidy3rSM6fgsud06aiHGlkZ6Nu6JCxUpAop85yPbd6KrZbinhFCCv+N4KzJo6QVZETv19/kMUFvcF2bfR/IQ/JSwKJxGBhThccpIXEfeAW160QM+mqNAAI9ZgsDT4VhpxQiXjXjD0VgyZImEASdVMVcWNqW45BjOqQ8xczTlPfVqMJzg==\",\"c\":\"vaZvk5sHOwQ1heU4rOEytaWydE6ivqW3J6u2tj7G3K2Lsbq0Ao7O/kvE2j+r01oi2dHRDr0Zg8KTdBp8s44SDsfuws0yQjKFIfvW9XCt…l5WXYv1huufPg4xRtH2njljJKQDrZTAKpsG5zzZ/Bu6fcMm3k0HYOGt5SJz17ev3AiHrFKX2Oe3l4viuRMgqruJWgXg6sn5VjlMVvLOuG+x0XWdto2mbaLYGqwyhXOBVqMavAGSgOOzhZsb6JP6R34NDV/+3g+VFNtyF1pWSLSpSrjCbiSDa1AHu7FP8wV6tSn6IjWJnyv+iNL9YxFQDy/DQzzS2+jskZsPpoTR8g9wVJ1XSWcu0qOuZp1QKfNX6KkGIJo4C5oOdAiWjHAE3oH2OkXA0WVUkZABLDRP8j9ethFVu5o+TGfXy9ZgYxlEgnYt3lvyGjXD6CpP75paQOr9utFDDD2NfZczVoYRdMK6vDnc5gPIZ1rcP+amnC69aVQ+e1XTTfvUTjVO+dqzUnezLRGJA0UCf7ccKPV6GdwjBZLyiJcwU6h+eTv9HTJklUFZgAcJLLto+AHLJV6TyHO5Oz9AAf1wMQzPQ+AoyA=\",\"d\":1,\"e\":2}}",
    "_d": "d",
    "showGoogleOneTapLogin": "true",
    "controlId": "d_checkpoint_lg_consumerLogin-login_submit_button",
    "session_password": "samadi123",
}

response = session.post(link, data=data, headers=header).text
print(response) # ТЕСТ АВТОРИЗАЦИИ



# def get_html(url, params=None):
    # r = session.get(url, headers=header, params=params)
    # return r

# def get_html2(url, params=None):
    # d = requests.get(url, headers=HEADERS, params=params)
    # return d

# def get_pages_count(html):
    # soup = BeautifulSoup(html, 'html.parser')
    # paginationTo = soup.find('div', class_='nums')
    # if paginationTo:
        # paginationTo = soup.find('div', class_='nums')
        # pagination = paginationTo.find_all('a') 
        # return int(pagination[-1].get_text())  
    # else:
        # return 1
        

    


# def get_content(html):
    # soup = BeautifulSoup(html, 'html.parser')
    # items = soup.find_all('div', class_='item_block col-4 col-md-3 col-sm-6 col-xs-6')
    
    # catalog = []
    # for item in items:
        # ImageLargePage = item.find('a').get('href'),
        # print(ImageLargePage)
        # ImageLargePage2 = str(ImageLargePage)[3:-3]
        # print(ImageLargePage2)
        # PageImageHref =str(HOST) + str(ImageLargePage2)
        # html2 = get_html2(PageImageHref)
  

        # soup2 = BeautifulSoup(html2.text, 'html.parser')
        # items2 = soup2.find('li', class_='current')
        # bb = items2.find('link').get('href')        
        # if bb:
            # bb = items2.find('link').get('href')   
        # else:
            # bb = ''      
        # items3 = soup2.find('div', class_='detail_text')
        # if items3:
            # text = str(items3.get_text)

            # text2 = text.replace('<br/>', '')

            # text3 = text2.replace('</div>>', '')

            # text4 = text3.replace('<bound method Tag.get_text of <div class="detail_text">', '')

        # else:
            # text4 = ''     


        # cost = item.find('div', class_='js_price_wrapper price')
        # numberOf = item.find('div', class_='js_price_wrapper price')
        # if cost and numberOf:

            # cost = cost.find('span', class_='values_wrapper')
            # print(cost)
            # cost2 = cost.get_text()
            # print(cost2)
            # cost3 = cost2.replace(' руб.', '')
            # print(cost3)
            # cost123 = ''.join(cost3.split())
            # print(cost123)
            
            # intcost = float(cost123)
            # print(intcost)
            # cost5 = intcost * 0.5 + intcost
            # print(cost5)
            # cost6 = float('{:.0f}'.format(cost5))
            # print(cost6)
            # cost7 = str(cost6)
            # print(cost7)
            # cost8 = cost7[:-2]
            # print(cost8)

            # visible = 'visible'
            
            
            # numberOf = numberOf.find('span', class_='price_measure')
            # numberOf2 = 'руб. ' + numberOf.get_text()
            # print(numberOf2)
        # else:
            # cost = 'Цену уточняйте' 
            # numberOf = ' '


        # catalog.append({
            # 'title': item.find('a', class_='dark_link').get_text(strip=True),
            # 'kategory': soup.find('h1', id='pagetitle').get_text(strip=True),
            # 'image': HOST + bb[1:],
            # 'kol-vo': item.find('span', class_='value').get_text(strip=True),
            # 'text': text4,
            # 'cost': cost8,
            # 'numberOf': numberOf2,
            # 'visible': visible
        # })
    # return catalog




# def save_file(items, path):
    # with open(path, 'w',  encoding='utf8', newline='') as file:
        # writer = csv.writer(file, delimiter=',')
        # writer.writerow(['Категории', 'Имя', 'Изображения', 'Описание', 'Базовая цена', 'Видимость в каталоге'])
        # for item in items:
            # writer.writerow([item['kategory'], item['title'], item['image'], item['text'], item['cost'], item['visible']])

# def parse():
    # for URL in [


    # 'http://mir-priaji.ru/catalog/vyshivanie_1/nabory_dlya_vyshivaniya/',  
    

    # ]:

        # html = get_html(URL)
        # if html.status_code == 200:
            # catalog = []
            # pages_count = get_pages_count(html.text)
            # for page in range (1, pages_count + 1):
                # print(f'Парсинг страницы {page} {pages_count} {URL}...')
                # html = get_html(URL, params={'PAGEN_1': page})
                # catalog.extend(get_content(html.text))
                # time.sleep(1)
            # FILE = 'parseResult' + '.csv'   
            # save_file(catalog, FILE)


            # print(f'Получено {len(catalog)} товаров')
        # else:
            # print('Error')    





# parse()