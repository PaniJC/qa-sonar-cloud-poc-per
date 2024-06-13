import logging

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)

def log_info(message: str):
    log.level = logging.INFO
    log.info(message)

def log_error(message: str):
    log.level = logging.ERROR
    log.error(message)

def log_warning(message: str):
    log.level = logging.WARNING
    log.warning(message)

def log_debug(message: str):
    log.level = logging.DEBUG
    log.debug(message)

