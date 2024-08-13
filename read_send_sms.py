import smpplib.client
import smpplib.consts
import smpplib.gsm
import smpplib.pdu
import threading
import requests

# Настройки соединения
host = '10.0.0.5'
port = 7777
username = 'username'
password = 'paswd'


# Создание SMPP клиента
client = smpplib.client.Client(host, port)

# Обработка входящих сообщений
def handle_sms(pdu):
    message_text = pdu.short_message.decode('utf-16be')
    number_sender = pdu.source_addr.decode('utf-8')
    print(f'Получено сообщение от {number_sender} {message_text}')
# Отправка полученного текста на другой номер
    send_sms = requests.post(
        'http://admin:admin@192.168.100.5/default/en_US/sms_info.html?type=sms',
        data={'line': '1',
            'smskey': '12345678',
            'action': 'SMS',
            'telnum': 'telefon',
            'smscontent': (f'SMS сообщение от: {number_sender} текст: {message_text}; ссылка на WhatsApp https://wa.me/{number_sender}'),
            'send': 'Send',})
    print(send_sms)


client.set_message_received_handler(handle_sms)

# Подключение к серверу и авторизация
client.connect()
client.bind_receiver(system_id=username, password=password)

# Ожидание входящих сообщений (в бесконечном цикле)
client.listen()

# Завершение соединения (если нужно прервать выполнение)
#client.unbind()
#client.disconnect()
