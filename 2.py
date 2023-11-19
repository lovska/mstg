import requests
from pprint import pprint
import time
import random

URL = 'https://api.telegram.org/bot'
TOKEN = 'СВОЙ ТОКЕН'

offset = 0

sample_frases = ["привет", "как дела", "сколько время"]
sample_answers = ["Здарова", "Норм", "Сам позырь"]

while True:
    response = requests.get(URL + TOKEN + "/getUpdates?offset=" + str(offset))
    updates = response.json()['result']

    if updates != []:
        # Обработайте каждое обновление
        for update in updates:
            # Обновите значение offset после успешной обработки обновления
            offset = update['update_id'] + 1

            message = updates[-1]['message']
            chat_id = message['chat']['id']
            text = message['text']

            if text in sample_frases:
                num_index = sample_frases.index(text)
                requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
            else:
                requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text=Я тебя не понимаю')
    else:
        # Если нет новых обновлений, вы можете добавить задержку перед следующим запросом, чтобы не нагружать сервер
        print("Обновлений нету!", updates)
        time.sleep(2)
