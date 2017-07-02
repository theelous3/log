__all__ = [
    'config',
    'critical',
    'error',
    'warning',
    'info',
    'debug',
]
__author__ = 'Carl Bordum Hansen'
__license__ = 'MIT'


import inspect
import sys
from functools import partial
import time
import traceback


levels = {
    'CRITICAL': 50,
    'ERROR': 40,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
}

config = {
    'print_level': 'DEBUG',
    'file': sys.stdout,
    'asctime_format': '%Y-%m-%d %H:%M:%S',
    'output_format': '{asctime} - {module} - {message}',
}


def _log(level, message, *, exc_info=False):
    if levels[level] < levels[config['print_level']]:
        return
    asctime = time.strftime(config['asctime_format'])
    if '{module}' in config['output_format']:
        module = inspect.currentframe().f_back.f_globals['__name__']
    output = config['output_format'].format(
        message=message,
        module=module,
        asctime=asctime,
    )
    print(output, file=config['file'])
    if exc_info:
        traceback.print_exc(file=config['file'])


docstring = """\
Logs a *message* with level `{}`.

Args:
    message (str): the message to log.
    exc_info (bool): adds exception information to *message*. Default to False.

help(log) for more information about configuration.
"""

critical = partial(_log, 'CRITICAL')
error = partial(_log, 'ERROR')
warning = partial(_log, 'WARNING')
info = partial(_log, 'INFO')
debug = partial(_log, 'DEBUG')

critical.__doc__ = docstring.format('CRITICAL')
error.__doc__ = docstring.format('ERROR')
warning.__doc__ = docstring.format('WARNING')
info.__doc__ = docstring.format('INFO')
debug.__doc__ = docstring.format('DEBUG')
