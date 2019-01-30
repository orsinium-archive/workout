# external
from setuptools import setup, find_packages


reqs = open('requirements.txt').read().split('\n')
reqs = [req.split()[0] for req in reqs if req.split() and req[0] != '#']

name = 'workout'

setup(
    name=name,
    install_requires=reqs,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            name + ' = workout:manage',
        ],
    },
)
