try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Sigma',
    'description': 'A dungeon exploring game. Made using PyGame',
    'author': 'Tousif Khan',
    'url': 'Null',
    'author_email': 'khan.tousif719@gmail.com',
    'version': '0.0',
    'install_requires': ['nose', 'pygame'],
    'packages': ['Sigma'],
    'scripts': []
}

setup(**config)
