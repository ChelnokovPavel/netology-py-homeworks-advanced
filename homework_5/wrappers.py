from datetime import datetime


def logger(path):
    def _logger(foo):
        def func(*args, **kwargs):
            start = datetime.now()
            res = foo(*args, **kwargs)
            with open(f'{path}/logger.log', 'a') as f:
                f.write(f'{start}, {foo.__name__}, {args}, {kwargs}, {res}\n')
            return res
        return func
    return _logger
