import telepot
token = '1178748794:AAHtbgK2dTod_7sp5J_NhL7PTXdgY8Su9Lg'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
