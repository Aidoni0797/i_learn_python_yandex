# Добавьте условия в elif,
# допишите код в блоки elif и else.
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        # напишите ваш код здесь
        print('У вас 1 новое сообщение')
    elif messages_count <=4 and messages_count >=2:
        # напишите ваш код здесь
        print(f'У вас {messages_count} новых сообщения')
    else:
        # напишите ваш код здесь
        print(f'У вас {messages_count} новых сообщений')
