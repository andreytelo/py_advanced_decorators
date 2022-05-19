import datetime
import os


def loged(path):

    def _loged(old_function):

        def new_function(*args, **kwargs):
            start = datetime.datetime.today()
            result = old_function(*args, **kwargs)
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f' Start time - {start}, '
                        f' Name Function - {old_function.__name__},'
                        f' Argiments - {args} и {kwargs}'
                        f' Result - {result}\n'
                        )
            return result

        return new_function
    return _loged
