import time
import vk_api

#vk = vk_api.VkApi(login='login', password='password') #Авторизироваться как пользователь
vk_api.VkApi(token = 'a02d...e83fd') #Авторизоваться как сообщество
vk.auth()


def write_msg(user_id, s):
    vk.method('messages.send', {'user_id': user_id, 'message': s})
    values = {'out': 0, 'count': 100, 'time_offset': 60}
    vk.method('messages.get', values)


while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        write_msg(item[u'user_id'], u'your message')
    time.sleep(1)
