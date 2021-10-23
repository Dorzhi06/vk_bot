import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEvent

statusDorzhi='Свободен'

vk_session = vk_api.VkApi(token='f1ab558b85ce25d5ccbb4bf0beb8f5f5cfa0b15580e9a4538b8f622cdc1db4ed3c15552a4a5ea2e2fd056')
session_api = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, '174268307')

def sender(id,text):
    vk_session.method('messages.send', {'user_id': id,'message':text,'random_id':0})
    print('I send Message')

print('i readiong')

for event in longpoll.listen():
    if str(event.type) == 'VkBotEventType.MESSAGE_NEW':
        print('input message')
        if event.message['text']=='.help':
            id=event.message['from_id']
            print('Me send Message')
            sender(id,'Список доступных команд (точка обязательна) \n1) .status - Проверка статуса Доржи\n2) .mess - Посмотреть письмо от Доржи')
        elif event.message['text']=='.status':
            id=event.message['from_id']
            print('Me send Message')
            sender(id, 'Статус Доржи: ' + statusDorzhi)
        elif event.message['text']=='.dorzhi0607-Занят':
            id = event.message['from_id']
            print('Me send Message')
            statusDorzhi='Занят'
            sender(id, 'Статус Доржи: ' + statusDorzhi)
        elif event.message['text'] == '.dorzhi0607-Свободен':
            id = event.message['from_id']
            print('Me send Message')
            statusDorzhi = 'Занят'
            sender(id, 'Статус Доржи: ' + statusDorzhi)
        elif event.message['text'] == '.mess':
            id = event.message['from_id']
            print('Me send Message')
            sender(id, 'Доржи вам ничего не оставил')
        else:
            id = event.message['from_id']
            sender(id, 'Напишите ".help", без КАВЫЧЕК ')
