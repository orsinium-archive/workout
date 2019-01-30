from setuptools import setup

reqs = open('requirements.txt').read().split()
reqs = [req for req in reqs if req[0] != '#']

name = 'workout'

setup(
    name=name,
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            name + ' = entrypoints:manage',
        ],
    }
)