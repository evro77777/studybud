import time
from functools import wraps, lru_cache, singledispatch
from collections import abc
import numbers
import html

DEFAULT_FMT = '{dt:0.5f}s {name} ({args})->{res}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            res = func(*args)
            dt = time.perf_counter() - t0
            name = func.__name__
            arg_str = ', '.join(repr(arg) for arg in args)
            print(fmt.format(**locals()))
            # print(f'{dt:8f} {name}({arg_str}) -> {res} ')
            return res

        return clocked
    return decorate


@clock(fmt='{name}: {dt:0.8f}s')
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@lru_cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<p>{content}</p>'


@htmlize.register(numbers.Integral)
def _(n):
    return f'<pre>{n} (0x16_bit) </pre>'


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


factorial(6)
