import requests

response = requests.post(
    'http://admin:admin@192.168.100.2:2121/default/en_US/sms_info.html?type=sms',
    data={'line': '1',
          'smskey': '12345678',
          'action': 'SMS',
          'telnum': 'tefefon',
          'smscontent': 'Tekst_sms ',
          'send': 'Send',})
print(response)
