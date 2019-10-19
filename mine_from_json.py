from hashlib import sha256
import urllib.request, json
from urllib.parse import urlencode
# ссылка на наш сервер
url = "http://192.168.0.12:5000/"
data = urllib.request.urlopen(url).read()
# вытаскиваем json структуру с сайта
output = json.loads(data)
print(type(output))
print(type(output['blocks']))
# Смотрим наши блоки
for i in range(len(output['blocks'])):
    print(type(output['blocks'][i]['hash']))

# Вытаскиваем последний хэш из словарей
lash_hash = output['blocks'][len(output['blocks']) - 1]['hash']
print(lash_hash)
msg = "kek5"
hsh = None
for x in range(10**100):
    s = lash_hash + msg + str(x)
    s = s.encode()
    hsh = sha256(s).hexdigest()
    if hsh.startswith('0000'):
        break
print(x)
print(hsh)
#составляем Post запрос
post_fields = {'text': msg, 'nonce': str(x)}
request = urllib.request.Request('http://192.168.0.12:5000/add', urlencode(post_fields).encode())
urllib.request.urlopen(request).read()
# for block in output['blocks']:
#     print(type(block))
#     print(block['hash'])