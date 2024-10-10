import logging
import sys

# Определяем первый вид форматирования
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
# Определяем второй вид форматирования
format_2 = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

# Инициализируем первый форматтер
formatter_1 = logging.Formatter(fmt=format_1)
# Инициализируем второй форматтер
formatter_2 = logging.Formatter(
    fmt=format_2,
    style='{'
)

# Создаем логгер
logger = logging.getLogger(__name__)

# Инициализируем хэндлер, который будет перенаправлять логи в stderr
stderr_handler = logging.StreamHandler()
# Инициализируем хэндлер, который будет перенаправлять логи в stdout
stdout_handler = logging.StreamHandler(sys.stdout)

# Устанавливаем форматтеры для хэндлеров
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)

# Добавляем хэндлеры логгеру
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# Создаем лог
logger.warning('Это лог с предупреждением!')

# ----------------------------------------------------------

#  Хэндлер для записи логов в файл.
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log')

logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('Это лог с предупреждением!')