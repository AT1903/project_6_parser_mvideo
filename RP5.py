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

#текущая дата
date_today = datetime.date.today()

# print(f'Завтра: {date_today+timedelta(days=1)}')
# now = datetime.datetime.now()
# print(now.strftime("%d-%m-%Y"))
data_i = date_today
print(f'Сегодня: {data_i}')


dict_temp = {}
dict_out = {}
dict_headers = ['Дата', 'Температура']

#выгрузка привязки по времени
res_n_time = soup.find('div', class_ = 'ftab_content transition-02').find_all('tr')
res_n_time = [int(i.text) for i in res_n_time[1].find_all('td')[1:]]

#выгрузка температуры
res_temp = [int(i.getText()) for i in soup.find_all('div', class_= "t_0")]
#[print(f'{i} - {res_temp[i]}') for i in range(len(res_temp))]


print('==========================')

l_temp1 = []
l_temp2 = []
# dict_out[data_i] = []
#создаем словарь с данными
for i in range(len(res_n_time)):
    # print(f'datai - {data_i}')
    # print(f'dict_2 keys - {dict_2.keys()}')
    if data_i not in dict_temp.keys(): dict_temp[data_i] = []
    if data_i not in dict_out.keys(): dict_out[data_i] = []
    # print(f'{i} - {dict_out}')

    l_temp1.append(res_temp[i])     #температура - фактическая
    l_temp2.append(res_temp[i+25])  #температура - ощущается

    if res_n_time[i] == 23:
        dict_temp[data_i].append(l_temp1)
        dict_temp[data_i].append(l_temp2)

        dict_out[data_i].append(sum(l_temp1) / len(l_temp1))

        dict_out[data_i].append(sum(l_temp2) / len(l_temp2))

        l_temp1 = []
        l_temp2 = []

        data_i = data_i + timedelta(days=1)


print(tabulate([k,v] for k,v in dict_out.items()))
#создаем словарь с данными для вывода на экран
# dict_out = {}
# for key in dict_temp.keys():
#     dict_out[key] = []
# print(tabulate(dict_temp))
#
# print('---------------------------------')
# for k, v in dict_temp.items():
#     for y in v:
#         print(sum(y)/len(y))
# print('---------------------------------')
# print('************************************************')
# [print(k, [sum(v1)/len(v1) for v1 in v]) for k, v in dict_temp.items()]

# print(list(dict_temp))
# l_3 = []
# l_3.append(dict_temp.keys())
# print(l_3)


# print('************************************************')
# print('==========================')
#print(tabulate([k, [sum(v1)/len(v1) for v1 in v]) for k, v in dict_temp.items()]))
# print(dict_temp)
# print('=/////////////////////////////===')
# for ky, va in dict_temp.items():
#     print (sum(*va))
# print('=/////////////////////////////===')
#
# [print(k, sum(*v)/len(*v)) for k, v in dict_temp.items()]
#
# print(tabulate([k, v for k, v in dict_temp.items()]))

# print(tabulate([k, [sum(v1)/len(v1) for v1 in v] for k, v in dict_temp.items()], tablefmt='github', colalign=("center", "left") ,headers=dict_headers))#colalign=("right",)numalign="left",

# print('...........................')
# dict_temp[date_today] = []
# [print(k, v) for k, v in dict_temp.items()]
# print(':::::::::::::::::::::::::')
#print(dict_temp)
# print(*res_n_time, sep = '\n')
# for i in range(len(res_n_time)):
#     print(f'{i}: {res_n_time[i]}')
# print(('=========================='))

# res_temp = [int(i.getText()) for i in soup.find_all('div', class_= "t_0")]
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