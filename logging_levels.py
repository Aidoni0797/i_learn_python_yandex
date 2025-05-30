import logging

# 9-12 СТРОКИ. Мы написали 5 строк с логами разного уровня, а в консоли получили только три.
# Почему так?
# А дело в том, что по умолчанию вывод логов начинается только с уровня WARNING,
# то есть уровни DEBUG и INFO к сожелению ИГНОРИРУЕТСЯ.

# Строго говоря, есть еще и нулевой уровень NOTSET - Нельзя забывать!!!

# -------------------------------------------

# В библиотеке logging есть класс basicConfig, у которого есть параметр level,
# как раз и отвечающий за базовую настройку уровня логирования - класс basicConfig меняет жизнь - юху
# logging.basicConfig(level=logging.DEBUG)

logging.debug('Это лог уровня DEBUG')
logging.info('Это лог уровня INFO')
logging.warning('Это лог уровня WARNING')
logging.error('Это лог уровня ERROR')
logging.critical('Это лог уровня CRITICAL')




