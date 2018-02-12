"""eralchemy magic"""
__version__ = '0.0.1'

from .eralchemy import EralchemyMagic

def load_ipython_extension(ipython):
    ipython.register_magics(EralchemyMagic)