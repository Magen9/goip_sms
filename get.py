import requests

tekst_sms = "teskst_sms"
tel = "number_of_telefon"

reg = requests.get('http://192.68.100.22:2121/default/en_US/send.html?u=admin&p=admin&l=1&n=' + tel + '&m=' + tekst_sms +'')

print(reg)
