#!/usr/bin/env python
import sys

SNAKE = r"""
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
"""


def manage():
    from django.core.management import execute_from_command_line
    print(SNAKE)
    execute_from_command_line(sys.argv)


def wsgi(environ, start_response):
    import django
    from django.core.handlers.wsgi import WSGIHandler

    django.setup(set_prefix=False)
    application = WSGIHandler()
    return application(environ, start_response)
