from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from datetime import timedelta
import requests
import datetime
from tabulate import tabulate

ua1 = UserAgent()
ua_rand = ua1.random
print(ua_rand)

url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%B1%D0%B5%D1%82%D1%82%D0%B5'

# headers = {
#             'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
#         }

headers = {
    'user-agent': ua_rand
}

res = requests.get(url, headers=headers)#, allow_redirects=False)
soup = BeautifulSoup(res.text, 'lxml')
#print(soup)
date_today = datetime.date.today()
print(f'Сегодня: {date_today}')
print(f'Завтра: {date_today+timedelta(days=1)}')


now = datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))

dict_temp = {}
print('...........................')
dict_temp[date_today] = []
[print(k, v) for k, v in dict_temp.items()]
print(':::::::::::::::::::::::::')
#print(dict_temp)




res_n_time = soup.find('div', class_ = 'ftab_content transition-02').find_all('tr')
res_n_time = [int(i.text) for i in res_n_time[1].find_all('td')[1:]]
#print(type(res_n_time))

res_temp = [int(i.getText()) for i in soup.find_all('div', class_= "t_0")]

data_i = date_today
print('==========================')
for i in range(len(res_n_time)):

    if data_i not in dict_temp : dict_temp[data_i] = []
    dict_temp[data_i].append(res_temp[i])
    if res_n_time[i] == 23:
        data_i = data_i+timedelta(days=1)

print('==========================')

[print(k, sum(v)/len(v)) for k, v in dict_temp.items()]


print(tabulate([(k, sum(v)/len(v)) for k, v in dict_temp.items()], tablefmt='github', stralign='center'))


# print(*res_n_time, sep = '\n')
# for i in range(len(res_n_time)):
#     print(f'{i}: {res_n_time[i]}')
# print(('=========================='))

res_temp = [int(i.getText()) for i in soup.find_all('div', class_= "t_0")]
# print(*res_temp, sep = '\n')
# for i in range(len(res_temp)):
#     print(f'{i}: {res_temp[i]}')
# print(('=========================='))



# print(res_n_time1[1].text)

# print(res_n_time[1].prettify())
# print(res_n_time.prettify())

# print(f'Размер списка: {len(res_n_time1)}')
# print('---------')
# num = 0
# for i in res_n_time1:
#     print(f'{num} - {i.text}')
#     num=num +1
# print(*res_n_time1, sep = '\n')



# res_temp = soup.find_all('div', class_= "t_0") #.find_all('a')
# //*[@id="forecastTable"]/tbody/tr[2]/td[2]

# for i in res_temp:
#     print(i.getText())


#
# for i in range(len(res_n_time1)-1):
#     print(f'Время {res_n_time1[i+1].text}:00 - температура {res_temp[i].text}')
#
#

# #print(*links_prod, sep = '\n')\
# #print(res_temp[0].getText())
# # print(*res_temp.getText(), sep='\n')


# res_n_time = soup.find('div', {'class': 'ftab_content transition-02'})
#res_n_time = soup.find('td', string='forecastTable') #ftab_content transition-02