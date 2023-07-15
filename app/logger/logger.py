"""
Check my rating to HSU - модуль для создания регистратора
"""

from loguru import logger
logger.add('app/logger/info.log', level='DEBUG',
           rotation='10 MB', compression='zip', 
           serialize=True)
logger = logger