import vk_api 
from vk_api.utils import get_random_id 
from vk_api.bot_longpoll import VkBotLongPoll 
from vk_api.bot_longpoll import VkBotEventType 
TOKEN = '' 
vk_session=vk_api.VkApi(token=TOKEN ) 
vk=vk_session.get_api() 
longpoll = VkBotLongPoll(vk_session,'') 
for event in longpoll.listen():#Проверка действий 
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        #Проверяем пустое ли сообщение нам пришло 
        if event.obj.text != '':
        #Проверяем пришло сообщение от пользователя
            print(event.object.text)
            if event.obj.text == 'Привет' or event.obj.text == 'привет' or event.obj.text == 'Прив' or event.obj.text == 'прив' or event.object.text == 'Hi': 
                reply = 'Приветствую! Я бот Ильдар.'
            elif event.object.text == 'Что ты можешь?' or event.object.text == 'что ты можешь' or event.object.text == 'Что ты можешь' or event.object.text == 'что ты можешь?':
                reply = 'Я могу с вами поболтать (правда, в очень урезанном варианте), вывести вам таблицу истинности и прокомпилировать ваш код.'
            elif event.object.text == 'Таблица истинности' or event.object.text == 'таблица истинности':
                reply = '0 - Ложь, 1 - Истина\nA | B | A и B | A или B | не A\n0 | 0 |   0   |    0    | 1\n0 | 1 |   0   |    1    | 1\n1 | 1 |   1   |    1    | 0'
            elif event.object.text == 'Как дела?' or event.object.text == 'Как дела' or event.object.text == 'как дела?' or event.object.text == 'как дела':
                reply = 'Лучше не бывает!'
            #elif event.object.text == 'Научи меня python' or event.object.text == 'научи меня python' or event.object.text == 'Научи меня Python' or event.object.text == 'научи меня Python' or event.object.text == 'Научи меня python' or event.object.text == 'Научи меня Питону' or event.object.text == 'Научи меня питону' or event.object.text == 'научи меня Питону' or event.object.text == 'научи меня питону' or event.object.text == 'Python' or event.object.text == 'python' or event.object.text == 'Питон' or event.object.text == 'питон':
                #reply = 'Хорошо. Итак, в товарах группы есть все нужные тебе курсы. Возможно, их там не будет, это значит, что этому не учат. После покупки соответствующего курса с тобой свяжутся, и мы начнем обучение ;)'
                #reply = 'Извиняюсь, в данный момент паблик находится в разработке и в работу еще не вошел. Возможно, я уведомлю вас о начале работы.'
            elif event.object.text == 'Ты просто робот' or event.object.text == 'ты просто бот':
                reply = 'Ну... Да. И я этим горжусь'
            elif event.object.text[0:3] == 'Код' or event.object.text[0:3] == 'код':
                try:
                    reply = eval(event.object.text[4:])
                except:
                    reply = 'Что-то пошло не так...'
            else:
                reply = 'Не понял, просьба говорить корректно'
        else: 
            reply = '..?'
    print(reply)
