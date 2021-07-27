import random
import requests
import string
from random import randint

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


for i in range (2):
    print("Request number: {}" .format(i))
    randSize = randint(5, 15)
    username = id_generator(randSize)
    password= id_generator(randSize)
#send request
    files = {
        'email': (None, '{}@gmail.com'.format(username)),
        'passwd' : (None, password),
    }
    print('------------------------')
    print('requst number: {}'.format(i))
    print('Email:{}\nPassword:{}'.format('{}@gmail.com'.format(username),password))
    response= requests.post('domain', files = files)
