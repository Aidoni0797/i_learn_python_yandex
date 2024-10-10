import logging

# переменная logger ссылается на экземпляр класса RootLogger с именем root и уровнем логирования WARNING.
logger = logging.getLogger()

print(logger)

#  ----------------------------------------------

# принято называть логгеры по имени модуля, в котором они создаются, а за имя модуля,
# как вы знаете, отвечает магическая переменная __name__
logger = logging.getLogger(__name__)

print(logger)

#  ----------------------------------------------

# что из себя представляет только что созданный объект класса Logger. Для этого передадим наш логгер в функцию dir
logger = logging.getLogger(__name__)

print(dir(logger))

#  ----------------------------------------------

logger = logging.getLogger()

print(logger.parent)

logger = logging.getLogger(__name__)

print(logger.parent)

#  ----------------------------------------------

logger_1 = logging.getLogger('one.two')

print(logger_1.parent)

logger_2 = logging.getLogger('one.two.three')

print(logger_2.parent)

# -----------------------------------------------

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG

logger.warning('Предупреждение!')
logger.debug('Отладочная информация')