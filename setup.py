from setuptools import setup

setup(name='eralchemy-magic',
      packages=['eralchemy_magic'],
      install_requires=['ipython-sql'],
      dependency_links=['git+https://github.com/psychemedia/eralchemy.git']
)