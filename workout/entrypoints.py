#!/usr/bin/env python
# built-in
import sys


PROMPT = r"""
  _     _
 | |   (_)
 | |__  _ _ __ ___   _ __ ___   ___
 | '_ \| | '__/ _ \ | '_ ` _ \ / _ \
 | | | | | | |  __/ | | | | | |  __/
 |_| |_|_|_|  \___| |_| |_| |_|\___|
"""


def manage():
    from django.core.management import execute_from_command_line
    print(PROMPT)
    execute_from_command_line(sys.argv)


def wsgi(environ, start_response):
    import django
    from django.core.handlers.wsgi import WSGIHandler

    django.setup(set_prefix=False)
    application = WSGIHandler()
    return application(environ, start_response)
