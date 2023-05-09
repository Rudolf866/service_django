import logging
from logging.handlers import RotatingFileHandler

info_log = logging.getLogger('logger')
info_log.setLevel(logging.DEBUG)

log_formatter = logging.Formatter("%(asctime)s : [%(levelname)s] : [%(filename)s].%(funcName)s() - %(message)s")

File = './logs/service_django.log'
#File = '/var/log/service_django/service_django.log'


handler = RotatingFileHandler(File, mode='a', maxBytes=5 * 1024 * 1024,
                              backupCount=5, encoding='utf-8')
handler.setFormatter(log_formatter)
handler.setLevel(logging.DEBUG)

info_log.addHandler(handler)
