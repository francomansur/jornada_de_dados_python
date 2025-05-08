# decorators.py
from functools import wraps

from loguru import logger


def log_atividade(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Iniciando função: {func.__name__}")
            resultado = func(*args, **kwargs)
            logger.success(f"Função '{func.__name__}' executada com sucesso.")
            return resultado
        except Exception as e:
            logger.error(f"Erro na função '{func.__name__}': {e}")
            raise

    return wrapper
